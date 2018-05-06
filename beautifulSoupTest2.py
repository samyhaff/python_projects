from bs4 import BeautifulSoup
import requests
import re
 
url = "https://www.kartable.fr"
 
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'lxml')
tags = soup.find_all('p')
text = [re.sub(r'<.+?>',r'',str(a)) for a in tags]

print(text)
