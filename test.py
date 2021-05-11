import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from secret import email, password, rasta, secret_key
import time
import requests
class FlaskTestCase(unittest.TestCase):               

    # def test_club_admim_login(self):
        
    #     driver = webdriver.Chrome(rasta)
    #     driver.get("http://localhost:5000/login")
    #     try:
    #         input_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="identifierId"]'))
    #         )
    #         input_field.send_keys(email)
    #         input_field.send_keys(Keys.RETURN)
    #         password_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    #         )
    #         password_field.send_keys(password)
    #         password_field.send_keys(Keys.RETURN)
    #         WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
    #         )
    #         self.assertTrue('Successfully signed in as' in driver.page_source)
    #         print("Checked If Club Admin is able to sign in")
    #         driver.quit()
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()

    # def test_details_visibility_to_non_admin_users(self):
    #     driver = webdriver.Chrome(rasta)
    #     driver.get("http://localhost:5000/login")
    #     try:
    #         input_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="identifierId"]'))
    #         )
    #         input_field.send_keys(email)
    #         input_field.send_keys(Keys.RETURN)
    #         password_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    #         )
    #         password_field.send_keys(password)
    #         password_field.send_keys(Keys.RETURN)
    #         WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
    #         )
    #         self.assertTrue('Successfully signed in as' in driver.page_source)
    #         driver.get("http://localhost:5000/clubs/literary")
    #         member_name = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="members"]/div/div[2]/table/tbody/tr[2]/td[1]/a'))
    #         )
    #         member_name.send_keys(Keys.RETURN)
    #         WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="body-top"]/div[1]/p[1]'))
    #         )
    #         self.assertTrue('Not Allowed' in driver.page_source)
    #         print("Checked visibility of details to non admin users")
    #         driver.quit()
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()
    
    # def test_non_iiti_email(self):
        
    #     driver = webdriver.Chrome(rasta)
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
    #         print("Test for non iiti email id")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()


    # def test_unregister_button(self):
        
    #     driver = webdriver.Chrome(rasta)
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
        
            
    #         unregister_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="body-top"]/div[1]/h1'))
    #         )
            
    #         unregister_button.send_keys(Keys.RETURN)
            
    #         self.assertTrue('GOOD BYE!' in driver.page_source)
    #         print("Unregister Button Working")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()

    def test_unregister_button(self):

        driver = webdriver.Chrome(rasta)
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

            edit_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="navbarResponsive"]/ul/li[6]/a'))
            )
            edit_button.send_keys(Keys.RETURN)

            unregister_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="body-top"]/div[1]/form[2]/div/button'))
            )

            unregister_button.send_keys(Keys.RETURN)

            self.assertTrue('GOOD BYE!' in driver.page_source)
            print("Unregister Button Working")
        except Exception as e:
            print("Test Case Failed")
            print(e)
            driver.quit()
            exit()
        

    # def test_mail_functionality_on_applying(self):
    #     driver = webdriver.Chrome(rasta)
    #     driver.get("http://localhost:5000/login")
    #     try:
    #         input_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="identifierId"]'))
    #         )
    #         input_field.send_keys(email)
    #         input_field.send_keys(Keys.RETURN)
    #         password_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    #         )
    #         password_field.send_keys(password)
    #         password_field.send_keys(Keys.RETURN)
    #         WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
    #         )
            
    #         # Make sure this email does not already exist in music club, thus remove it
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})

    #         driver.get("http://localhost:5000/clubs/music")
    #         apply_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="body-top"]/header/div/a'))
    #         )
    #         apply_button.send_keys(Keys.RETURN)

    #         self.assertTrue(
    #             'Club Head will decide further....Hope for the best!' in driver.page_source)
    #         print("Testing Mail sending functionality and Verified Join Button Visibility")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()
    
    # def test_join_button_visible_avana(self):

    #     driver = webdriver.Chrome(rasta)
    #     driver.get("http://localhost:5000/login")
    #     try:
    #         input_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="identifierId"]'))
    #         )
    #         input_field.send_keys(email)
    #         input_field.send_keys(Keys.RETURN)
    #         password_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    #         )
    #         password_field.send_keys(password)
    #         password_field.send_keys(Keys.RETURN)
    #         WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
    #         )

    #     except:
    #         driver.quit()

    # def test_join_button_visible_music(self):
    #     # "make sure club admin can sign in"

    #     #    tester = app.test_client(self)
    #     #    response = tester.get('/clubs/avana', content_type='html/text')
    #     #    self.assertFalse(b'join' in response.data)

    #     driver = webdriver.Chrome(rasta)
    #     driver.get("http://localhost:5000/login")
    #     try:
    #         input_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="identifierId"]'))
    #         )
    #         input_field.send_keys(email)
    #         input_field.send_keys(Keys.RETURN)
    #         password_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    #         )
    #         password_field.send_keys(password)
    #         password_field.send_keys(Keys.RETURN)
    #         WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
    #         )
    #         if('Successfully signed in as' in driver.page_source):
    #             tester = app.test_client(self)
    #             response = tester.get('/clubs/music', content_type='html/text')
    #             self.assertTrue(b'join' in response.data)

    #     except:
    #         driver.quit()

    # def test_join_button_visible_dance(self):
    #     # "make sure club admin can sign in"

    #     #    tester = app.test_client(self)
    #     #    response = tester.get('/clubs/avana', content_type='html/text')
    #     #    self.assertFalse(b'join' in response.data)

    #     driver = webdriver.Chrome(rasta)
    #     driver.get("http://localhost:5000/login")
    #     try:
    #         input_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="identifierId"]'))
    #         )
    #         input_field.send_keys(email)
    #         input_field.send_keys(Keys.RETURN)
    #         password_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    #         )
    #         password_field.send_keys(password)
    #         password_field.send_keys(Keys.RETURN)
    #         WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
    #         )
    #         if('Successfully signed in as' in driver.page_source):
    #             tester = app.test_client(self)
    #             response = tester.get('/clubs/dance', content_type='html/text')
    #             self.assertTrue(b'join' in response.data)

    #     except:
    #         driver.quit()

    # def test_join_button_visible_dramatics(self):
    #     # "make sure club admin can sign in"

    #     #    tester = app.test_client(self)
    #     #    response = tester.get('/clubs/avana', content_type='html/text')
    #     #    self.assertFalse(b'join' in response.data)

    #     driver = webdriver.Chrome(rasta)
    #     driver.get("http://localhost:5000/login")
    #     try:
    #         input_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="identifierId"]'))
    #         )
    #         input_field.send_keys(email)
    #         input_field.send_keys(Keys.RETURN)
    #         password_field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    #         )
    #         password_field.send_keys(password)
    #         password_field.send_keys(Keys.RETURN)
    #         WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
    #         )
    #         if('Successfully signed in as' in driver.page_source):
    #             tester = app.test_client(self)
    #             response = tester.get('/clubs/dramatics',
    #                                   content_type='html/text')
    #             self.assertTrue(b'join' in response.data)
    #     except:
    #         driver.quit()
        
if __name__ == '__main__':
    unittest.main()
