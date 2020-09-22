from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import date
import time
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
import os
from PIL import Image
from io import BytesIO
import pafy
import random
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from selenium.webdriver import ChromeOptions, Chrome

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# wait or sleep in seconds
Wait_1 = 3
Wait_2 = 5
Wait_3 = 10
Wait_4 = 20
Wait_5 = 35

# Chrome_path = '/home/rails/python_requirement/chromedriver'
Chrome_path = r'C:\Users\arifa\Documents\chromedriver.exe' 
Edge_path = ''
Opera_path = ''
Firefox_path = ''

# Username & password
Task_value_group_3 = ['']
# Search query
Task_value_group_4 = ['Python', 'Python programmer']
# Skype message
Task_value_group_5 = ['Hi are you a programmer?', 'two']

# The task value group index should be the sequence number (SN) of the selected row.
# Each task function has its own index depending on whether its SN is unique or non-unique
tvg_index_1 = 0

class YoutubeLogin():

    def tf_get_proxy():
        # proxies = set()
        proxy_list = list()
        try:
            url = "https://free-proxy-list.net/"
            adapter = HTTPAdapter(max_retries=2)

            request_session = requests.Session()
            request_session.mount(url, adapter)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            r = requests.get(url, headers=headers, verify=False, timeout=5)
            soup = BeautifulSoup(r.content, 'html.parser')
            proxy_data = soup.select('td:nth-child(2) , td:nth-child(1)')
            for i in range(0, 20, 2):
                proxy_list.append(str(proxy_data[i].text) + ':' + str(proxy_data[i + 1].text))
            # proxy = str(proxy_data[i].text) + ':' + str(proxy_data[i + 1].text)
            # proxies.add(proxy)
            return proxy_list
        except Exception as e:
            print(" --->", e)
            pass


    ALL_PROXIES = tf_get_proxy()

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--window-position=0,0')
    options.add_argument('--disable-infobars')
    options.add_argument('--window-size=1920,1080')

    def tf_proxy_driver(PROXIES, options=options):
        pxy = ''
        # if PROXIES:
        #     pxy = PROXIES[-1]
        # else:
        #     print("--- Proxies used up (%s)" % len(PROXIES))
        #
        # options.add_argument('--proxy-server=%s' % pxy)

        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        # driver = Chrome(chrome_options=opts)

        Chromedriver = webdriver.Chrome(Chrome_path, chrome_options=opts)        
        Chromedriver.implicitly_wait(Wait_3)
        print("proxy is - ", pxy)
        return Chromedriver


    def tf_use_same_session(ChromeDriver):
        executor_url = ChromeDriver.command_executor._url  # "http://127.0.0.1:60622/hub"
        session_id = ChromeDriver.session_id  # '4e167f26-dc1d-4f51-a207-f761eaf73c31'
        print(session_id)
        driver_temp = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        driver_temp.close()
        driver_temp.session_id = session_id
        return driver_temp

    def tf_check_folder_path(new_folder_create=""):
        path = os.path.dirname(os.getcwd())
        path = path + "/" + "source_page_screen_shot_media"
        new_folder = date.today()
        directory = path + "/" + str(new_folder)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if new_folder_create != "":
            directory = directory + "/" + str(new_folder_create)
            if not os.path.exists(directory):
                os.makedirs(directory)
                return directory
            else:
                return directory

    def tf_check_and_rename(file, add=0):
        original_file = file
        if add != 0:
            split = file.split(".")
            part_1 = split[0] + "_" + str(add)
            file = ".".join([part_1, split[1]])
        if not os.path.isfile(file):
            os.rename(original_file, file)
        else:
            add += 1
            YoutubeLogin.tf_check_and_rename(original_file, add)

    def tf_screen_shots(driver, scroll_delay=0.3):
        path = YoutubeLogin.tf_check_folder_path("screenshot")
        title = driver.title
        if title != "":
            title_length = len(str(title))
            if title_length > 26:
                title = title.replace("@", "").replace("/", "").replace("$", "").replace(".", "").replace(":",
                                                                                                        "").replace(
                    "|", "")
                title = str(title)[0:25]
        else:
            title = driver.current_url
            title = title.replace("@","").replace("/","").replace("$","").replace(".","").replace(":","").replace("|","")

        file_name = path +"/"+ title + ".png"
        if os.path.exists(file_name):
            YoutubeLogin.tf_check_and_rename(file_name)
        device_pixel_ratio = driver.execute_script('return window.devicePixelRatio')
        total_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        viewport_height = driver.execute_script('return window.innerHeight')
        total_width = driver.execute_script('return document.body.offsetWidth')
        viewport_width = driver.execute_script("return document.body.clientWidth")

        # this implementation assume (viewport_width == total_width)
        assert (viewport_width == total_width)

        # scroll the page, take screenshots and save screenshots to slices
        offset = 0  # height
        slices = {}

        while offset < total_height:
            if offset + viewport_height > total_height:
                offset = total_height - viewport_height

            driver.execute_script('window.scrollTo({0}, {1})'.format(0, offset))
            time.sleep(scroll_delay)

            img = Image.open(BytesIO(driver.get_screenshot_as_png()))
            slices[offset] = img

            offset = offset + viewport_height
            if total_height < 10000:
                update_total_height = driver.execute_script('return document.body.parentNode.scrollHeight')
                if total_height != update_total_height:
                    total_height = update_total_height
        # combine image slices
        stitched_image = Image.new('RGB', (total_width * device_pixel_ratio, total_height * device_pixel_ratio))
        for offset, image in slices.items():
            stitched_image.paste(image, (0, offset * device_pixel_ratio))
        stitched_image.save(file_name)
        driver.execute_script('window.scrollTo({0}, {1})'.format(0, 0))

    def tf_source_code(driver):
        path = YoutubeLogin.tf_check_folder_path("sourcepage")
        title = driver.title
        if title != "":
            title_length = len(str(title))
            if title_length > 26:
                title = title.replace("@", "").replace("/", "").replace("$", "").replace(".", "").replace(":","").replace("|", "")
                title = str(title)[0:25]
            else:
                title = title.replace("@", "").replace("/", "").replace("$", "").replace(".", "").replace(":",
                                                                                                        "").replace(
                    "|", "")
        else:
            title = driver.current_url
            title = title.replace("@","").replace("/","").replace("$","").replace(".","").replace(":","").replace("|","")

        YoutubeLogin.tf_File_name = path + "/" + title + ".html"
        if os.path.exists(YoutubeLogin.tf_File_name):
            YoutubeLogin.tf_check_and_rename(YoutubeLogin.tf_File_name)
        pagesource = driver.page_source.encode('ascii', 'ignore')
        soup = BeautifulSoup(pagesource, 'html.parser')
        # Create text file, then write page source to the file
        fh = open(YoutubeLogin.tf_File_name, 'w')
        fh.write(str(soup.prettify()))
        fh.close()

    def tf_Type_driver_scroller(Chromedriver):
        total_height = Chromedriver.execute_script('return document.body.parentNode.scrollHeight')
        viewport_height = Chromedriver.execute_script('return window.innerHeight')
        total_width = Chromedriver.execute_script('return document.body.offsetWidth')
        viewport_width = Chromedriver.execute_script("return document.body.clientWidth")

        # this implementation assume (viewport_width == total_width)
        assert (viewport_width == total_width)

        # scroll the page, take screenshots and save screenshots to slices
        offset = 0  # height
        while offset < total_height:
            if offset + viewport_height > total_height:
                offset = total_height - viewport_height

            Chromedriver.execute_script('window.scrollTo({0}, {1})'.format(0, offset))
            time.sleep(Wait_1)

            offset = offset + viewport_height
            if total_height < 10000:
                update_total_height = Chromedriver.execute_script('return document.body.parentNode.scrollHeight')
                if total_height != update_total_height:
                    total_height = update_total_height
        Chromedriver.execute_script('window.scrollTo({0}, {1})'.format(0, 0))

    #To Url
    def tf_To_url():
        url = 'https://www.youtube.com/?gl=IN'
        return url

    def tf_Click_Sign_in(Chromedriver):
        try:
            Sign_in = Chromedriver.find_element_by_link_text('SIGN IN')
            Sign_in.click ()
            time.sleep (Wait_2)
        except:
            pass

    def tf_Type_already_login(Chromedriver):
        try:
            youtube_user = Chromedriver.find_element_by_xpath("//div[@role = 'link']")
            youtube_user.click()
            time.sleep(Wait_2)
        except:
            pass

    def tf_Type_login(Chromedriver):
        try:
            youtube_user_for_login = Chromedriver.find_element_by_name("identifier")
            youtube_user_for_login.clear()
            youtube_user_for_login.send_keys("johnbradman2019@gmail.com")
            time.sleep(Wait_2)
        except:
            pass

    def tf_Type_next1(Chromedriver):
        try:
            ytube_next1 = Chromedriver.find_element_by_xpath('//*[@id="identifierNext"]')
            ytube_next1.click()
            time.sleep(Wait_2)
        except:
            pass

    def tf_Type_password(Chromedriver):
        try:
            youtube_user_password = Chromedriver.find_element_by_name("password")
            youtube_user_password.clear()
            youtube_user_password.send_keys("John2019#")
            time.sleep(Wait_2)
        except:
            pass

    def ty_Type_next2(Chromedriver):
        try:
            ytube_next2 = Chromedriver.find_element_by_xpath('//*[@id="passwordNext"]')
            ytube_next2.click()
            time.sleep(Wait_2)
        except:
            pass

    def tf_Type_get_youtube_url(Chromedriver):
        url_data_type1 = Chromedriver.find_elements_by_xpath('//*[@id="video-title-link"]')
        links = []
        for url_href in url_data_type1:
            links.append(url_href.get_attribute('href'))
        if len(links) == 0:
            url_data_type2 = Chromedriver.find_elements_by_xpath('//*[@id="video-title"]')
            for url_href in url_data_type2:
                links.append(url_href.get_attribute('href'))
        print(links)
        return links

    def tf_Type_get_youtube_video(video_url_list):
        secure_random = random.SystemRandom()
        url = secure_random.choice(video_url_list)
        video = pafy.new(url)
        streams = video.streams
        for s in streams:
            print(s)
        # get best resolution regardless of format
        best = video.getbest(preftype="webm")
        print(best.resolution, best.extension)
        # Download the video
        path = YoutubeLogin.tf_check_folder_path("youtube-video")
        best.download(quiet=False,filepath=path)

    def tf_Type_comment_youtube_video(Chromedriver):
        comment_boxt = Chromedriver.find_element_by_xpath('//*[@id="contenteditable-root"]')
        comment_boxt.send_keys("Good video")
        time.sleep(Wait_1)
        post_comment = Chromedriver.find_element_by_xpath('//*[@id="submit-button"]/a')
        post_comment.click()
        time.sleep(Wait_2)



        #--- YOU ONLY NEED TO CARE FROM THIS LINE ---
# creating new driver to use proxy
def youtube_login():
    ALL_PROXIES = YoutubeLogin.tf_get_proxy()
    Chromedriver = YoutubeLogin.tf_proxy_driver(ALL_PROXIES)
    running = True
    while running:
        try:
            Chromedriver.get(YoutubeLogin.tf_To_url())
            time.sleep(Wait_2)
            if Chromedriver != None:
                YoutubeLogin.tf_Click_Sign_in(Chromedriver)
                YoutubeLogin.tf_Type_login(Chromedriver)
                YoutubeLogin.tf_Type_next1(Chromedriver)
                YoutubeLogin.tf_Type_password(Chromedriver)
                YoutubeLogin.ty_Type_next2(Chromedriver)
                # tf_Type_comment_youtube_video(Chromedriver)
                # links = tf_Type_get_youtube_url(Chromedriver)
                # tf_Type_get_youtube_video(links)
                running = False

        except Exception as e:
            print(e)
            new = ""
            try:
                new = ALL_PROXIES.pop()
            except Exception as e:
                ALL_PROXIES = YoutubeLogin.tf_get_proxy()

            # reassign driver if fail to switch proxy
            Chromedriver = YoutubeLogin.tf_proxy_driver(ALL_PROXIES)
            print("--- Switched proxy to: %s" % new)
            time.sleep(1)