#!/usr/bin/env python

import pandas as pd
import subprocess
import shutil
import re
from pathlib import Path

HERE = Path(__file__).parent
RAW_DIR = HERE / 'data-raw'
PDF_DIR = RAW_DIR / 'pdf'
TXT_DIR = RAW_DIR / 'txt'
CSV_DIR = RAW_DIR / 'csv'
CLEAN_DIR = HERE / 'data-clean'
CLEAN_FILE = CLEAN_DIR / 'dhcr-rgb-rent-stabilized-buildings-2017.csv'


def make_dir(dir_path):
    shutil.rmtree(dir_path, ignore_errors=True)
    dir_path.mkdir(parents=True)


def parse_text_to_csv(text_file, csv_file):
    with open(text_file, 'r') as f:
        all_lines = f.read().splitlines()

    is_first_header = True
    with open(csv_file, 'w') as f:
        for line in all_lines:

            if re.search(r'^Z', line):
                row_type = 'header'
                # Each page of the PDF uses different fixed-width positions, so every time
                # we get to a new header row we need to reset the indexes used to split
                # the lines into columns.
                starts = [m.start(0) for m in re.finditer(r'\w+', line)]
            elif re.search(r'^[1-9]', line):
                row_type = 'data'
            else:
                continue

            # Process and write the header row only on the first occurrence.
            if row_type == 'header':
                if is_first_header:
                    is_first_header = False
                else:
                    continue

            # Split the lines into columns, strip/squish whitespace, add commas, write to file.
            split_line = [line[i:j] for i, j in zip(starts, starts[1:] + [None])]
            split_line = [re.sub(r'\s+', ' ', i.strip()) for i in split_line]
            csv_line = ','.join(split_line)

            f.write(csv_line + '\n')


def scrape_pdfs_raw(pdf_dir, txt_dir, csv_dir):
    for pdf_file in pdf_dir.glob('*.pdf'):
        txt_file = txt_dir.joinpath(pdf_file.stem + '.txt')
        csv_file = csv_dir.joinpath(pdf_file.stem + '.csv')

        subprocess.call(['pdftotext', '-table', '-enc', 'UTF-8', pdf_file, txt_file])

        parse_text_to_csv(txt_file, csv_file)


def clean_csvs(raw_dir, clean_file):
    for f in raw_dir.glob('*.csv'):
        (pd.read_csv(f, dtype=str)
         .rename(columns=str.lower)
         .assign(bbl=lambda x: x['county'].replace({'62': '1', '60': '2', '61': '3', '63': '4', '64': '5'})
                               + x['block'].str.pad(5, 'left', '0')
                               + x['lot'].str.pad(4, 'left', '0'))
         .assign(address1=lambda x: x['bldgno1'].str.replace(' TO ', '-') + ' ' + x['street1'] + ' ' + x['stsufx1'])
         .assign(address2=lambda x: x['bldgno2'].str.replace(' TO ', '-') + ' ' + x['street2'] + ' ' + x['stsufx2'])
         .filter(['bbl', 'address1', 'address2', 'zip', 'status1', 'status2', 'status3'])
         .to_csv(clean_file, index=False, mode='a', header=(not clean_file.exists())))


def main():
    make_dir(TXT_DIR)
    make_dir(CSV_DIR)
    make_dir(CLEAN_DIR)

    scrape_pdfs_raw(PDF_DIR, TXT_DIR, CSV_DIR)

    clean_csvs(CSV_DIR, CLEAN_FILE)


if __name__ == '__main__':
    main()
