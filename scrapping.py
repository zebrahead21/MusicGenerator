import os
import sys
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver

genres = ["black", "death", "doom", "electronic",
          "avantgarde", "folk", "gothic", "grindcore",
          "groove", "heavy", "metalcore", "power",
          "progressive", "speed", "symphonic", "thrash"]

def init():
    chromedriver = "./chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    if sys.argv[1] in genres:
        if sys.argv[1] == "symphonic":
            url = "https://www.metal-archives.com/lists/orchestral"
        elif sys.argv[1] == "progressive":
            url = "https://www.metal-archives.com/lists/prog"
        elif sys.argv[1] == "grindcore":
            url = "https://www.metal-archives.com/lists/grind"
        else:
            url = "https://www.metal-archives.com/lists/" + sys.argv[1]
        driver.get(url)
        return driver
    return -1

def colect_data(driver):
    condition = True
    groups = []
    while condition:
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        links = soup.findAll("td", {"class": "sorting_1"})
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
    if driver == -1:
        print("No genre found")
    else:
        link = colect_data(driver)
        result = random.choice(link)
        print(result)
        driver.get(result)

