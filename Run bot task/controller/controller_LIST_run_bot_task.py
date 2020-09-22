from flask import request
from flask import render_template
from main import getPath

import sys
#Bot task, task functions, and task value groups
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys 
import time, os, fnmatch, shutil 
from datetime import datetime, timezone, timedelta, date 
import re 
from bs4 import BeautifulSoup 

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from requests.adapters import HTTPAdapter
import os
from PIL import Image
from io import BytesIO
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import multiprocessing
import threading
import concurrent.futures
# sys.path.insert(1, getPath()+'/Run bot task/model/')
sys.path.insert(1, getPath()+'Run bot task/model/')
from model_LIST_run_bot_task import DataList

sys.path.insert(1, getPath()+'/Bot Scene Task/') 
from facebook_login import facebook_login
from facebook_reg import facebook_reg
from instagram_reg import instagram_reg
from instagram_login import instagram_login
from telegram_reg import telegram_reg
from telegram_login import telegram_login
from tumblr_login import tumblr_login
from tumblr_reg import tumblr_reg
from linkedin_login import linkedin_login
from linkedin_reg import linkedin_reg
from pinterest_login import pinterest_login
from pinterest_reg import pinterest_reg
from skype_login import skype_login
from skype_reg import skype_reg
from twitter_login import twitter_login
from twitter_reg import twitter_reg
from youtube_login import youtube_login
from youtube_reg import youtube_reg
from duckduckgo_images import duckduckgo_images

class ListController():
    def list_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        text= request.form.get('search')
        from_sn= request.form.get('from_sn')
        to_sn= request.form.get('to_sn')


        if request.form.get('search'):            
            result = DataList.search_data(text)
        elif request.form.get('from_sn'):            
            result = DataList.search_data1(from_sn,to_sn)     
        else:
            result = DataList.get_data(start,limit)
        
        count = DataList.count_data()
        return render_template('tmpl_LIST_run_bot_task.html', title='List Run bot task',listdata=result, countdata=count)

    def run_run_controller():
                #Task value groups - The task values in the task value groups will change according to the selected value groups 
        urls = ['https://duckduckgo.com/', 'https://google.com/search?q=','https://bing.com/search?q=','https://yahoo.com/search?q='] 
        keys = ['User', 'Administrator', 'Member'] 

        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        text= request.form.get('search')
        from_sn= request.form.get('from_sn')
        to_sn= request.form.get('to_sn')

        if request.form.get('search'):            
            result = DataList.search_data(text)
        elif request.form.get('from_sn'):            
            result = DataList.search_data1(from_sn,to_sn)      
        elif request.form.getlist('checkbox'):
            checkId = request.form.getlist('checkbox')
            logstart = datetime.now()
            
        for x in checkId:
            key = DataList.get_bottask(x)

            proc = []
            for x in checkId:
                key = DataList.get_bottask(x)
                template = DataList.get_bottasktemplate(x)   
                if (template[0].lower() == 'facebook'):  
                        url = 'https://www.facebook.com/'  
                        keyword = url
                        if key[0].lower() == 'login':
                                #save the function class into variable
                                p = threading.Thread(target=facebook_login)
                                proc.append(p)
                        elif key[0].lower() == 'register':
                                #save the function class into variable
                                p = threading.Thread(target=facebook_reg)
                                proc.append(p)
                        run_count = DataList.get_run_count(x)
                elif (template[0].lower() == 'instagram'):  
                        url = 'https://www.instagram.com/'
                        keyword = url
                        if key[0].lower() == 'login':
                                #save the function class into variable
                                p = threading.Thread(target=instagram_login)
                                proc.append(p)
                        elif key[0].lower() == 'register':
                                #save the function class into variable
                                p = threading.Thread(target=instagram_reg)
                                proc.append(p)
                        run_count = DataList.get_run_count(x)
                elif (template[0].lower() == 'linkedin'):  
                        url = 'https://www.linkedin.com/'
                        keyword = url
                        if key[0].lower() == 'login':
                                #save the function class into variable
                                p = threading.Thread(target=linkedin_login)
                                proc.append(p)
                        elif key[0].lower() == 'register':
                                #save the function class into variable
                                p = threading.Thread(target=linkedin_reg)
                                proc.append(p)
                        run_count = DataList.get_run_count(x)
                elif (template[0].lower() == 'pinterest'):  
                        url = 'https://in.pinterest.com/'
                        keyword = url+key[0]
                        if key[0].lower() == 'login':
                                #save the function class into variable
                                p = threading.Thread(target=pinterest_login)
                                proc.append(p)
                        elif key[0].lower() == 'register':
                                #save the function class into variable
                                p = threading.Thread(target=pinterest_reg)
                                proc.append(p)
                        run_count = DataList.get_run_count(x)
                elif (template[0].lower() == 'skype'):  
                        url = "https://www.skype.com/en/"
                        keyword = url+key[0]
                        if key[0].lower() == 'login':
                                #save the function class into variable
                                p = threading.Thread(target=skype_login)
                                proc.append(p)
                        elif key[0].lower() == 'register':
                                #save the function class into variable
                                p = threading.Thread(target=skype_reg)
                                proc.append(p)             
                        run_count = DataList.get_run_count(x)
                elif (template[0].lower() == 'telegram'):  
                        url = 'https://web.telegram.org/#/login'
                        keyword = url+key[0]
                        if key[0].lower() == 'login':
                                #save the function class into variable
                                p = threading.Thread(target=telegram_login)
                                proc.append(p)
                        elif key[0].lower() == 'register':
                                #save the function class into variable
                                p = threading.Thread(target=telegram_reg)
                                proc.append(p)                  
                        run_count = DataList.get_run_count(x)
                elif (template[0].lower() == 'tumblr'):  
                        url = "https://mx.tumblr.com/wf/click?upn=rkn-2Bn4Ut-2BmJG-2BjXrxx-2FWfRVhSEJrCqHkmNvVCtVtMZo0UQxEmMaTYPnvUY6PtumNSRgZkNQISylJymCM7Yd4q5yUTxWtvhlqd3G7-2BeXTk7nW-2F-2Fno7iPkNEmptOZKLOKoucBa9Zcnfo7MhQCPp3UIWwRQuA35VUvTmI49YHlrb9yp-2BD0S4NYsJZUFAyka4hWM_dLZYRNjweXQmVRj4LdlmKcPVpMU7tUXwUN-2FXAxlbQ2oiQflisjxPZahhHK4F72aSxg78uapKGa-2BWQCnDiMWbYVTML60c6n9vr3zROUluHFMs4B0D6Tp1qw-2BVm2E7zU14cpAKuvql-2BkVnfDxMtArs3z5dRsKP8vtRznGZplQVA6Xf9ejVk6-2FGt2aNWZLWks8QWWJT7WAS371uvlHYrWIBmkSE525D20pFw9T6ITGcHvRXM4q-2F7bcQ7pyhRveTq9QiXjvekikMd8-2BaKMwq52yjA1eD5XKrYtxDU-2FDtXsXmm3MTxNouCH1ZTYCwMaUmgDky"
                        keyword = url+key[0]
                        if key[0].lower() == 'login':
                                #save the function class into variable
                                p = threading.Thread(target=tumblr_login)
                                proc.append(p)
                        elif key[0].lower() == 'register':
                                #save the function class into variable
                                p = threading.Thread(target=tumblr_reg)
                                proc.append(p)                  
                        run_count = DataList.get_run_count(x)
                elif (template[0].lower() == 'twitter'):  
                        url = 'https://www.twitter.com/'
                        keyword = url+key[0]
                        if key[0].lower() == 'login':
                                #save the function class into variable
                                p = threading.Thread(target=twitter_login)
                                proc.append(p)
                        elif key[0].lower() == 'register':
                                #save the function class into variable
                                p = threading.Thread(target=twitter_reg)
                                proc.append(p)                             
                        run_count = DataList.get_run_count(x)
                elif (template[0].lower() == 'youtube'):   
                        url = 'https://www.youtube.com/?gl=IN'
                        keyword = url
                        if key[0].lower() == 'login':
                                #save the function class into variable
                                p = threading.Thread(target=youtube_login)
                                proc.append(p)
                        elif key[0].lower() == 'register':
                                #save the function class into variable
                                p = threading.Thread(target=youtube_reg)
                                proc.append(p)                   
                        run_count = DataList.get_run_count(x)
                elif (template[0].lower() == 'duckduckgo'):   
                        url = 'https://duckduckgo.com/?ia=web&q='
                        keyword = url
                        p = threading.Thread(target=duckduckgo_images, args=(key[0],))
                        proc.append(p)
                        run_count = DataList.get_run_count(x)        
                else:
                        Chrome_path = r'C:\Users\arifa\Documents\chromedriver.exe' 
                        Chromedriver = webdriver.Chrome(Chrome_path) 
                        url = 'https://google.com/search?q='
                        keyword = url+key[0]
                        Chromedriver.execute_script('window.open("%s")' % keyword)
                        run_count = DataList.get_run_count(x)

        #     to execute the process file outside the loop.
            if proc:
                for p in proc:
                    p.start()
                for p in proc:
                    p.join()

            for row in run_count:
                run_count_plus = row[0]+1
                DataList.update_data(run_count_plus,x)
                DataList.update_log('Run bot task - '+x,x,logstart)
            result = DataList.get_data(start,limit)

        else:            
            result = DataList.get_data(start,limit)

        count = DataList.count_data()
        return render_template('tmpl_LIST_run_bot_task.html', title='List Run bot task',listdata=result, countdata=count)