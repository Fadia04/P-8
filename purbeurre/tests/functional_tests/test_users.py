from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAuthentification(StaticLiveServerTestCase):
    
    def test_signup(self):
        #options = webdriver.ChromeOptions()
        #options.add_experimental_option('excludeSwitches', ['enable-logging'])
                
        self.browser = webdriver.Chrome("purbeurre/tests/functional_tests/chromedriver")
        self.browser.get(self.live_server_url + reverse("signup"))
        
        username = self.browser.find_element(By.NAME, "username")
        username.send_keys("nanou10")
        email = self.browser.find_element(By.NAME, "email")
        email.send_keys("nanou10@protonmail.com")    
        fname = self.browser.find_element(By.NAME, "first_name")
        fname.send_keys("hmloulou10")
        lastname = self.browser.find_element(By.NAME, "last_name")
        lastname.send_keys("loulouhm")
        password1 = self.browser.find_element(By.NAME, "password1")
        password1.send_keys("code12345")        
        password2 = self.browser.find_element(By.NAME, "password2")
        password2.send_keys("code12345")        
               
        #agree_term = self.browser.find_element(By.NAME, "agree_term")
        #agree_term.click()    
        #wait = WebDriverWait(self.browser, 10)
        #wait.until(EC.visibility_of_element_located((By.ID, "inscription-button"))).click()
        signup = self.browser.find_element(By.ID, "inscription-button")
        signup.click()
        #time.sleep(20)    
        self.assertEqual(self.browser.find_element(By.TAG_NAME,'h2').text, "Inscription")
        self.assertEqual(self.browser.current_url, self.live_server_url + reverse("login"))
        
    """
    def test_login(self):
        self.browser = webdriver.Chrome("purbeurre/tests/functional_tests/chromedriver")
        self.browser.get(self.live_server_url + reverse("login"))
        username = self.browser.find_element(By.NAME,"username")
        username.send_keys("loulou")
        password = self.browser.find_element(By.NAME,"password")
        password.send_keys("kiki")
        #wait = WebDriverWait(self.browser, 20)
        #wait.until(EC.visibility_of_element_located((By.ID, 'connexion-button')))
        #wait.until(EC.ElementToBeClickable(By.XPath("//*[@id='connexion-button']"))).Click();
        login_button = self.browser.find_element(By.ID, "connexion-button")
        login_button.click()
        time.sleep(5)
        #self.assertEqual(self.browser.find_element(By.TAG_NAME, "h1").text, "Du gras, oui, mais de qualité")
        self.assertEqual(self.browser.current_url, self.live_server_url + reverse("home"))
        self.browser.close()   
        #time.sleep(5)
    
    
    def test_logout(self):
        self.browser = webdriver.Chrome("purbeurre/tests/functional_tests/chromedriver")
        self.browser.get(self.live_server_url + reverse("login"))
        username = self.browser.find_element(By.NAME,"username")
        username.send_keys("nanou")
        password = self.browser.find_element(By.NAME,"password")
        password.send_keys("nanou12345")
        login_button = self.browser.find_element(By.CLASS_NAME,"d-grid")
        login_button.click()

        logout_button = self.browser.find_element(By.LINK_TEXT,"déconnexion")
        logout_button.click()
        
        #self.assertNotEqual(self.browser.page_source.find("LOGIN"), -1)
        self.assertEqual(self.browser.current_url, self.live_server_url + reverse("home"))
        self.browser.close()   
        #time.sleep(5)
        """    
        
