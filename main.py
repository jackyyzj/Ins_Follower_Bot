from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = ""
PASSWORD = ""


class InstaFollower:
	def __init__(self):
		self.driver = driver = webdriver.Chrome()

	def login(self):
		self.driver.get("https://www.instagram.com/accounts/login/")
		self.driver.maximize_window()
		time.sleep(20)

		username_fill = self.driver.find_element(By.NAME, "username")
		password_fill = self.driver.find_element(By.NAME, "password")

		username_fill.send_keys(USERNAME)
		password_fill.send_keys(PASSWORD)

		time.sleep(15)

		login = self.driver.find_element(By.XPATH, '// *[ @ id = "loginForm"] / div / div[3] / button')
		login.click()

		time.sleep(20)

		save_info = self.driver.find_element(By.XPATH, '/ html / body / div[2] / div / div / div[2] / div / div / div / div[1] / div[1] / div[2] / section / main / div / div / div / section / div / button')
		save_info.click()

		time.sleep(20)

		turn_notification = self.driver.find_element(By.XPATH, '/ html / body / div[2] / div / div / div[3] / div / div / div[1] / div / div[2] / div / div / div / div / div[2] / div / div / div[3] / button[1]')
		turn_notification.click()

		time.sleep(5)

	def find_followers(self):
		time.sleep(5)
		self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
		self.driver.maximize_window()
		time.sleep(15)

		followers = self.driver.find_element(By.XPATH,
			'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
		followers.click()

		time.sleep(20)

		bar = self.driver.find_element(By.XPATH, '/ html / body / div[2] / div / div / div[3] / div / div / div[1] / div / div[2] / div / div / div / div / div[2] / div / div / div[3]')

		for i in range(10):
			self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", bar)
			time.sleep(10)

	def follow(self):
		all_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div._aano  button._acan._acap._acas._aj1-')
		for button in all_buttons:
			try:
				button.click()
				time.sleep(5)
			except ElementClickInterceptedException:
				cancel_button = self.driver.find_element(By.CSS_SELECTOR, 'button._a9--._a9_1')
				cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
