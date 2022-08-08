#! /usr/bin/env python
"""
Quick and dirty script to convert a csv download from EuroepMC to a yml file
that then can be used to generate the publication list in the webpage.

Images anf full text links should be added manually thereafter as this info
is not in the csv file that can be downloaded from europePMC

Melchor Sanchez-Martinez, 2021
"""

import os
import argparse
import pandas as pd

#Defining the argments
parser = argparse.ArgumentParser(description="Help file")
parser.add_argument("--csv_file", "-fd", \
    help="CSV file downloaded from EuropePMC)")
args = parser.parse_args()

pubyml_template="""
- title: "{}"
  citation: "{}"
  image: "/static/img/pub/xxx.png"
  date: "{}"
  journal: "{}"
  doi: "{}"
  volume: "{}"
  issue: "{}"
  pages: "{}"
  year: "{}"
  pmid: "{}"
  pmcid: "{}"
  pdf: "https://www.aging-us.com/article/202154/pdf"

"""

pubdata=pd.read_csv('/home/melchor/science/papers/europepmc-list.csv', \
delimiter=',')
with open ('publications.yml', 'a') as fa:
    for i in range(len(pubdata)):
        pubyml=pubyml_template.format(pubdata['TITLE'][i], pubdata['AUTHORS'][i]\
        +'. *'+pubdata['JOURNAL'][i]+'* ,'+pubdata['FIRST_PUB_DATE (dd/mm/yyyy)'][i]\
        .split('-')[0], pubdata['FIRST_PUB_DATE (dd/mm/yyyy)'][i], \
        pubdata['JOURNAL'][i], pubdata['DOI'][i], pubdata['VOLUME'][i], \
        pubdata['ISSUE'][i], pubdata['PAGE_INFO'][i], \
        pubdata['FIRST_PUB_DATE (dd/mm/yyyy)'][i].split('-')[0], \
        pubdata['EXTERNAL_ID'][i], \
        pubdata['PMCID'][i])
        fa.write(pubyml+os.linesep)
