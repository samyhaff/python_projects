import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

url="http://www.synonymes.com/synonyme.php?mot=manger&x=0&y=0"

uClient = uReq(url)
page_html = uClient.read()
uClient.close()

page_soup = BeautifulSoup(page_html, "html.parser")
