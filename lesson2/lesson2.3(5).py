from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe")

url = "http://suninjuly.github.io/redirect_accept.html"

def confirm():
    driver.get(url = url)

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

def window_switch():
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

def set_capha():
    try:
        x = driver.find_element(By.ID, "input_value").text
        total = str(math.log(abs(12 * math.sin(int(x)))))
        input = driver.find_element(By.ID, "answer")
        input.send_keys(total)

        button = driver.find_element(By.TAG_NAME, "button")
        button.click()


    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

def main():
    confirm()
    window_switch()
    set_capha()

if __name__ == "__main__":
    main()