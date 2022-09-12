from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By
import time


class TestHome(StaticLiveServerTestCase):
    def login(self):
        self.browser = webdriver.Chrome("purbeurre/tests/functional_tests/chromedriver")
        self.browser.get(self.live_server_url + reverse("login"))
        username = self.browser.find_element(By.NAME,"username")
        username.send_keys("nanou")
        password = self.browser.find_element(By.NAME,"password")
        password.send_keys("nanou12345")
        login_button = self.browser.find_element(By.CLASS_NAME,"d-grid")
        login_button.click()

        self.assertEqual(self.browser.find_element(By.TAG_NAME, "h2").text, "Connectez-vous")
        self.assertEqual(self.browser.current_url, self.live_server_url + reverse("home"))
        self.browser.close()   
        #time.sleep(5)
    def test_home_with_logged_user(self):
        self.login()

        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("home")
        )
        self.assertNotEqual(self.browser.page_source.find("LOGOUT"), -1)

    def test_home_with_not_logged_user(self):
        self.browser = webdriver.Chrome("purbeurre/tests/functional_tests/chromedriver")
        self.browser.get(self.live_server_url + reverse("home"))
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("home")
        )
        self.assertNotEqual(self.browser.page_source.find("LOGIN"), -1)
        