from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe")

url = "http://SunInJuly.github.io/execute_script.html"


def get_data():
    driver.get(url=url)
    driver.maximize_window()
    try:
        x = driver.find_element(By.ID, "input_value").text
        total = str(math.log(abs(12 * math.sin(int(x)))))
        input = driver.find_element(By.ID, "answer")
        input.send_keys(total)


    except Exception as ex:
        print(ex)


def click_capcha():

    try:

        checkbox_click = driver.find_element(By.ID, "robotCheckbox")
        checkbox_click.click()

        driver.execute_script("window.scrollBy(0, 100);")
        radio_click = driver.find_element(By.ID, "robotsRule")
        radio_click.click()
        submit = driver.find_element(By.TAG_NAME, "button")
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

