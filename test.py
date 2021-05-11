import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from secret import email, password
class FlaskTestCase(unittest.TestCase):

    # # Ensure that Flask was set up correctly
    # def test_index(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)

    # # Ensure that clubs show up correctly on homepage
    # def test_home_page(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/', content_type='html/text')
    #     self.assertTrue(b'Cultural Clubs' in response.data)
    #     self.assertTrue(b'Technical Clubs' in response.data)
    #     self.assertTrue(b'clubsiiti' in response.data)
    #     self.assertTrue(b'about' in response.data)
    #     self.assertTrue(b'contact' in response.data)

    # def test_session(self):
    #     tester = app.test_client(self)
    #     session['isAdmin'] = True
    #     response = tester.get('/', content_type='html/text')
    #     self.assertTrue(b'contact' in response.data)
    
    # def test_club_admim_login(self):
    #     "make sure club admin can sign in"
    #     driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
    #     driver.get("http://localhost:5000/login")
    #     try:
    #         input_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
    #         )
    #         input_field.send_keys(email)
    #         input_field.send_keys(Keys.RETURN)
    #         password_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    #         )
    #         password_field.send_keys(password)
    #         password_field.send_keys(Keys.RETURN)
    #         WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
    #         )
    #         self.assertTrue('Successfully signed in as' in driver.page_source)
    #     except:
    #         driver.quit()

    #         #check outer iiti email id //*[@id="navbarResponsive"]/ul/li[5]/a

    # def test_non_iiti_email(self):
        
    #     driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
    #     driver.get("http://localhost:5000/login")
    #     try:
    #         input_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
    #         )
    #         input_field.send_keys(email)
    #         input_field.send_keys(Keys.RETURN)
    #         password_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    #         )
    #         password_field.send_keys(password)
    #         password_field.send_keys(Keys.RETURN)


    #         WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
    #         )
    #         self.assertTrue('Please use IITI email id' in driver.page_source)

 
    #     except:
    #         driver.quit()

    def test_unregister_button(self):
        
        driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
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
        
            
            unregister_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="body-top"]/div[1]/h1'))
            )
            
            unregister_button.send_keys(Keys.RETURN)
            
            self.assertTrue('xxx' in driver.page_source)
            

 
        except:
            driver.quit()


       

if __name__ == '__main__':
    unittest.main()

