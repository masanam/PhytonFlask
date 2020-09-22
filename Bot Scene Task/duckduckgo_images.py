from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date
import time
import requests
import shutil
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
import os
from PIL import Image
from io import BytesIO
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

class DuckduckgoImages():
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
                    DuckduckgoImages.tf_dir_check_and_rename(directory)
                    return directory

    def tf_file_check_and_rename(file, add=0):
        original_file = file
        if add != 0:
            split = file.split(".")
            part_1 = split[0] + "_" + str(add)
            file = ".".join([part_1, split[1]])
        if not os.path.isfile(file):
            try:
                os.rename(original_file, file)
            except FileNotFoundError:
                pass
        else:
            add += 1
            DuckduckgoImages.tf_file_check_and_rename(original_file, add)

    def tf_dir_check_and_rename(dirpath, add = 0):
        original_file = dirpath
        if add != 0:
            dirpath = dirpath + " (" + str(add) + ")"
        if not os.path.isdir(dirpath):
            try:
                os.rename(original_file, dirpath)
            except FileNotFoundError:
                pass
        else:
            add += 1
            DuckduckgoImages.tf_dir_check_and_rename(original_file, add)

    def tf_screen_shots(driver, scroll_delay=1):
        path = DuckduckgoImages.tf_check_folder_path("screenshot")
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
            DuckduckgoImages.tf_file_check_and_rename(file_name)
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
            if total_height < 20000:
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
        path = DuckduckgoImages.tf_check_folder_path("sourcepage")
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

        DuckduckgoImages.tf_File_name = path + "/" + title + ".html"
        if os.path.exists(DuckduckgoImages.tf_File_name):
            DuckduckgoImages.tf_file_check_and_rename(DuckduckgoImages.tf_File_name)
        pagesource = driver.page_source.encode('ascii', 'ignore')
        soup = BeautifulSoup(pagesource, 'html.parser')
        # Create text file, then write page source to the file
        fh = open(DuckduckgoImages.tf_File_name, 'w')
        fh.write(str(soup.prettify()))
        fh.close()

    def save_image_to_file(image, dirname, suffix):
        with open('{dirname}/img_{suffix}.jpg'.format(dirname=dirname, suffix=suffix), 'wb') as out_file:
            shutil.copyfileobj(image.raw, out_file)

    def tf_download_images(dirname, links):
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

    #To url
    def tf_To_url(search):
        url= 'https://duckduckgo.com/?ia=web&q='+search
        return url

    def tf_Click_images(Chromedriver):
        duck_duck_bar = Chromedriver.find_element_by_id("duckbar")
        choose_image_option = duck_duck_bar.find_element_by_link_text("Images")
        choose_image_option.click()
        time.sleep(Wait_2)

    def tf_Get_source_page_for_image(Chromedriver,query="admin"):
        image_collection = []
        div_select_for_image_collections = Chromedriver.find_element_by_xpath("//div[@class='tile-wrap']")
        image_collections = div_select_for_image_collections.find_elements_by_tag_name("img")
        for image_tag in image_collections:
            image = ''
            try:
                image = image_tag.get_attribute("src")
            except Exception as e:
                print(e)
                pass
            if str(image).startswith("https://external-content.duckduckgo.com/iu/?u="):
                image_url = image.replace("https://external-content.duckduckgo.com/iu/?u=", "")
                image_url_parsed = urlparser.unquote(image_url)
                image_collection.append(image_url_parsed)
        create_folder = "duck_duck_go/"+query
        image_path = DuckduckgoImages.tf_check_folder_path(create_folder)
        image_name = "image_urls_"+query
        with open(image_path + '/' + "" + image_name + '.csv', 'w') as f:
            for item in image_collection:
                f.write("%s\n" % item)
        ## download top ten images url
        top_ten_url = image_collection[0:10]
        DuckduckgoImages.tf_download_images(image_path, top_ten_url)

    # this task function create for image download with set limit
    def tf_Type_download_images(path=r"C:\python\Automation",start=0,end=10,query="admin"):
        url_load = []
        with open(path, 'r') as reader:
            line = reader.readline()
            while line != '':  # The EOF char is an empty string
                link = str(line).replace("\n","")
                url_load.append(link)
                line = reader.readline()
        download_images_list = DuckduckgoImages.tf_Image_url_download_range(url_load,start,end)
        create_folder = "duck_duck_go/" + query
        images_path = DuckduckgoImages.tf_check_folder_path(create_folder)
        if not os.path.exists(images_path):
            os.makedirs(images_path)
        DuckduckgoImages.tf_download_images(images_path, download_images_list)

    def tf_Image_url_download_range(url_list,start,end):
        if type(url_list) == list:
            if len(url_list) != 0:
                if end < len(url_list):
                    if start < len(url_list):
                        return url_list[start:end]
                    else:
                        return url_list[:len(url_list)-1]
                else:
                    return url_list[start:len(url_list) - 1]
#@NoSelf
# call this function here.....
# file_path = "/home/rails/projects/django_projects/shane/source_page_screen_shot_media/2019-12-12/duck_duck_go/user/image_urls_shane baba.csv"
# query = "admin"
# start = 10
# ends = 50
# tf_Type_download_images(file_path,start,ends,query)

#--- YOU ONLY NEED TO CARE FROM THIS LINE ---
# creating new driver to use proxy
def duckduckgo_images(search):
    ALL_PROXIES = DuckduckgoImages.tf_get_proxy()
    Chromedriver = DuckduckgoImages.tf_proxy_driver(ALL_PROXIES)
    running = True
    while running:
        try:
            Chromedriver.get(DuckduckgoImages.tf_To_url(search))
            # Chromedriver.execute_script('window.open("%s")' % DuckduckgoImages.tf_To_url(search))
            if Chromedriver != None:
                DuckduckgoImages.tf_Click_images(Chromedriver)
                DuckduckgoImages.tf_screen_shots(Chromedriver)
                DuckduckgoImages.tf_source_code(Chromedriver)
                # DuckduckgoImages.tf_Get_source_page_for_image(Chromedriver)
                running = False

        except Exception as e:
            print(e)
            new = ""
            try:
                new = ALL_PROXIES.pop()
            except Exception as e:
                ALL_PROXIES = DuckduckgoImages.tf_get_proxy()

            # reassign driver if fail to switch proxy
            Chromedriver = DuckduckgoImages.tf_proxy_driver(ALL_PROXIES)
            print("--- Switched proxy to: %s" % new)
            time.sleep(1)