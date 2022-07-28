from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe")

url = "http://suninjuly.github.io/explicit_wait2.html"


def click_button():
    driver.get(url=url)

    button = driver.find_element(By.ID, "book")
    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()

    driver.execute_script("window.scrollBy(0, 300);")

    x = driver.find_element(By.ID, "input_value").text
    total = str(math.log(abs(12 * math.sin(int(x)))))
    input = driver.find_element(By.ID, "answer")
    input.send_keys(total)

    button = driver.find_element(By.ID, "solve")
    button.click()


def main():
    click_button()



if __name__ == '__main__':
    main()
