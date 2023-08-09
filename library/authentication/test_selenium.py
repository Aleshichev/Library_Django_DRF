import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import environ
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))


class LoginTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(LoginTest, self).__init__(*args, **kwargs)
        self.correct_email = env("CORRECT_EMAIL")
        self.correct_password = env("CORRECT_PASSWORD")
        self.incorrect_email = env("INCORRECT_EMAIL")
        self.incorrect_password = env("INCORRECT_PASSWORD")
        self.base_url = "http://127.0.0.1:8000/"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.base_url)
        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/a[1]")
        login_button.click()
        time.sleep(2)

    def login(self, email, password):
        self.email_input = self.driver.find_element(By.ID, "id_email")
        self.password_input = self.driver.find_element(By.ID, "id_password")
        self.email_input.send_keys(email)
        self.password_input.send_keys(password)
        time.sleep(2)
        login_button = self.driver.find_element(
            By.XPATH, "/html/body/div/form/div[3]/button"
        )
        login_button.click()
        time.sleep(2)

    def test_successful_login(self):
        self.login(self.correct_email, self.correct_password)
        check_text = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Library", check_text)
        self.assertNotEqual("Llibrary", check_text)

    def test_successful_logout(self):
        self.login(self.correct_email, self.correct_password)
        logout_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/a[2]")
        logout_button.click()
        check_text = self.driver.find_element(By.TAG_NAME, "h2").text
        time.sleep(2)
        self.assertEqual("Login to your account", check_text)
        self.assertNotEqual("Logout to your account", check_text)

    def test_invalid_login(self):
        self.login(self.incorrect_email, self.incorrect_password)
        check_error_message = self.driver.find_element(By.TAG_NAME, "li").text
        time.sleep(2)
        self.assertEqual("Invalid email or password", check_error_message)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
