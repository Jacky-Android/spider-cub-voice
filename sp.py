from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
import time
import requests
from tqdm import tqdm
import os 
import wget

def pachong(name):
    driver = webdriver.Edge()
    driver.get('https://xeno-canto.org/explore?query='+name )
    try:
        nums = driver.find_element(By.XPATH,'/html/body/div[1]/nav[1]')
        num_ = nums.find_elements(By.XPATH,'ul/li')
        numss = int(num_[-2].text)
        for j in range(1,numss+1):
            num = driver.find_element(By.XPATH,'/html/body/div[1]/table/tbody').find_elements(By.XPATH,'tr')
            for i in num:
                url = (i.find_element(By.XPATH,'td[12]/a[1]').get_attribute('href'))
                
                try:
                    wget.download(url,name+'/')
                except:
                    continue
            
            driver.find_element(By.XPATH,'/html/body/div[1]/nav[1]').find_elements(By.XPATH,'ul/li')[-1].click()
            #time.sleep(10)
            
    except:
        num = driver.find_element(By.XPATH,'/html/body/div[1]/table/tbody').find_elements(By.XPATH,'tr')
        for i in num:
            url = (i.find_element(By.XPATH,'td[12]/a[1]').get_attribute('href'))
            try:
                wget.download(url,name+'/')
            except:
                continue
    driver.close()  

f=open('class.txt')

data = f.readlines()  
f.close()  # 关
for i in tqdm(range(len(data))):
    os.makedirs(data[i].replace('\n','').split(' ')[-1].split('.')[-1]) 
    
    pachong(data[i].replace('\n','').split(' ')[-1].split('.')[-1])
    time.sleep(10+i)
    

