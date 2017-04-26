import requests
from bs4 import BeautifulSoup as bs
import time, timeit
import re

keywords = ["jordan",'prem']

size = '8'
session = requests.session()
site = "https://shop.exclucitylife.com"
url = "https://shop.exclucitylife.com/sitemap_products_1.xml"

# output = atc URL


def link_finder():

    response = session.get(url)
    soup = bs(response.content, 'html.parser')

    all_found_urls = []
    for urls_found in soup.find_all("url"):
        for keyword_search in urls_found.find_all("image:image"):
            if all(i in keyword_search.find("image:title").text.lower() for i in keywords):
                found_url = "Found URL: " + urls_found.find("loc").text
                all_found_urls.append(urls_found.find("loc").text + ".xml")
                print(found_url)

    for found_products in all_found_urls:
            response = session.get(found_products)
            soup = bs(response.content, 'html.parser')
            product_name = soup.find('hash').find('title').text
            product_tags = soup.find('tags').text
            print('-'*80, '\nProduct name: {}. Tags: {}\n'.format(product_name, product_tags), '-'*80)

            for variants in soup.find_all('variant'):
                print(variants.find('title').text)

                if size in variants.find('title').text and '.5' not in variants.find('title').text:

                    size_id = variants.find('id', {'type': 'integer'}).text
                    atc_link = "{}/cart/{}:1".format(site, size_id)
                    print(atc_link)
                    return atc_link



def sitekey_search(atc_link):

    sess = requests.Session()
    response = sess.get(atc_link, allow_redirects=True)
    soup = bs(response.content, 'lxml')
    sitekey = soup.select("div script")[0]
    b = sitekey.text
    print(re.findall(r'"([^"]*)"', b)[0])






