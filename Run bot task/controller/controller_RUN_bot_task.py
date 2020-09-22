#Bot task, task functions, and task value groups
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys 
import time, os, fnmatch, shutil 
from datetime import datetime, timezone, timedelta 
import re 
from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen
import threading

#import C:\Users\Shane Fang\Desktop\Automation Systems 2020\Auto Sys - Simplified\Skype web\UI_elements.py
#wait or sleep in seconds 
Wait_1 = 3 
Wait_2 = 5 
Wait_3 = 10 
Wait_4 = 20 
Wait_5 = 35

#Webdriver file path 
Chrome_path = r'C:\Users\arifa\Documents\chromedriver.exe' 
Edge_path = '' 
Opera_path = ''  
Firefox_path = ''

#Use different web drivers 
Chromedriver = webdriver.Chrome(Chrome_path) 
Edgedriver = '' 
Operadriver = '' 
Firefoxdriver = ''

# def get_content_len(url):
#     response = urlopen(Request(url))
#     content = response.read()
#     print(len(content))

# urls = [
#     "http://www.codepolitan.com", 
#     "http://www.codepolitan.com/articles",
#     "http://www.codepolitan.com/upcoming-event",
#     "http://www.codepolitan.com/course",
#     "http://www.codepolitan.com/statistics"
# ]

urls = ['https://duckduckgo.com/', 'https://google.com/search?q=','https://bing.com/search?q='] 
keys = ['User', 'Administrator', 'Member'] 

for url in urls:
    for key in keys:
        keyword = url+key
        Chromedriver.execute_script('window.open("%s")' % keyword)