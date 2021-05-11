import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from secret import email, password, rasta, secret_key, email_user, password_user

from tests.admin import FlaskAdminTestCase 
import requests
# class FlaskTestCase(unittest.TestCase):               

    # def test_unregister_button(self):
    #     print("Checking  if Unregister Button is Working")
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

    # def test_unregister_button(self):

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

    #         edit_button = WebDriverWait(driver, 20).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="navbarResponsive"]/ul/li[6]/a'))
    #         )
    #         edit_button.send_keys(Keys.RETURN)

    #         unregister_button = WebDriverWait(driver, 20).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="body-top"]/div[1]/form[2]/div/button'))
    #         )

    #         unregister_button.send_keys(Keys.RETURN)

    #         self.assertTrue('GOOD BYE!' in driver.page_source)
    #         print("Unregister Button Working")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()
        

    # def test_mail_functionality_on_applying(self): 
    #     driver = webdriver.Chrome(rasta)
    #     driver.get("http://localhost:5000/login")
    #     print("Testing Mail sending functionality and Verified Join Button Visibility")
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

    
    # def test_join_button_visible_literaray(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/literary")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on literary page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()

    # def test_join_button_visible_cinephiles(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/cinephiles")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on cinephiles page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()


    # def test_join_button_visible_kalakriti(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/kalakriti")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on kalakriti page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()

    # def test_join_button_visible_dance(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/dance")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on dance page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()   

    # def test_join_button_visible_dramatics(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/dramatics")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on dramatics page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()

    # def test_join_button_visible_music(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/music")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on music page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()  

    # def test_join_button_visible_mystic_hues(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/mystic_hues")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on mystic_hues page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()   

    # def test_join_button_visible_quiz(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/quiz")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on quiz page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()  


    # def test_join_button_visible_debsoc(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/debsoc")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on debsoc page")
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/avana")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on avana page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()    

    # def test_join_button_visible_srijanClub(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/srijanClub")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on srijanClub page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()    

    # def test_join_button_visible_progClub(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/progClub")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on progClub page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()   

    # def test_join_button_visible_robotics(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/robotics")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on robotics page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()    

    # def test_join_button_visible_concreate(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/concreate")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on concreate page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()    

    # def test_join_button_visible_cae(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/cae")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on cae page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()    

    # def test_join_button_visible_astronomy(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/astronomy")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on astronomy page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()    

    # def test_join_button_visible_electronics(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/electronics")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on electronics page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()  

    # def test_join_button_visible_aeromodelling(self):
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/aeromodelling")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on aeromodelling page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()    

    # def test_join_button_visible_dsc(self):
    #     print("Checking DSC club")
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
    #         requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
    #         driver.get("http://localhost:5000/clubs/dsc")
    #         join_button = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, '/html/body/header/div/a'))
    #         )
    #         join_button.send_keys(Keys.RETURN)
    #         print("Join Button visibility on dsc page")
    #     except Exception as e:
    #         print("Test Case Failed")
    #         print(e)
    #         driver.quit()
    #         exit()       

if __name__ == '__main__':
    unittest.main()
