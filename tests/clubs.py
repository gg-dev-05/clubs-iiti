import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from secret import rasta, email_user, password_user, email, password, secret_key
import requests

class FlaskClubsTestCase(unittest.TestCase):

	def test_9_join_button_visible_literaray(self):
		print("Join Literary Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/literary")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()

	def test_10_join_button_visible_cinephiles(self):
		print("Join Cinephiles Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/cinephiles")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()


	def test_11_join_button_visible_kalakriti(self):
		print("Join kalakriti Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/kalakriti")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()

	def test_12_join_button_visible_dance(self):
		print("Join dance Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/dance")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()

	def test_13_join_button_visible_dramatics(self):
		print("Join dramatics Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/dramatics")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()

	def test_14_join_button_visible_music(self):
		print("Join music Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/music")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()

	def test_15_join_button_visible_mystic_hues(self):
		print("Join mystic_hues Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/mystic_hues")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()	

	def test_16_join_button_visible_quiz(self):
		print("Join quiz Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/quiz")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()	

	def test_17_join_button_visible_debsoc(self):
		print("Join debsoc Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/debsoc")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()						

	def test_18_join_button_visible_avana(self):
		print("Join avana Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/avana")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()	
	



	def test_19_join_button_visible_srijanClub(self):
		print("Join srijanClub Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/srijanClub")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()	

	def test_20_join_button_visible_progClub(self):
		print("Join progClub Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/progClub")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()			


	def test_21_join_button_visible_robotics(self):
		print("Join robotics Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/robotics")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()	
 
	def test_22_join_button_visible_concreate(self):
		print("Join concreate Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/concreate")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()	
 
	def test_23_join_button_visible_cae(self):
		print("Join cae Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/cae")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()	
 
	def test_24_join_button_visible_astronomy(self):
		print("Join astronomy Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/astronomy")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()	


	def test_25_join_button_visible_electronics(self):
		print("Join electronics Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/electronics")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()	

	def test_26_join_button_visible_aeromodelling(self):
		print("Join aeromodelling Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/aeromodelling")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()			



	def test_27_join_button_visible_dsc(self):
		print("Join dsc Club Test")
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
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM approvals WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
			driver.get("https://clubs-iiti.herokuapp.com/clubs/dsc")
			join_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located(
					(By.XPATH, '/html/body/header/div/a'))
			)
			join_button.send_keys(Keys.RETURN)
			print("Test Success")
			driver.quit()
		except Exception as e:
			print("Test Case Failed")
			print(e)
			driver.quit()
			exit()			

     