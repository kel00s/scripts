#!/usr/bin/env python3

import argparse, pdfkit, re
from requests_html import HTMLSession

parser = argparse.ArgumentParser(description='Program for scraping SRE books to PDFs\n Example: \n ./main.py -u https://sre.google/sre-book/table-of-contents/')
parser.add_argument('--url','-u',help='Provide url to page to scape',nargs=1)

args = parser.parse_args()
session = HTMLSession()

try:
    r = session.get(args.url[0])
except requests.exceptions.RequestException as e:  # This is the correct syntax
    raise SystemExit(e)

page_links = r.html.absolute_links

for link in page_links:
    page = session.get(link)
    chapter_title = page.html.find('.chapter-title',first=True)
    try:
        pdf_filename = chapter_title.text + '.pdf' 
    except:
        pass
    
    pdfkit.from_url( link, 'pdf/' + pdf_filename )

