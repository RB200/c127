from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL='https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser=webdriver.Chrome()
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers=['name','light-years from earth','planet mass','stellar magnitude','discovery date']
    planetData=[]
    for i in range(0,453):
        soup=BeautifulSoup(browser.page_source,'html.parser')
        for ultag in soup.find_all('ul',attrs={'class','exoplanet'}):
            litags=ultag.find_all('li')
            tempList=[]
            for index,litag in enumerate(litags):
                if index==0:
                    tempList.append(litag.find_all('a')[0].contents[0])
                else:
                    try:
                        tempList.append(litag.contents[0])
                    except:
                        tempList.append('')
            planetData.append(tempList)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('scraper.csv','w') as f:
        csvWriter=csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(planetData)
scrape()
