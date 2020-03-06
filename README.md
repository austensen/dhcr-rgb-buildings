This project scrapes PDF documents published by the NYC Rent Guidelines Board (RGB) listing buildings that contain rent stabilized units. 

For more information on the buildings list refer to the [RGB website](https://rentguidelinesboard.cityofnewyork.us/resources/rent-stabilized-building-lists/). 
The contents of that page are copied below in case the page is moved/changed/deleted. 

<details><summary>Click to expand - RGB website contents</summary>
<p>

> #### Buildings That Contain Rent Stabilized Units
> On this page, you will find general guidelines for identifying if your apartment may be rent stabilized as well as downloadable listings of buildings in New York City that contain rent stabilized apartments. The lists do not indicate which apartments in these buildings are rent stabilized, but rather, only those buildings that contain at least one rent stabilized unit. Also below is a link to NYS Homes and Community Renewal’s (HCR) searchable database of buildings that may contain rent stabilized units.
> 
> _Note: The NYC Rent Guidelines Board does not have any information concerning whether any particular apartment is rent stabilized._
> 
> #### How to Tell If a Building Is Rent Stabilized
> In general, rent stabilized buildings:
> - Contain 6 or more units;
> - Were built before 1974;
> - Are not co-ops or condos;
> 
> However, not all apartments in these buildings may be rent stabilized. For an apartment to be stabilized it should:
> - Have had a rent of less than $2,000, if a tenant initially moved into the apartment between 1993 and June 23, 2011. 
> - Have had a rent of less than $2,500, if a tenant initially moved into the apartment between June 24, 2011 and June 14, 2015. 
> - Have had a rent of less than $2,700, if a tenant initially moved into the apartment since June 15, 2015.
> - Have had a rent of less than $2,733.75, if a tenant initially moved into the apartment after December 31, 2017.
> - Have had a rent of less than $2,774.76, if a tenant initially moved into the apartment after December 31, 2018 but prior to June 14, 2019.
> 
> There are many exceptions to these rules. For instance, if you moved into the apartment before the building was converted to a co-op, the apartment may be stabilized. Also, newly constructed buildings that receive 421-a or J-51 tax exemptions may be rent stabilized, even if the rent exceeds the above rent thresholds.
> 
> Our rent stabilized building lists only include buildings whose owners registered with the NY State Homes and Community Renewal (HCR). If an owner filed after the lists were compiled or not at all, a building will not be on our lists but may still contain rent stabilized apartments.
> 
> The only way to know if your apartment is rent stabilized is to contact [NYS Homes and Community Renewal (HCR)](https://hcr.ny.gov/office-rent-administration-ora#contact-ora), the state agency which administers the rent laws.
>
> #### How to Use the Rent Stabilized Building Listings
> 1. Buildings are grouped by zip code. Within each zip code, buildings are sorted first by street name and then by building number. 
> 2. Some buildings have multiple addresses. If a building has two addresses (e.g. 415 E. 52nd, also known as 404 E. 53rd), both addresses are in the list.  
> 3. The lists also indicate some additional information about the building if it was available:  
  > - Co-op or condominium status: If the building is a co-op or condominium, renters who move in AFTER the conversion date are NOT protected by rent stabilization regulations.
  > - 421a or J-51: Buildings which are listed as “421-a” or “j-51” are stabilized because they took advantage of the 421-a or J-51 tax exemption program. These buildings remain rent stabilized for the length of the tax exemption, and thereafter may be deregulated if the buildings were not stabilized prior to the participation in the tax exemption program.
  > - Multiple Dwelling Class: Hotel or Rooming House/Class B Multiple Dwelling status indicates a multiple dwelling which is generally occupied transiently. A Class A Multiple Dwelling generally is occupied as a permanent residence and are mostly apartment houses.
  > - Type of Structure: hi-rise, garden complex, etc.
  > - HCR [provides a list of definitions](https://apps.hcr.ny.gov/BuildingSearch/popup.aspx) of Rent Regulation and Building Status terms as well as a further explanation of buildings contained in these listings.
> 4. The lists do not include owner information. However, you can find owner information, as well as a wealth of other building-specific information, on these NYC.gov web sites: 
  > - [NYC Department of Buildings – Buildings Information System](http://a810-bisweb.nyc.gov/bisweb/bsqpm01.jsp)
  > - [NYC Department of Housing Preservation and Development – HPDOnline](https://www1.nyc.gov/site/hpd/about/hpd-online.page)
  > - [NYC Department of Finance – Automated City Register Information System (ACRIS)](http://www1.nyc.gov/site/finance/taxes/acris.page)
  > - [NYC Department of Finance – Property Tax Benefit Information (e.g. 421-a, J-51)](https://a836-pts-access.nyc.gov/care/forms/htmlframe.aspx?mode=content/home.htm)
>   
> #### NYC Rent Stabilized Building Listings
> - Listings are in pdf format. If you are unable to view the pdf, download the Adobe reader for free. If you are having trouble installing or using the Adobe reader, please see their troubleshooting page.
> - If you are looking up a particular building and are not sure of its zip code, you can find it on the U.S. Postal Service website.
> - HCR provides a list of definitions of Rent Regulation and Building Status terms as well as a further explanation of buildings contained in these listings.
> - [**Manhattan**](https://rentguidelinesboard.cityofnewyork.us/wp-content/uploads/2019/10/2017manhattanbldgs.pdf)
> - [**Brooklyn**](https://rentguidelinesboard.cityofnewyork.us/wp-content/uploads/2019/10/2017brooklynbldgs.pdf)
> - [**Bronx**](https://rentguidelinesboard.cityofnewyork.us/wp-content/uploads/2019/10/2017bronxbldgs.pdf)
> - [**Queens**](https://rentguidelinesboard.cityofnewyork.us/wp-content/uploads/2019/10/2017queensbldgs.pdf)
> - [**Staten Island**](https://rentguidelinesboard.cityofnewyork.us/wp-content/uploads/2019/10/2017statenislbldgs.pdf)
>
> **Data Source:** 2017 Building Registrations filed with NYS Homes and Community Renewal (HCR).
> 
> #### Statewide Rent Regulated Building Search on HCR’s Website
> The buildings that will be listed on HCR’s web site have filed records with the NYS Homes and Community Renewal at least one time from 1984 to the present year and may contain one or more regulated apartments. Inclusion on the list is not determinative of the building’s current status. The list is searchable by either address and/or zip code and include both buildings within and outside of NYC. However, the list may not include all buildings that have rent regulated tenants:
> 
> [HCR Registered Building Search](https://apps.hcr.ny.gov/BuildingSearch/)

</p>
</details>  

## How it works

The original PDF documents are likely to disappear from the RGB website, as the prior year's files already have, so they are all saved in this project [here](/data-raw/pdf).

In this project [`pdftotext`](https://www.xpdfreader.com/pdftotext-man.html) is used to convert the original PDF files to plain text files, which are available [here](data-raw/txt). 

The plain text files are essentially fixed-width format, with extra unnecessary lines and the fixed-width positions can change for each page. Python is used to parse the text files and convert them into csv files without any other alteration of the data, the csv files are available [here](data-raw/csv).

Finally, all the separate borough raw csv files are stacked together and cleaned up for ease of use. The address fields are joined together for simplicity, some other less useful columns are dropped, and a BBL (borough-block-lot) identifier is added. This final clean csv file is available [here](data-clean/dhcr-rgb-rent-stabilized-buildings-2017.csv)


## Setup

All the files created in this project are available in the repository, but if you want to run this yourself the easiest way to do so is using Docker. 

First you'll need to get set up with [Docker](https://www.docker.com/get-started). Once you've installed Docker you can download/clone this repository, navigate to the directory and run:

```
docker-compose build
docker-compose run app
```

This will start with the original PDF files and rebuild everything else again from scratch. 
