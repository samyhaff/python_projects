from bs4 import BeautifulSoup
import requests
import re

html = requests.get("https://www.kartable.fr/ressources/geographie/cours/des-cartes-pour-comprendre-le-monde/9712").content

unicode_str = html.decode("utf8")
encoded_str = unicode_str.encode("ascii",'ignore')
news_soup = BeautifulSoup(encoded_str, "html.parser")
a_text = news_soup.find_all('p')

y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
lines = (line.strip() for line in str(y).splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
y = '\n'.join(chunk for chunk in chunks if chunk)

#print(y)

file = open("textOutput.txt", "w")
file.write(str(y))
file.close()
