import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html
from openpyxl import load_workbook

class Relic:
    def __init__(self, name, vaulted, b1, b2, b3, s1, s2, g1):
        self.name = name
        self.vaulted = vaulted
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.s1 = s1
        self.s2 = s2
        self.g1 = g1

def startup():
    url = "https://warframe.fandom.com/wiki/Void_Relic"
    unvaultedXPath = '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[2]'
    vaultedXPath = '//*[@id="mw-customcollapsible-VaultedRelicList"]/table/tbody/tr[2]'

    scrapeForRelics(url, unvaultedXPath, vaultedXPath)

def fetch_and_parse(url, xpath_expression):
    # Fetch the HTML content
    response = requests.get(url)
    html_content = response.content
    
    # Parse the HTML content
    tree = html.fromstring(html_content)
    
    # Find elements using XPath
    elements = tree.xpath(xpath_expression)
    
    return [element.text_content() for element in elements]

def scrapeForRelics(url, unvaultedXPath, vaultedXPath):
    relics = {}
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content
    tree = html.fromstring(html_content)

    # Find elements using XPath
    elements = tree.xpath(unvaultedXPath)
    
    extension = '/td/ul/li/span/a/span'
    path = unvaultedXPath + extension
    unvaultedTexts = fetch_and_parse(url, unvaultedXPath)
    vaultedTexts = fetch_and_parse(url, vaultedXPath)
    for text in unvaultedTexts:
        #replace \xao (space) character with space
        text = text.replace(u'\xa0', u' ')
        #split to list when new line
        text = text.splitlines()
        #remove empty list elements
        text = list(filter(None, text))
        for relic in text:
            relics[relic] = False
        
       
    for text in vaultedTexts:
        #replace \xao (space) character with space
        text = text.replace(u'\xa0', u' ')
        #split to list when new line
        text = text.splitlines()
        #remove empty list elements
        text = list(filter(None, text))
        for relic in text:
            relics[relic] = True
    print(relics)
    
startup()