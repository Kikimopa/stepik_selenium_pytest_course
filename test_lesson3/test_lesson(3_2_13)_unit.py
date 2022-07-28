import unittest
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class TestSuite(unittest.TestCase):
    def test_number_one(self):
        driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe")
        driver.get("http://suninjuly.github.io/registration1.html")

        first_name = driver.find_element(By.CLASS_NAME, "first")
        first_name.send_keys("First name")

        second_name = driver.find_element(By.CLASS_NAME, "second")
        second_name.send_keys("Second name")

        email = driver.find_element(By.CLASS_NAME, "third")
        email.send_keys("email")

        submit = driver.find_element(By.TAG_NAME, "button")
        submit.click()

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Succsesfull")

    def test_number_two(self):
        driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe")
        driver.get("http://suninjuly.github.io/registration2.html")

        for item in ['first', 'second', 'third']:
            elements = driver.find_elements(By.CSS_SELECTOR, f'input.form-control.{item}[required]')
            if not elements:
                raise NoSuchElementException
            for element in elements:
                element.send_keys("Мой ответ")

        button = driver.find_element(By.TAG_NAME, "button")
        button.click()

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Succsesfull")


if __name__ == "__main__":
    pytest.main()
