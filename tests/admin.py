import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from secret import email, password, rasta, secret_key, email_user, password_user
import requests
class FlaskAdminTestCase(unittest.TestCase):
	def test_1_club_admim_login(self):
		print("Checking If Club Admin is able to sign in")
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
			self.assertTrue('Successfully signed in as' in driver.page_source)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()

	def test_2_details_visibility_to_non_admin_users(self):
		print("Checking visibility of details to non admin users")
		driver = webdriver.Chrome(rasta)
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
			WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
			)
			self.assertTrue('Successfully signed in as' in driver.page_source)
			driver.get("https://clubs-iiti.herokuapp.com/clubs/progClub")
			member_name = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '//*[@id="members"]/div/div[2]/table/tbody/tr[2]/td[1]/a'))
			)
			member_name.send_keys(Keys.RETURN)
			WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '//*[@id="body-top"]/div[1]/p[1]'))
			)
			self.assertTrue('Not Allowed' in driver.page_source)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()

	def test_3_check_apply_functionality(self):
		print("Checking Apply Functionality")
		driver = webdriver.Chrome(rasta)
		driver.get("https://clubs-iiti.herokuapp.com/login")
		try:
			# send request to join club
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email_user), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email_user), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/cinephiles")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)

			driver.quit()
			
			# Sign in using admin credentials 
			driver = webdriver.Chrome(rasta)
			driver.get("https://clubs-iiti.herokuapp.com/login")

			# Sign in using admin credentials 
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

			# Wait for sign in to complete
			WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div[2]/h1'))
			)

			driver.get("https://clubs-iiti.herokuapp.com/clubs/cinephiles")
			approve_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/section[4]/div/div[2]/table/tbody/tr[2]/td[3]/a[1]'))
			)
			approve_button.send_keys(Keys.RETURN)

			# Wait for page to complete load
			WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/h1'))
			)
			self.assertTrue('Cinephiles Club' in driver.title)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()


	def test_4_check_reject_functionality(self):
		print("Checking Reject Functionality")
		driver = webdriver.Chrome(rasta)
		driver.get("https://clubs-iiti.herokuapp.com/login")
		try:
			# send request to join club
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email_user), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email_user), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/cinephiles")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)

			driver.quit()

			# Sign in using admin credentials 
			driver = webdriver.Chrome(rasta)
			driver.get("https://clubs-iiti.herokuapp.com/login")

			# Sign in using admin credentials 
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

			# Wait for sign in to complete
			WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div[2]/h1'))
			)

			driver.get("https://clubs-iiti.herokuapp.com/clubs/cinephiles")
			reject_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/section[4]/div/div[2]/table/tbody/tr[2]/td[3]/a[2]'))
			)
			reject_button.send_keys(Keys.RETURN)

			# Wait for page to complete load
			WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/h1'))
			)
			self.assertTrue('Cinephiles Club' in driver.title)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()

	def test_5_check_schedule_functionality(self):
		print("Checking Interview Schedule Success")
		driver = webdriver.Chrome(rasta)
		driver.get("https://clubs-iiti.herokuapp.com/login")
		try:

			# send request to join club
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email_user), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email_user), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/cinephiles")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)

			driver.quit()
			
			# Sign in using admin credentials 
			driver = webdriver.Chrome(rasta)
			driver.get("https://clubs-iiti.herokuapp.com/login")
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
					(By.XPATH, '/html/body/header/div[2]/h1'))
			)

			driver.get("https://clubs-iiti.herokuapp.com/clubs/cinephiles")
			schedule_button= WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '//*[@id="members"]/div/div[2]/table/tbody/tr[2]/td[3]/a[3]'))
			)
			schedule_button.send_keys(Keys.RETURN)
			self.assertTrue('Schedule interview' in driver.page_source)
			print("Test success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()
			
	def test_non_iiti_email(self):
		print("Testing  for non iiti email id")
		driver = webdriver.Chrome(rasta)
		driver.get("https://clubs-iiti.herokuapp.com/login")
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


			WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/h1'))
			)
			self.assertTrue('Please use IITI email id' in driver.page_source)
			print("Tested for non iiti email id")
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()