import selenium
from selenium import webdriver

path = "C:\Program Files\chromedriver"
driver = webdriver.Chrome(path)
url = "https://www.instagram.com/explore/tags/followyouback/"

driver.get(url)
print(driver.title)
# driver.quit()