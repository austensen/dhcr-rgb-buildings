FROM python:3.7

ARG XPDF_VERSION=4.02

# https://github.com/JustFixNYC/nyc-doffer/blob/master/Dockerfile
RUN curl https://xpdfreader-dl.s3.amazonaws.com/xpdf-tools-linux-${XPDF_VERSION}.tar.gz > /xpdf.tar.gz \
  && tar -zxvf /xpdf.tar.gz \
  && cp xpdf-tools-linux-${XPDF_VERSION}/bin64/pdftotext /bin \
  && rm -rf xpdf-tools-linux-${XPDF_VERSION} \
  && rm /xpdf.tar.gz

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

CMD ["python", "scraper.py"]
