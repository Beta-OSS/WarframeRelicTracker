import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html
from openpyxl import load_workbook

def startup():
    url = "https://warframe.fandom.com/wiki/Void_Relic"
    unvaultedXPath = '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[2]'
    vaultedXPath = '//*[@id="mw-customcollapsible-VaultedRelicList"]/table/tbody/tr[2]'

    scrapeForRelics(url, unvaultedXPath, vaultedXPath)

def scrapeForRelics(url, unvaultedXPath, vaultedXPath):
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content
    tree = html.fromstring(html_content)

    # Find elements using XPath
    elements = tree.xpath(unvaultedXPath)
    print(tree)
    while True:
        i = 0
        while True:
            j = 0
            extension = '/td['+ i +']/ul/li['+ j +']'
            path = unvaultedXPath + extension
    
startup()