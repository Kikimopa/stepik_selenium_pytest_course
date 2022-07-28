import math
import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe", options=chrome_options)

    yield driver
    driver.close()

 # "236896", "236897", "236898", "236899", "236903", "236904", "236905"
@pytest.mark.parametrize('url', ["236895",])
def test_get_sum(driver, url):
    text = []
    try:
        link = f"https://stepik.org/lesson/{url}/step/1"

        driver.get(link)
        answer = math.log(int(time.time()))

        driver.implicitly_wait(10)

        input_area = driver.find_element(By.TAG_NAME, "textarea")
        input_area.send_keys(str(math.log(int(time.time()))))

        driver.implicitly_wait(5)
        button = driver.find_element(By.CLASS_NAME, "submit-submission")
        button.click()

        driver.implicitly_wait(5)

        result = driver.find_element(By.CLASS_NAME, "smart-hints__hint").text

        text.append(result)

        assert result == "Correct!"

        print(text)

    except WebDriverException as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    pytest.main()
