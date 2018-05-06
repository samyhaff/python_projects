import bs4
from urlib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup

url=""

uClient = uReq(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
