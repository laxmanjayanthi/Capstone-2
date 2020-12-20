from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import *


class TestUrls(SimpleTestCase):


    def test_accounts_register(self):
        url=reverse("register")
        self.assertEquals(resolve(url).func, register)

    def test_accounts_login(self):
        url=reverse("login")
        self.assertEquals(resolve(url).func, login)
    
    def test_accounts_main(self):
        url=reverse("main")
        self.assertEquals(resolve(url).func, main)
    
    def test_accounts_contact(self):
        url=reverse("contact")
        self.assertEquals(resolve(url).func, contact)

    
    def test_accounts_single(self):
        url=reverse("single")
        self.assertEquals(resolve(url).func, single) 
    
    def test_accounts_index(self):
        url=reverse("index")
        self.assertEquals(resolve(url).func, index)   
   
    def test_sccounts_shop(self):
        url=reverse("shop")
        self.assertEquals(resolve(url).func, shop) 

    def test_accounts_o404(self):
        url=reverse("o404")
        self.assertEquals(resolve(url).func, o404)    
   

    
    

    