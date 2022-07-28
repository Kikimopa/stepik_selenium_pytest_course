from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe")

url = "http://suninjuly.github.io/cats.html"

def confirm():
    driver.get(url = url)
    try:
        button = driver.find_element(By.ID, "button")
        button.click()
    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

def main():
    confirm()

if __name__ == '__main__':
    main()
