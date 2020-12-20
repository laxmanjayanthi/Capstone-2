from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class Testprojecthome(StaticLiveServerTestCase):

    def setUp(self):
        self.browser= webdriver.Chrome("functional_tests/chromedriver.exe")

    def tearDown(self):
        self.browser.close()
    
    def test_no_login(self):
        self.browser.get(self.live_server_url)
        #alert= self.browser.find_element
        time.sleep(2)
        self.browser.find_element_by_id("b1").click()
        self.browser.find_element_by_name("username").send_keys("jhvjgasjh")
        self.browser.find_element_by_name("password").send_keys("jasbjd")
        time.sleep(2)
        self.browser.find_element_by_name("login").click()  

        alert=self.browser.find_element_by_class_name("invalid")
        self.assertEquals(
            alert.find_element_by_tag_name('h3').text,
            "Invalid Credentials"
        )

    def test_register(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('b2').click()
        self.browser.find_element_by_name("first_name").send_keys("re")
        self.browser.find_element_by_name("last_name").send_keys("pay")
        self.browser.find_element_by_name("username").send_keys("repay")
        self.browser.find_element_by_name("email").send_keys("repay@gmail.com")
        self.browser.find_element_by_name("password1").send_keys("capstone@8")
        self.browser.find_element_by_name("password2").send_keys("capstone@8")
        self.browser.find_element_by_class_name("registerbtn").click()
        self.browser.find_element_by_name("username").send_keys("repay")
        self.browser.find_element_by_name("password").send_keys("capstone@8")
        self.browser.find_element_by_name("login").click() 
        alert=self.browser.find_element_by_class_name("banner-w3ls-inner")
        self.assertEquals(
            alert.find_element_by_tag_name('h3').text,
            "Online Banking"
        )
  

    # def test_about(self):
    #     self.browser.get(self.live_server_url)
    #     self.browser.find_element_by_link_text('About').click()
    #     alert=self.browser.find_element_by_class_name("name")
    #     self.assertEquals(
    #         alert.find_element_by_tag_name('h3').text,
    #         "Plagiarism Detection"
    #     )


    # def test_register(self):
    #     self.browser.get(self.live_server_url)
    #     self.browser.find_element_by_link_text('Register').click()
    #     self.browser.find_element_by_name("username").send_keys("pranay")
    #     self.browser.find_element_by_name("email").send_keys("jasti.pranay@gmail.com")
    #     self.browser.find_element_by_name("password1").send_keys("capstone@8")
    #     self.browser.find_element_by_name("password2").send_keys("capstone@8")
    #     self.browser.find_element_by_name("submit").click()
    #     self.browser.find_element_by_name("username").send_keys("pranay")
    #     self.browser.find_element_by_name("password").send_keys("capstone@8")
    #     self.browser.find_element_by_name("submit").click() 
    #     alert=self.browser.find_element_by_class_name("row")
    #     self.assertEquals(
    #         alert.find_element_by_tag_name('h2').text,
    #         "Proctored"
    #     )


    # def test_upload(self): 
    #     self.browser.get(self.live_server_url)
    #     self.browser.find_element_by_link_text('Register').click()
    #     self.browser.find_element_by_name("username").send_keys("pranay")
    #     self.browser.find_element_by_name("email").send_keys("jasti.pranay@gmail.com")
    #     self.browser.find_element_by_name("password1").send_keys("capstone@8")
    #     self.browser.find_element_by_name("password2").send_keys("capstone@8")
    #     self.browser.find_element_by_name("submit").click()
    #     self.browser.find_element_by_name("username").send_keys("pranay")
    #     self.browser.find_element_by_name("password").send_keys("capstone@8")
    #     self.browser.find_element_by_name("submit").click() 
    #     self.browser.find_element_by_link_text('Upload Assignment').click()
    #     self.browser.find_element_by_name("content").send_keys("test")
    #     self.browser.find_element_by_id("id_document").send_keys("D:\\Users\\Pranay Chowdary\\Downloads\\pethullanaveenreddy_finalreport.docx")
    #     self.browser.find_element_by_name("submit").click()
    #     time.sleep(10)
    #     alert=self.browser.find_element_by_id("plag")
        
    #     self.assertEquals(
    #         alert.find_element_by_tag_name('h3').text,
    #         "Plagiarism Details"
    #     )