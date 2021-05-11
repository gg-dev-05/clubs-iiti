import unittest
from app import app
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from secret import email, password
class FlaskTestCase(unittest.TestCase):

    def test_club_admim_login(self):
        "make sure club admin can sign in"
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        driver.get("http://localhost:5000/login")
        try:
            input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="identifierId"]'))
            )
            input_field.send_keys(email)
            input_field.send_keys(Keys.RETURN)
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
            )
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
            )
            self.assertTrue('Successfully signed in as' in driver.page_source)
            driver.quit()
        except:
            driver.quit()

    def test_details_visibility_to_non_admin_users(self):
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        driver.get("http://localhost:5000/login")
        try:
            input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="identifierId"]'))
            )
            input_field.send_keys(email)
            input_field.send_keys(Keys.RETURN)
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
            )
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
            )
            self.assertTrue('Successfully signed in as' in driver.page_source)
            driver.get("http://localhost:5000/clubs/cinephiles")
            member_name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="members"]/div/div[2]/table/tbody/tr[2]/td[1]/a'))
            )
            member_name.send_keys(Keys.RETURN)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="body-top"]/div[1]/p[1]'))
            )
            self.assertTrue(
                'Only Club Head can continue further' in driver.page_source)
            driver.quit()
        except:
            driver.quit()

    def test_mail_functionality_on_applying(self):
        driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        driver.get("http://localhost:5000/login")
        try:
            input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="identifierId"]'))
            )
            input_field.send_keys(email)
            input_field.send_keys(Keys.RETURN)
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
            )
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
            )
            self.assertTrue('Successfully signed in as' in driver.page_source)
            driver.get("http://localhost:5000/clubs/music")
            apply_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="body-top"]/header/div/a'))
            )
            apply_button.send_keys(Keys.RETURN)

            self.assertTrue(
                'Club Head will decide further....Hope for the best!' in driver.page_source)
        except:
            driver.quit()


if __name__ == '__main__':
    unittest.main()
