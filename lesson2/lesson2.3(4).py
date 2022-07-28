from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe")

url = "http://suninjuly.github.io/alert_accept.html"

def confirm():
    driver.get(url = url)

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    confirm = driver.switch_to.alert
    confirm.accept()

def set_capha():
    try:
        x = driver.find_element(By.ID, "input_value").text
        total = str(math.log(abs(12 * math.sin(int(x)))))
        input = driver.find_element(By.ID, "answer")
        input.send_keys(total)

        button = driver.find_element(By.TAG_NAME, "button")
        button.click()

        time.sleep(3)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

def main():
    confirm()
    set_capha()

if __name__ == "__main__":
    main()