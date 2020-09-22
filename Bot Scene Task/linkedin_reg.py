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

class LinkedinReg():

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
            tf_check_and_rename(original_file, add)

    def tf_screen_shots(driver, scroll_delay=0.3):
        path = LinkedinReg.tf_check_folder_path("screenshot")
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
            LinkedinReg.tf_check_and_rename(file_name)
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
        path = LinkedinReg.tf_check_folder_path("sourcepage")
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

        LinkedinReg.tf_File_name = path + "/" + title + ".html"
        if os.path.exists(LinkedinReg.tf_File_name):
            LinkedinReg.tf_check_and_rename(LinkedinReg.tf_File_name)
        pagesource = driver.page_source.encode('ascii', 'ignore')
        soup = BeautifulSoup(pagesource, 'html.parser')
        # Create text file, then write page source to the file
        fh = open(LinkedinReg.tf_File_name, 'w')
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
        url = 'https://www.linkedin.com/'
        return url

    #Find UI item - Find UI element and click must be put inside the same function
    #Use a separate function to store find UI element might not work in some situations.
    #Click my account
    def tf_Click_Sign_up(Chromedriver):
        try:
            Sign_up = Chromedriver.find_element_by_link_text('Join now')
            Sign_up.click()
            time.sleep(Wait_3)
        except:
            pass

    def tf_Type_firstname(Chromedriver):
        fname = None
        email = None
        try:
            # Pattern no 1
            fname = Chromedriver.find_element_by_name ('firstName')
            fname.clear()
        except:
            try:
                # Pattern no 2
                email = Chromedriver.find_element_by_name('email-or-phone')
                email.clear()
            except:
                try:
                    # Pattern no 3
                    email = Chromedriver.find_element_by_name('emailAddress')
                    email.clear()
                except:
                    pass
        if fname:
            fname.send_keys("jissu")
        elif email:
            email.send_keys("jissumahh14234@hotmail.com")
        time.sleep(Wait_1)

    def tf_Type_lastname(Chromedriver):
        lname = None
        password = None
        try:
            # Pattern no 1
            lname = Chromedriver.find_element_by_name ('lastName')
            lname.clear()
        except:
            #Pattern no 2&3
            try:
                password = Chromedriver.find_element_by_name('password')
                password.clear()
            except:
                pass
        if lname:
            lname.send_keys("mahh")
            time.sleep(Wait_1)
        elif password:
            password.send_keys("@abc1234#Az")
            time.sleep(Wait_2)

    def tf_linkedIn_do_next(Chromedriver):
        join_process = None
        try:
            # Pattern no 2
            join_process = Chromedriver.find_element_by_id("join-form-submit")
            join_process.click()
        except:
            try:
                # Pattern no 3
                join_process = Chromedriver.find_element_by_id("submit-join-form-text")
                join_process.click()
            except:
                pass
        if join_process:
            time.sleep(Wait_2)

    def tf_Type_email(Chromedriver):
        email = None
        fname = None
        try:
            # Pattern no 1
            email = Chromedriver.find_element_by_name('emailAddress')
            email.clear()
        except:
            try:
                # Pattern no 2
                fname = Chromedriver.find_element_by_name('first-name')
                fname.clear()
            except:
                try:
                    # Pattern no 3
                    fname = Chromedriver.find_element_by_id('first-name')
                    fname.clear()
                except:
                    pass
        if email:
            email.send_keys("jissumahh14234@hotmail.com")
            time.sleep(Wait_1)
        elif fname:
            fname.send_keys("jissu")
            time.sleep(Wait_1)


    def tf_Type_password(Chromedriver):
        lname = None
        try:
            # Pattern no 1
            password = Chromedriver.find_element_by_id ('join-password')
            password.clear()
            password.send_keys("@abc1234#Az")
        except:
            try:
                # Pattern no 2
                lname = Chromedriver.find_element_by_name('last-name')
            except:
                try:
                    # Pattern no 3
                    lname = Chromedriver.find_element_by_id('last-name')
                except:
                    pass
        if lname:
            lname.clear()
            lname.send_keys("mahh")
        time.sleep(Wait_1)

    def tf_linkedIn_do_submit(Chromedriver):
        join_now = None
        try:
            # Pattern no 1&3
            join_now = Chromedriver.find_element_by_id("submit-join-form-text")
            join_now.click()
        except:
            try:
                # Pattern no 2
                join_now = Chromedriver.find_element_by_id("join-form-submit")
                join_now.click()
            except:
                pass
        if join_now:
            time.sleep(Wait_2)

    def tf_Type_Mobile_Country(Chromedriver):
        country_value = None
        # Pattern no 1
        try:
            country_value = Select(Chromedriver.find_element_by_name("country-select"))
        except:
            # Pattern no 2
            try:
                Chromedriver.switch_to.frame(Chromedriver.find_element_by_tag_name('iframe'))
                country_value =  Select(Chromedriver.find_element_by_name("countryCode"))
            except:
                pass

        if country_value:
            country_value.select_by_value('in')
            time.sleep(Wait_1)

    def tf_linkedIn_do_mobile(Chromedriver):
        mobile_field = None
        try:
            # Pattern no 1
            mobile_field = Chromedriver.find_element_by_id("phoneNumber")
        except:
            # Pattern no 2
            try:
                Chromedriver.switch_to.frame(Chromedriver.find_element_by_tag_name('iframe'))
                mobile_field = Chromedriver.find_element_by_name("phoneNumber")
            except:
                pass
        if mobile_field:
            mobile_field.clear()
            mobile_field.send_keys("9812121212")
            time.sleep(Wait_1)

    def tf_Type_do_submit(Chromedriver):
        try:
            submit_form = Chromedriver.find_element_by_xpath("//button[@type='submit']")
            submit_form.send_keys(Keys.RETURN)
            time.sleep(Wait_1)
        except Exception as e:
            print(e)
            pass

    def tf_recaptch_click(Chromedriver):
        try:
            recaptch = Chromedriver.find_element_by_id("recaptcha-anchor")
            recaptch.click()
            time.sleep(Wait_2)
        except:
            pass

    def tf_Type_remove_model(Chromedriver):
        Chromedriver.find_element_by_tag_name('html').send_keys(Keys.ESCAPE)
        time.sleep(Wait_1)

#--- YOU ONLY NEED TO CARE FROM THIS LINE ---
# creating new driver to use proxy
def linkedin_reg():
    ALL_PROXIES = LinkedinReg.tf_get_proxy()
    Chromedriver = LinkedinReg.tf_proxy_driver(ALL_PROXIES)
    running = True
    while running:
        try:
            Chromedriver.get(LinkedinReg.tf_To_url())
            time.sleep(Wait_3)
            if Chromedriver != None:
                LinkedinReg.tf_Click_Sign_up(Chromedriver)
                LinkedinReg.tf_Type_firstname(Chromedriver)
                LinkedinReg.tf_Type_lastname(Chromedriver)
                LinkedinReg.tf_linkedIn_do_next(Chromedriver)
                LinkedinReg.tf_Type_email(Chromedriver)
                LinkedinReg.tf_Type_password(Chromedriver)
                LinkedinReg.tf_linkedIn_do_submit(Chromedriver)
                LinkedinReg.tf_Type_Mobile_Country(Chromedriver)
                LinkedinReg.tf_linkedIn_do_mobile(Chromedriver)
                LinkedinReg.tf_recaptch_click(Chromedriver)

                LinkedinReg.tf_Type_remove_model(Chromedriver)
            running = False
        except Exception as e:
            print(e)
            new = ""
            try:
                new = ALL_PROXIES.pop()
            except Exception as e:
                ALL_PROXIES = LinkedinReg.tf_get_proxy()


            # reassign driver if fail to switch proxy
            Chromedriver = LinkedinReg.tf_proxy_driver(ALL_PROXIES)
            print("--- Switched proxy to: %s" % new)
            time.sleep(1)