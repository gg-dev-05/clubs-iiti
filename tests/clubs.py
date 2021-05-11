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


	# def test_join_button_visible_kalakriti(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/kalakriti")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on kalakriti page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()

	# def test_join_button_visible_dance(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/dance")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on dance page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()   

	# def test_join_button_visible_dramatics(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/dramatics")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on dramatics page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()

	# def test_join_button_visible_music(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/music")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on music page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()  

	# def test_join_button_visible_mystic_hues(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/mystic_hues")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on mystic_hues page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()   

	# def test_join_button_visible_quiz(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/quiz")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on quiz page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()  


	# def test_join_button_visible_debsoc(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/debsoc")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on debsoc page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()  

	# def test_join_button_visible_avana(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/avana")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on avana page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()    

	# def test_join_button_visible_srijanClub(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/srijanClub")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on srijanClub page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()    

	# def test_join_button_visible_progClub(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/progClub")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on progClub page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()   

	# def test_join_button_visible_robotics(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/robotics")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on robotics page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()    

	# def test_join_button_visible_concreate(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/concreate")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on concreate page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()    

	# def test_join_button_visible_cae(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/cae")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on cae page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()    

	# def test_join_button_visible_astronomy(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/astronomy")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on astronomy page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()    

	# def test_join_button_visible_electronics(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/electronics")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on electronics page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()  

	# def test_join_button_visible_aeromodelling(self):
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/aeromodelling")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on aeromodelling page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()    

	# def test_join_button_visible_dsc(self):
	# 	print("Checking DSC club")
	# 	driver = webdriver.Chrome(rasta)
	# 	driver.get("https://clubs-iiti.herokuapp.com/login")
	# 	try:
	# 		input_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="identifierId"]'))
	# 		)
	# 		input_field.send_keys(email)
	# 		input_field.send_keys(Keys.RETURN)

	# 		password_field = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
	# 		)
	# 		password_field.send_keys(password)
	# 		password_field.send_keys(Keys.RETURN)
	# 		requests.post("https://clubs-iiti.herokuapp.com/mysql", data={"q": "DELETE FROM clubmembers WHERE Mail_Id = '{}';".format(email), "pwd": secret_key})
	# 		driver.get("https://clubs-iiti.herokuapp.com/clubs/dsc")
	# 		join_button = WebDriverWait(driver, 10).until(
	# 			EC.presence_of_element_located(
	# 				(By.XPATH, '/html/body/header/div/a'))
	# 		)
	# 		join_button.send_keys(Keys.RETURN)
	# 		print("Join Button visibility on dsc page")
	# 	except Exception as e:
	# 		print("Test Case Failed")
	# 		print(e)
	# 		driver.quit()
	# 		exit()       