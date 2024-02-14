import os, sys, glob, re
import json
from pprint import pprint
import urllib3
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import uuid
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from config import LINK_LIST_PATH_BLOOMBERG, LINK_LIST_PATH_BIGPARA



# Encoding for writing the URLs to the .txt file
# Do not change unless you are getting a UnicodeEncodeError
ENCODING = "utf-8"


def save_link_bigpara(url, page):
    """
    Save collected link/url and page to the .txt file in LINK_LIST_PATH
    """
    id_str = uuid.uuid3(uuid.NAMESPACE_URL, url).hex
    with open(LINK_LIST_PATH_BIGPARA, "a", encoding=ENCODING) as f:
        f.write("\t".join([id_str, url, str(page)]) + "\n")


def save_link_bloomberg(url, page):
    """
    Save collected link/url and page to the .txt file in LINK_LIST_PATH
    """
    id_str = uuid.uuid3(uuid.NAMESPACE_URL, url).hex
    with open(LINK_LIST_PATH_BLOOMBERG, "a", encoding=ENCODING) as f:
        f.write("\t".join([id_str, url, str(page)]) + "\n")


def download_links_from_index_bloomberg():
    """
    This function should go to the defined "url" and download the news page links from all
    pages and save them into a .txt file.
    """

    # Checking if the link_list.txt file exists
    if not os.path.exists(LINK_LIST_PATH_BLOOMBERG):
        with open(LINK_LIST_PATH_BLOOMBERG, "w", encoding=ENCODING) as f:
            f.write("\t".join(["id", "url", "page"]) + "\n")
        start_page = 1
        downloaded_url_list = []

    # If some links have already been downloaded,
    # get the downloaded links and start page
    else:
        # Get the page to start from
        data = pd.read_csv(LINK_LIST_PATH_BLOOMBERG, sep="\t")
        if data.shape[0] == 0:
            start_page = 1
            downloaded_url_list = []
        else:
            start_page = data["page"].astype("int").max()
            downloaded_url_list = data["url"].to_list()

    # WRITE YOUR CODE HERE
    #########################################
    # Start downloading from the page "start_page"
    # which is the page you ended at the last
    # time you ran the code (if you had an error and the code stopped)

    rootURL = 'https://www.bloomberght.com/tum-piyasa-haberleri/'

    for pid in range (start_page,37):     #start page is 0

        pageURL = '{}{}'.format(rootURL, pid)
        #print(pageURL)

        resp = requests.get(pageURL)
        #print(resp.text)

        soup = bs(resp.text, "lxml")
        #print(soup)
        #for item in soup.find_all("li", {"class:", "news-item-list__items__item"}):
        for item in soup.find_all("ul"):
            #print(item)
            #print(item.find('h2').find('a')['href'])
            # Save the collected url in the variable "collected_url"
            collected_url = 'https://www.bloomberght.com/tum-piyasa-haberleri' + item.find('li').find('a')['href']

            # Save the page that the url is taken from in the variable "page"
            page = pid

            # The following code block saves the collected url and page
            # Save the collected urls one by one so that if an error occurs
            # you do not have to start all over again

            if collected_url not in downloaded_url_list:
                print("\t", collected_url, flush=True)
                save_link_bloomberg(collected_url, page)
            #########################################





def download_links_from_index_bigpara():
    """
    This function should go to the defined "url" and download the news page links from all
    pages and save them into a .txt file.
    """

    # Checking if the link_list.txt file exists
    if not os.path.exists(LINK_LIST_PATH_BIGPARA):
        with open(LINK_LIST_PATH_BIGPARA, "w", encoding=ENCODING) as f:
            f.write("\t".join(["id", "url", "page"]) + "\n")
        start_page = 1
        downloaded_url_list = []

    # If some links have already been downloaded,
    # get the downloaded links and start page
    else:
        # Get the page to start from
        data = pd.read_csv(LINK_LIST_PATH_BIGPARA, sep="\t")
        if data.shape[0] == 0:
            start_page = 1
            downloaded_url_list = []
        else:
            start_page = data["page"].astype("int").max()
            downloaded_url_list = data["url"].to_list()

    # WRITE YOUR CODE HERE
    #########################################
    # Start downloading from the page "start_page"
    # which is the page you ended at the last
    # time you ran the code (if you had an error and the code stopped)

    rootURL = 'https://bigpara.hurriyet.com.tr/borsa/haber/'

    for pid in range (start_page,41):     #start page is 0

        pageURL = '{}{}'.format(rootURL, pid)
        #print(pageURL)

        resp = requests.get(pageURL)
        #print(resp.text)

        soup = bs(resp.text, "lxml")
        #print(soup)
        #for item in soup.find_all("li", {"class:", "news-item-list__items__item"}):
        for item in soup.find_all("li", {"class:", "cell029 imgCell fsn"}):
            #print(item)
            #print(item.find('h2').find('a')['href'])
            # Save the collected url in the variable "collected_url"
            collected_url = 'https://bigpara.hurriyet.com.tr/borsa/haber/' + item.find('h2').find('a')['href']

            # Save the page that the url is taken from in the variable "page"
            page = pid

            # The following code block saves the collected url and page
            # Save the collected urls one by one so that if an error occurs
            # you do not have to start all over again

            if collected_url not in downloaded_url_list:
                print("\t", collected_url, flush=True)
                save_link_bigpara(collected_url, page)
            #########################################












if __name__ == "__main__":
    download_links_from_index_bloomberg()
    download_links_from_index_bigpara()