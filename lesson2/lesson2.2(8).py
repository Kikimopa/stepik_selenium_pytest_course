from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe")

url = "http://suninjuly.github.io/file_input.html"


def get_data():
    driver.get(url=url)
    driver.maximize_window()
    try:
        first_name = driver.find_element(By.NAME, "firstname")
        first_name.send_keys("Pupok")

        last_name = driver.find_element(By.NAME, "lastname")
        last_name.send_keys("Zhopik")

        email = driver.find_element(By.NAME, "email")
        email.send_keys("Pupok@ksadj.ru")

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_dir = os.path.join(current_dir, "1.txt")

        file = driver.find_element(By.ID, "file")
        file.send_keys(file_dir)

        button = driver.find_element(By.TAG_NAME, "button")
        button.click()
        time.sleep(3)


    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


def main():
    get_data()



if __name__ == "__main__":
    main()

