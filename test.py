from app import app
from flask import session
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from secret import email, password
# class FlaskTestCase(unittest.TestCase):

#     # Ensure that Flask was set up correctly
#     def test_index(self):
#         tester = app.test_client(self)
#         response = tester.get('/', content_type='html/text')
#         self.assertEqual(response.status_code, 200)

#     # Ensure that clubs show up correctly on homepage
#     def test_home_page(self):
#         tester = app.test_client(self)
#         response = tester.get('/', content_type='html/text')
#         self.assertTrue(b'Cultural Clubs' in response.data)
#         self.assertTrue(b'Technical Clubs' in response.data)
#         self.assertTrue(b'clubsiiti' in response.data)
#         self.assertTrue(b'about' in response.data)
#         self.assertTrue(b'contact' in response.data)

#     def test_session(self):
#         testter = app.test_client(self)
#         session['isAdmin'] = True
#         response = tester.get('/', content_type='html/text')
#         self.assertTrue(b'contact' in response.data)

if __name__ == '__main__':
    # unittest.main()
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get("http://localhost:5000/login")
    try:
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
        )
        input_field.send_keys(email)
        input_field.send_keys(Keys.RETURN)
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
        )
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        time.sleep(40)
    finally:
        driver.quit()
