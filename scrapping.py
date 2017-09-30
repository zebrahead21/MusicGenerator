import os
import sys
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver


def init():
	chromedriver = "./chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)
	url = "https://www.metal-archives.com/lists/" + sys.argv[1]
	print(url)
	driver.get(url)
	return driver


def colect_data(driver):
	condition = True
	groups = []
	while condition:
		time.sleep(2)
		html = driver.page_source  
		soup = BeautifulSoup(html, "lxml")
		links = soup.findAll("td", { "class" : "sorting_1" })
		for tag in links:
			groups.append(str(tag.a).split('"')[1])
		next_button = driver.find_element_by_xpath('//*[@id="bandListGenre_wrapper"]/div[8]/a[3]')
		is_over = driver.find_element_by_xpath('//*[@id="bandListGenre_wrapper"]/div[7]')
		check_final = is_over.text
		list_aux = check_final.split(' ')
		if list_aux[3] == list_aux[5]:
			condition = False
		next_button.click()

	return groups


if __name__ == "__main__":
	driver = init()
	gr = colect_data(driver)
	print(random.choice(gr))
	driver.quit()
 





















