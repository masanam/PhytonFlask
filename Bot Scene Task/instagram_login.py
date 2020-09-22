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

class InstagramLogin():
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
            InstagramLogin.tf_check_and_rename(original_file, add)

    def tf_screen_shots(driver, scroll_delay=0.3):
        path = InstagramLogin.tf_check_folder_path("screenshot")
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
            InstagramLogin.tf_check_and_rename(file_name)
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
        path = InstagramLogin.tf_check_folder_path("sourcepage")
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

        tf_File_name = path + "/" + title + ".html"
        if os.path.exists(InstagramLogin.tf_File_name):
            InstagramLogin.tf_check_and_rename(InstagramLogin.tf_File_name)
        pagesource = driver.page_source.encode('ascii', 'ignore')
        soup = BeautifulSoup(pagesource, 'html.parser')
        # Create text file, then write page source to the file
        fh = open(InstagramLogin.tf_File_name, 'w')
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
        url = 'https://www.instagram.com/'
        return url


    #Find UI item - Find UI element and click must be put inside the same function
    #Use a separate function to store find UI element might not work in some situations.
    #Click my account
    def tf_Type_Email_or_Phone(Chromedriver):
        try:
            email_or_phone = Chromedriver.find_element_by_name('emailOrPhone')
            email_or_phone.clear()
            email_or_phone.send_keys("johnbradman2019@gmail.com")
            time.sleep (Wait_1)
        except:
            pass

    def tf_Type_Full_name(Chromedriver):
        try:
            full_name = Chromedriver.find_element_by_name('fullName')
            full_name.clear()
            full_name.send_keys("john bradman")
            time.sleep(Wait_1)
        except:
            pass

    def tf_Type_User_name(Chromedriver):
        try:
            user_name = Chromedriver.find_element_by_name('username')
            user_name.clear()
            user_name.send_keys("johnbradman2019")
            time.sleep(Wait_1)
        except:
            pass

    def tf_Type_Password(Chromedriver):
        try:
            password = Chromedriver.find_element_by_name('password')
            password.clear()
            password.send_keys("Xysbsg@1238#76Bd")
            time.sleep(Wait_1)
        except:
            pass

    def tf_Type_do_signup(Chromedriver):
        try:
            do_signup = Chromedriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button')
            do_signup.click()
            time.sleep(Wait_4)
        except:
            pass

    def tf_Type_notification(Chromedriver):
        try:
            try_notification = Chromedriver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
            try_notification.click()
            time.sleep(Wait_1)
        except:
            pass


#--- YOU ONLY NEED TO CARE FROM THIS LINE ---
# creating new driver to use proxy
def instagram_login():
    ALL_PROXIES = InstagramLogin.tf_get_proxy()
    Chromedriver = InstagramLogin.tf_proxy_driver(ALL_PROXIES)
    running = True
    while running:
        try:
            Chromedriver.get(InstagramLogin.tf_To_url())
            if Chromedriver != None:
                InstagramLogin.tf_Type_Email_or_Phone(Chromedriver)
                InstagramLogin.tf_Type_Full_name(Chromedriver)
                InstagramLogin.tf_Type_User_name(Chromedriver)
                InstagramLogin.tf_Type_Password(Chromedriver)
                InstagramLogin.tf_screen_shots(Chromedriver)
                InstagramLogin.tf_source_code(Chromedriver)
                InstagramLogin.tf_Type_do_signup(Chromedriver)
                InstagramLogin.tf_Type_notification(Chromedriver)
                running = False

        except Exception as e:
            print(e)
            new = ""
            try:
                new = ALL_PROXIES.pop()
            except Exception as e:
                ALL_PROXIES = InstagramLogin.tf_get_proxy()

            # reassign driver if fail to switch proxy
            Chromedriver = InstagramLogin.tf_proxy_driver(ALL_PROXIES)
            print("--- Switched proxy to: %s" % new)
            time.sleep(1)