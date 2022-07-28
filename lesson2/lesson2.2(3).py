import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe")

url = "http://suninjuly.github.io/selects2.html"



def click_button():
    try:
        driver.get(url=url)
        driver.maximize_window()

        num1 = driver.find_element(By.ID, "num1").text
        num2 = driver.find_element(By.ID, "num2").text
        total = str(int(num1) + int(num2))

        select = Select(driver.find_element(By.TAG_NAME, "select"))
        select.select_by_value(total)

        submit = driver.find_element(By.CLASS_NAME, "btn-default")
        submit.click()

        time.sleep(10)

    except Exception as ex:
        print(ex)

    finally:
       driver.close()
       driver.quit()


def main():

    click_button()

if __name__ == "__main__":
    main()