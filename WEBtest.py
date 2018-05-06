from bs4 import BeautifulSoup
import requests
import re
import codecs
import selenium.webdriver as webdriver

recherche = input("Votre recherche: ")

def get_results(search, nb = 1):
    global results
    url = "https://www.startpage.com"
    browser = webdriver.Chrome(executable_path="/Applications/chromedriver")
    browser.get(url)
    search_box = browser.find_element_by_id("query")
    search_box.send_keys(search)
    search_box.submit()
    try:
        links = browser.find_elements_by_xpath("//ol[@class='web_regular_results']//h3/a")
    except:
        links = browser.find_elements_by_xpath("//h3/a")
    results = []
    for link in links[:nb]:
        href = link.get_attribute("href")
        print(href)
        results.append(href)
    browser.close()
    return results

get_results(recherche)

html = requests.get(str(results[0])).content
encoded_str = html.decode('utf8')
news_soup = BeautifulSoup(encoded_str, "html.parser")
a_text = news_soup.find_all('p')
text = [re.sub(r'<.+?>',r'',str(a)) for a in a_text]
text = str(text)

file = codecs.open("textOutput.txt", "wb", encoding='utf-8')
file.write(text)
file.close()


