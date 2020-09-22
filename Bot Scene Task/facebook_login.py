from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

#Chrome_path = '/home/rails/python_requirement/chromedriver'
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

class FacebookLogin():
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
        # driver = Chrome(options=opts)

        Chromedriver = webdriver.Chrome(Chrome_path, options=opts)        
        Chromedriver.implicitly_wait(Wait_3)
        print("proxy is - ", pxy)
        return Chromedriver


    def tf_use_same_session(ChromeDriver):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        ChromeDriver = webdriver.Chrome(Chrome_path, options=opts) 
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

    print(tf_check_folder_path())

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
            FacebookLogin.tf_check_and_rename(original_file, add)

    def tf_screen_shots(driver, scroll_delay=0.3):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(Chrome_path, options=opts) 
        path = FacebookLogin.tf_check_folder_path("screenshot")
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
            FacebookLogin.tf_check_and_rename(file_name)
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
        path = FacebookLogin.tf_check_folder_path("sourcepage")
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(Chrome_path, options=opts) 
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
        if os.path.exists(FacebookLogin.tf_File_name):
            FacebookLogin.tf_check_and_rename(FacebookLogin.tf_File_name)
        pagesource = driver.page_source.encode('ascii', 'ignore')
        soup = BeautifulSoup(pagesource, 'html.parser')
        # Create text file, then write page source to the file
        fh = open(FacebookLogin.tf_File_name, 'w')
        fh.write(str(soup.prettify()))
        fh.close()

    #To url
    def tf_To_url():
        url= 'https://www.facebook.com/'
        return url

    def tf_Type_fb_username(Chromedriver):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        Chromedriver = webdriver.Chrome(Chrome_path, options=opts) 
        try:
            user_name = Chromedriver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input')
            user_name.clear()
            user_name.send_keys("johnbradman2019@gmail.com")
            time.sleep(Wait_1)
        except Exception as e:
            user_name = Chromedriver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/form/div[2]/div[1]/input')
            user_name.clear()
            user_name.send_keys("johnbradman2019@gmail.com")
            time.sleep(Wait_1)
            print("Try method second", e)

    def tf_Type_fb_userpassword(Chromedriver):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        Chromedriver = webdriver.Chrome(Chrome_path, options=opts) 
        try:
            user_pass = Chromedriver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input')
            user_pass.clear()
            user_pass.send_keys("Xysbsg@1238#76Bd")
            time.sleep(Wait_1)
        except Exception as e:
            user_pass = Chromedriver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/form/div[2]/div[2]/input')
            user_pass.clear()
            user_pass.send_keys("Xysbsg@1238#76Bd")
            time.sleep(Wait_1)
            print("Try method second", e)

    def tf_Type_fb_submit(Chromedriver):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        Chromedriver = webdriver.Chrome(Chrome_path, options=opts)
        try:
            submit_user = Chromedriver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input')
            submit_user.click()
            time.sleep(Wait_3)
            Chromedriver.find_element_by_tag_name('html').send_keys(Keys.ESCAPE)
            time.sleep(Wait_1)
        except Exception as e:
            submit_user = Chromedriver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/form/div[3]/button')
            submit_user.click()
            time.sleep(Wait_3)
            print("Try method second", e)

    #Send friend request
    def tf_Type_fb_search_user(Chromedriver):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        Chromedriver = webdriver.Chrome(Chrome_path, options=opts)
        try:
            search_user = Chromedriver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/div/div/div/div/input[2]')
            search_user.clear()
            search_user.send_keys("shekhar")
            search_user.send_keys(Keys.RETURN)
            time.sleep(Wait_2)
        except Exception as e:
            print(e)
            pass

    def tf_Type_search_user_see_all(Chromedriver):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        Chromedriver = webdriver.Chrome(Chrome_path, options=opts)        
        try:
            see_all = Chromedriver.find_element_by_xpath(
                '/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div/div/div[1]/a')
            see_all.click()
            time.sleep(Wait_2)
        except Exception as e:
            print(e)
            pass

    def tf_Type_driver_scroller(Chromedriver):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        Chromedriver = webdriver.Chrome(Chrome_path, options=opts)        
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

    def tf_Type_fb_send_request(Chromedriver):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        Chromedriver = webdriver.Chrome(Chrome_path, options=opts)        
        FacebookLogin.tf_Type_driver_scroller(Chromedriver)
        friend_request = Chromedriver.find_elements_by_class_name("addButton")
        i=0
        try:
            while True:
                friend_request[i].click()
                i+=1
        except Exception as e:
            print(e)
            pass
        time.sleep(Wait_2)


    #Send post on timeline
    def tf_Type_fb_send_post(Chromedriver):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        Chromedriver = webdriver.Chrome(Chrome_path, options=opts)
        post_content_click = Chromedriver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div/div/div/form/div[1]/div/div[2]/textarea')
        post_content_click.click()
        time.sleep(Wait_1)
        content_post_prepare = Chromedriver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/span')
        content_post_prepare.send_keys("My interest is in information technology.")
        time.sleep(Wait_2)

    def tf_Type_fb_submit_post(Chromedriver):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        Chromedriver = webdriver.Chrome(Chrome_path, options=opts)
        post_submit = Chromedriver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div[2]/button')
        post_submit.click()
        time.sleep(Wait_2)

    # People Friend List Search
    def tf_Type_fb_see_all_people_may_you_know(Chromedriver):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        Chromedriver = webdriver.Chrome(Chrome_path, options=opts)
        see_all = Chromedriver.find_element_by_xpath('//*[@class="ego_section"]/div[1]/a')
        see_all.click()
        time.sleep(Wait_3)

    def tf_Type_fb_click_people_timeline(Chromedriver,select_person):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        Chromedriver = webdriver.Chrome(Chrome_path, options=opts) 
        # handle_script = Chromedriver.window_handles[1]
        select_person.click()
        # Chromedriver.switch_to_window(handle_script)
        time.sleep(Wait_3)
        FacebookLogin.tf_Type_driver_scroller(Chromedriver)
        select_friend = Chromedriver.find_element_by_link_text("Friends")
        select_friend.click()
        time.sleep(Wait_3)
        FacebookLogin.tf_Type_driver_scroller(Chromedriver)
        # handle_script.close()

    def tf_Type_fb_click_friends(Chromedriver):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        Chromedriver = webdriver.Chrome(Chrome_path, options=opts)        
        FacebookLogin.tf_Type_driver_scroller(Chromedriver)
        friend_list = Chromedriver.find_elements_by_class_name("uiList")
        i = 0
        try:
            while True:
                select_person = friend_list[i].find_element_by_class_name("friendBrowserNameTitle")
                FacebookLogin.tf_Type_fb_click_people_timeline(Chromedriver,select_person)
                i += 1
        except Exception as e:
            print(e)
            pass
        time.sleep(Wait_2)

    # Send private message through chat box search
    def tf_Type_fb_click_chat_box(Chromedriver):
        try:
            chat_option = Chromedriver.find_element_by_xpath('//*[@class="fbNubButton"]/div/span[2]')
            chat_option.click()
            time.sleep(Wait_2)
        except:
            pass

    def tf_Type_fb_chat_box_search(Chromedriver):
        try:
            chat_box_search = Chromedriver.find_element_by_xpath('//*[@id="chatsearch"]/div/span/label/input')
            chat_box_search.clear()
            chat_box_search.send_keys("john")
            time.sleep(Wait_2)
        except:
            pass

    def tf_Type_fb_select_chat_person(Chromedriver):
        try:
            select_person = Chromedriver.find_element_by_xpath('//*[@id="js_1af"]/a/div/div[2]/div/div')
            select_person.click()
            time.sleep(Wait_2)
            chate_sender = Chromedriver.find_element_by_xpath('//div[@role="combobox"]')
            chate_sender.send_keys("hello john!" + Keys.ENTER)
            time.sleep(Wait_1)
        except:
            pass

    def tf_Type_fb_messenger(Chromedriver):
        Chromedriver.find_element_by_name("mercurymessages").click()
        WebDriverWait(Chromedriver, 120).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'John Bradman')]")))
        time.sleep(Wait_1)
        Chromedriver.find_element_by_xpath('//span[contains(text(),"John Bradman")]').click()
        time.sleep(Wait_1)
        Chromedriver.find_element_by_xpath('//div[@role="combobox"]').send_keys("Your text here" + Keys.ENTER)
        time.sleep(Wait_2)

    #--- YOU ONLY NEED TO CARE FROM THIS LINE ---
    # creating new driver to use proxy
def facebook_login():
    ALL_PROXIES = FacebookLogin.tf_get_proxy()
    Chromedriver = FacebookLogin.tf_proxy_driver(ALL_PROXIES)
    running = True
    while running:
        try:
            Chromedriver.get(FacebookLogin.tf_To_url())
            if Chromedriver != None:
                FacebookLogin.tf_Type_fb_username(Chromedriver)
                FacebookLogin.tf_Type_fb_userpassword(Chromedriver)
                FacebookLogin.tf_Type_fb_submit(Chromedriver)
                FacebookLogin.tf_Type_fb_click_chat_box(Chromedriver)
                FacebookLogin.tf_Type_fb_chat_box_search(Chromedriver)
                FacebookLogin.tf_Type_fb_select_chat_person(Chromedriver)
                        # tf_Type_see_all_people_may_you_know(Chromedriver)
                        # tf_Type_click_friends(Chromedriver)
                        # tf_Type_search_user(Chromedriver)
                        # tf_Type_search_user_see_all(Chromedriver)
                        # tf_Type_send_request(Chromedriver)
                        # tf_Type_send_post(Chromedriver)
                        # tf_Type_submit_post(Chromedriver)
                running = False

        except Exception as e:
            print(e)
            new = ""
            try:
                new = ALL_PROXIES.pop()
            except Exception as e:
                ALL_PROXIES = FacebookLogin.tf_get_proxy()

                    # reassign driver if fail to switch proxy
            Chromedriver = FacebookLogin.tf_proxy_driver(ALL_PROXIES)
            print("--- Switched proxy to: %s" % new)
            time.sleep(1)