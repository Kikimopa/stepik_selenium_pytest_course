import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


@pytest.mark.parametrize('url', ["236895", "236896", ])
class TestLogin:
    def test_guest_should_see_login_link(self, driver, url):
        text = ''
        link = f"https://stepik.org/lesson/{url}/step/1"
        driver.get(link)
        driver.implicitly_wait(10)

        input_area = driver.find_element(By.TAG_NAME, "textarea")
        input_area.send_keys(str(math.log(int(time.time()))))

        driver.implicitly_wait(5)
        button = driver.find_element(By.CLASS_NAME, "submit-submission")
        button.click()

        driver.implicitly_wait(5)

        result = driver.find_element(By.CLASS_NAME, "smart-hints__hint").text

        assert result == "Correct!", 'Sucsessfull'
        text += result
        print(text)


if __name__ == "__main__":
    pytest.main()