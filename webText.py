from bs4 import BeautifulSoup
import requests
import re
html = requests.get("https://www.kartable.fr/ressources/geographie/cours/des-cartes-pour-comprendre-le-monde/9712").content
#1 Recoding
unicode_str = html.decode("utf8")
encoded_str = unicode_str.encode("ascii",'ignore')
news_soup = BeautifulSoup(encoded_str, "html.parser")
a_text = news_soup.find_all('p')
#2 Removing
y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
print(y)
