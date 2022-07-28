from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe")

url = "http://suninjuly.github.io/math.html"

def get_data():
    driver.get(url=url)
    driver.maximize_window()
    try:
        x = driver.find_element(By.ID,"input_value").text
        total = str(math.log(abs(12*math.sin(int(x)))))
        input = driver.find_element(By.ID, "answer")
        input.send_keys(total)
        time.sleep(3)

    except Exception as ex:
        print(ex)


def click_capcha():

    try:
        checkbox_click = driver.find_element(By.ID, "robotCheckbox")
        checkbox_click.click()
        radio_click = driver.find_element(By.ID, "robotsRule")
        radio_click.click()
        submit = driver.find_element(By.CLASS_NAME, "btn-default")
        submit.click()
        time.sleep(3)
    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()



def main():
    get_data()
    click_capcha()


if __name__ == "__main__":
    main()

