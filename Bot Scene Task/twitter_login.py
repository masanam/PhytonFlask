from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

class TwitterLogin():

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
        new_folder = str(new_folder)
        # directory = path + "/" + str(new_folder)
        directory = os.path.join(path, new_folder)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if new_folder_create != "":
            # directory = directory + "/" + str(new_folder_create)
            directory = os.path.join(directory, str(new_folder_create))
            if not os.path.exists(directory):
                os.makedirs(directory)
            return directory
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
            TwitterLogin.tf_check_and_rename(original_file, add)

    def tf_screen_shots(driver, scroll_delay=0.3):
        path = TwitterLogin.tf_check_folder_path("screenshot")
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
            TwitterLogin.tf_check_and_rename(file_name)
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
        path = TwitterLogin.tf_check_folder_path("sourcepage")
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

        TwitterLogin.tf_File_name = path + "/" + title + ".html"
        if os.path.exists(TwitterLogin.tf_File_name):
            TwitterLogin.tf_check_and_rename(TwitterLogin.tf_File_name)
        pagesource = driver.page_source.encode('ascii', 'ignore')
        soup = BeautifulSoup(pagesource, 'html.parser')
        # Create text file, then write page source to the file
        fh = open(TwitterLogin.tf_File_name, 'w')
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
            if total_height < 20000:
                update_total_height = Chromedriver.execute_script('return document.body.parentNode.scrollHeight')
                if total_height != update_total_height:
                    total_height = update_total_height
        Chromedriver.execute_script('window.scrollTo({0}, {1})'.format(0, 0))

    #To Url
    def tf_To_url():
        url = 'https://www.twitter.com/'
        return url

    def tf_Click_Log_in(Chromedriver):
        Log_in = Chromedriver.find_element_by_link_text('Log In')
        Log_in.click ()
        time.sleep (Wait_2)

    def tf_Type_user_input(Chromedriver):
        username = Chromedriver.find_element_by_css_selector("input[placeholder='Phone, email or username']")
        # username = Chromedriver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
        username.send_keys("johnbradman2019@gmail.com")
        time.sleep(Wait_1)

    def tf_Type_user_password(Chromedriver):
        userpass = Chromedriver.find_element_by_css_selector("input[class='js-password-field']")
        # userpass = Chromedriver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
        userpass.send_keys("Xysbsg@1238#76Bd")
        time.sleep(Wait_1)

    def tf_Type_user_submit(Chromedriver):
        usersubmit = Chromedriver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
        # usersubmit = Chromedriver.find_element_by_xpath("//button[text()='Log in']")
        usersubmit.click()
        time.sleep(Wait_2)

    def ty_Type_twitter_connection(Chromedriver):
        see_more = Chromedriver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/aside/a/div/span')
        see_more.click()
        time.sleep(Wait_2)

    def tf_Type_follow_connection(Chromedriver):
        follow = Chromedriver.find_elements_by_xpath ('//*[contains(text(), "Follow")]')
        try:
            i=0
            while True:
                follow[i].click()
                i+=1
                time.sleep(Wait_1)
                if i == 4:
                    break
        except:
            pass

    def tf_Type_publish_tweet(Chromedriver):
        tweet = Chromedriver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div')
        tweet.send_keys("""twitter is my favorite social media site.""")
        time.sleep(Wait_2)
        tweet_now = Chromedriver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        tweet_now.click()
        time.sleep(Wait_2)

    import shutil
    def save_image_to_file(image, dirname, suffix):
        with open('{dirname}/img_{suffix}.jpg'.format(dirname=dirname, suffix=suffix), 'wb') as out_file:
            shutil.copyfileobj(image.raw, out_file)

    def download_images(dirname, links):
        length = len(links)
        for index, url in enumerate(links):
            try:
                index_start = index + 1
                print('Downloading {0} of {1} images'.format(index_start, length))
                response = requests.get(url, stream=True)
                save_image_to_file(response, dirname, index_start)
                del response
            except Exception as e:
                print(e)
                pass

    def tf_Type_get_all_images(Chromedriver):
        TwitterLogin.tf_Type_driver_scroller(Chromedriver)
        TwitterLogin.tf_source_code(Chromedriver)
        soup = BeautifulSoup(Chromedriver.page_source, "html.parser")
        images = soup.find_all('img')
        images_url = []
        for image in images:
            if 'src' in str(image):
                print(image['src'])
                images_url.append(image['src'])
        twitter_image_path = TwitterLogin.tf_check_folder_path("twitter_images")
        download_images(twitter_image_path,images_url)

    def tf_Type_timeline_tweets(Chromedriver):
        timeline_elements = Chromedriver.find_elements_by_xpath("//section[contains(@class, 'css-1dbjc4n')]")
        timeline_element = None
        image_list = set()
        heading_element_list = list()
        if timeline_elements:
            timeline_element = timeline_elements[0]
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
            div_content = timeline_element.find_elements_by_tag_name("img")
            for get_img in div_content:
                try:
                    image = str(get_img.get_attribute("src"))
                    if image.startswith("https://pbs.twimg.com/media"):
                        image_list.add(image)
                except Exception as e:
                    print(e)
                    pass
            try:
                heading_span = timeline_element.find_elements_by_tag_name("span")
                for heading_element in heading_span:
                    if str(heading_element.text).strip() != "":
                        heading = str(heading_element.text)
                        if heading not in heading_element_list:
                            heading_element_list.append(heading)
            except Exception as e:
                print(e)
                pass
            if total_height < 20000:
                update_total_height = Chromedriver.execute_script('return document.body.parentNode.scrollHeight')
                if total_height != update_total_height:
                    total_height = update_total_height
        print(len(list(image_list)))
        images_url_list = list(image_list)
        twitter_image_path = TwitterLogin.tf_check_folder_path("twitter_images")
        download_images(twitter_image_path, images_url_list)
        print(len(heading_element_list))
        print(heading_element_list)
        title = Chromedriver.title
        if title != "":
            title_length = len(str(title))
            if title_length > 26:
                title = title.replace("@", "").replace("/", "").replace("$", "").replace(".", "").replace(":", "").replace(
                    "|", "")
                title = str(title)[0:25]
            else:
                title = title.replace("@", "").replace("/", "").replace("$", "").replace(".", "").replace(":",
                                                                                                        "").replace(
                    "|", "")
        else:
            title = Chromedriver.current_url
            title = title.replace("@", "").replace("/", "").replace("$", "").replace(".", "").replace(":", "").replace("|",
                                                                                                                    "")
        with open(twitter_image_path+'/'+title+''+'.txt', 'w') as f:
            for item in heading_element_list:
                f.write("%s\n" % item)


#--- YOU ONLY NEED TO CARE FROM THIS LINE ---
# creating new driver to use proxy
def twitter_login():
    ALL_PROXIES = TwitterLogin.tf_get_proxy()
    Chromedriver = TwitterLogin.tf_proxy_driver(ALL_PROXIES)
    running = True
    while running:
        try:
            Chromedriver.get(TwitterLogin.tf_To_url())
            # time.sleep(Wait_3)
            if Chromedriver != None:
                TwitterLogin.tf_Click_Log_in(Chromedriver)
                TwitterLogin.tf_Type_user_input(Chromedriver)
                TwitterLogin.tf_Type_user_password(Chromedriver)
                TwitterLogin.tf_Type_user_submit(Chromedriver)
                TwitterLogin.tf_Type_timeline_tweets(Chromedriver)
                # tf_Type_get_all_images(Chromedriver)
                # tf_Type_publish_tweet(Chromedriver)
                # ty_Type_twitter_connection(Chromedriver)
                # tf_Type_follow_connection(Chromedriver)
            running = False
        except Exception as e:
            print(e)
            new = ""
            try:
                new = ALL_PROXIES.pop()
            except Exception as e:
                ALL_PROXIES = TwitterLogin.tf_get_proxy()

            # reassign driver if fail to switch proxy
            Chromedriver = TwitterLogin.tf_proxy_driver(ALL_PROXIES)
            print("--- Switched proxy to: %s" % new)
            time.sleep(1)