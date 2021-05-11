import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from secret import rasta, email_user, password_user, email, password, secret_key
import requests
class FlaskUserTestCase(unittest.TestCase):
	def test_6_mail_functionality_on_applying(self): 
		print("Testing Mail sending functionality and Verifying Join Button Visibility")
		driver = webdriver.Chrome(rasta)
		driver.get("https://clubs-iiti.herokuapp.com/login")
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
			
			# Make sure this email does not already exist in music club, thus remove it
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})

			driver.get("https://clubs-iiti.herokuapp.com/clubs/music")
			apply_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '//*[@id="body-top"]/header/div/a'))
			)
			apply_button.send_keys(Keys.RETURN)

			self.assertTrue(
				'Club Head will decide further....Hope for the best!' in driver.page_source)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()

	def test_7_unregister_button(self):
		print("Checking Unregister Button")
		driver = webdriver.Chrome(rasta)
		driver.maximize_window()
		driver.get("https://clubs-iiti.herokuapp.com/login")

		try:
			input_field = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '//*[@id="identifierId"]'))
			)

			input_field.send_keys(email_user)
			input_field.send_keys(Keys.RETURN)
			password_field = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
			)

			password_field.send_keys(password_user)
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
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()

	def test_8_register_button(self):
		print("Testing Initial Registeration")
		driver = webdriver.Chrome(rasta)
		driver.get("http://localhost:5000/login")

		try:
			input_field = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '//*[@id="identifierId"]'))
			)
			requests.post("http://localhost:5000/mysql", data={"q": "DELETE FROM students WHERE Mail_Id = '{}';".format(email_user), "pwd": secret_key})
			input_field.send_keys(email_user)
			input_field.send_keys(Keys.RETURN)
			password_field = WebDriverWait(driver, 20).until(
				EC.presence_of_element_located(
					(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
			)

			password_field.send_keys(password_user)
			password_field.send_keys(Keys.RETURN)


			PhoneNo = WebDriverWait(driver, 20).until(
				EC.presence_of_element_located(
					(By.XPATH, '//*[@id="phone_no"]'))
			)
			PhoneNo.send_keys("8823986121")

			linkedin = WebDriverWait(driver, 20).until(
				EC.presence_of_element_located(
					(By.XPATH, '//*[@id="linkedin"]'))
			)
			linkedin.send_keys("mehtasomya.com")

			BIO = WebDriverWait(driver, 20).until(
				EC.presence_of_element_located(
					(By.XPATH, '//*[@id="Bio"]'))
			)
			BIO.send_keys("The Pessimist Sees")

			submit = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
				(By.XPATH, '//*[@id="body-top"]/div[2]/form/button')))
			submit.send_keys(Keys.RETURN)
			self.assertTrue('Successfully signed in' in driver.page_source)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()