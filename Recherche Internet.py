import selenium.webdriver as webdriver

def get_results(search, nb=1):
    url = "https://www.startpage.com"
    browser = webdriver.Chrome(executable_path="/Applications/chromedriver")
    browser.get(url)
    search_box=browser.find_element_by_id("query")
    search_box.send_keys(search)
    search_box.submit()
    try:
        links = browser.find_elements_by_xpath("//ol[@class='web_regular_results']//h3//a")
    except:
        links = browser.find_elements_by_xpath("//h3//a")
    results = []
    for link in links:
        href = link.get_attribute("href")
        print(href)
        results.append(href)
    browser.close()
    return results

get_results("dog")
