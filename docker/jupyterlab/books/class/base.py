import os
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class Auto_Client(object):
    def __init__(self, url='', domain=''):
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/google-chrome'
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        )
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-setuid-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--incognito')
        options.add_argument('--window-size=1500,1500')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(
            executable_path="/content/chromedriver", desired_capabilities=options.to_capabilities())
        self.driver.get(url)
        self.domain = domain
        self.search_box = None
        
    def __del__(self):
        print('driver deleted')
        self.driver.close()
        del self.driver
    
    def TransitionToPath(self, path):
        self.driver.get(self.domain + path)
        return True
    
    def SwitchChildWindow(self):
        window_child = self.driver.window_handles[1]
        self.driver.switch_to.window(window_child)
        return True
    
    def SwitchDefaultWindow(self):
        window_parent = self.driver.window_handles[0]
        self.driver.switch_to.window(window_parent)
        return True
        
    def sendkey_by_elmId(self, idname, data):
        print(idname, data)
        self.GetElementById(idname)
        self.SendKeys(data)
        time.sleep(0.1)
    
    def sendkey_by_elmName(self, name, data):
        print(name, data)
        self.GetElementByName(name)
        self.SendKeys(data)
        time.sleep(0.1)
        
    def GetCurrentUrl(self):
        print(self.driver.current_url)
        return self.driver.current_url
    
    def GetElementById(self, element_id=''):
        self.search_box = self.driver.find_element_by_id(element_id)
        if self.search_box == None: return False
        self.search_box.location_once_scrolled_into_view
        return True
    
    def GetElementByName(self, element_name=''):
        self.search_box = self.driver.find_element_by_name(element_name)
        if self.search_box == None: return False
        self.search_box.location_once_scrolled_into_view
        return True
    
    def GetElementByClassName(self, element_classname=''):
        self.search_box = self.driver.find_element_by_name(element_classname)
        if self.search_box == None: return False
        self.search_box.location_once_scrolled_into_view
        return True
    
    def GetElementBySelecter(self, element_selecter=''):
        self.search_box = self.driver.find_element_by_css_selector(element_selecter)
        if self.search_box == None: return False
        self.search_box.location_once_scrolled_into_view
        return True
    
    def SendKeys(self, data=''):
        self.search_box.send_keys(data)
        return True
    
    def EnterKeys(self):
        self.search_box.send_keys(Keys.RETURN)
        return True
    
    def SelectElement(self, selecter='', index=0):
        self.GetElementBySelecter(selecter)
        #セレクトタグの要素を指定してSelectクラスのインスタンスを作成
        select = Select(self.search_box)
        #セレクトタグのオプションをインデックス番号から選択する
        select.select_by_index(index)
        return True
    
    def SelectElementByNameFromIndex(self, name='', index=0):
        self.GetElementByName(name)
        select = Select(self.search_box)
        select.select_by_index(index)
        return True
    
    def SelectElementByNameFromValue(self, name='', value=0):
        self.GetElementByName(name)
        select = Select(self.search_box)
        select.select_by_value(value)
        return True
    
    def SelectRadioElement(self, selecter=''):
        self.execute_js("document.querySelector('"+selecter+"').checked = true;")
        return True

    def clickelement(self):
        self.search_box.click
        return True
    
    def submit(self):
        self.search_box.submit()
        return True
    
    def execute_js(self, script=''):
        self.driver.execute_script(script)
        return True
    
    def GetElementTextWithSelecter(self, selecter):
        self.GetElementBySelecter(selecter)
        return self.search_box.get_attribute('innerText')
    
    def SaveScreenShot(self, path='', filename='', is_overwrite=True):
        try:
            if os.path.isfile(path + filename) and is_overwrite:
                os.remove(path + filename)
                self.driver.save_screenshot(path + filename)
            else:
                self.driver.save_screenshot(path + filename)
            return True
            
        except Exception as e:
            print(e)
            return False