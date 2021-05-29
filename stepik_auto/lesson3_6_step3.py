import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestLogin:
    text = ''
    cl = ['https://stepik.org/lesson/236895/step/1',
          'https://stepik.org/lesson/236896/step/1',
          'https://stepik.org/lesson/236897/step/1',
          'https://stepik.org/lesson/236898/step/1',
          'https://stepik.org/lesson/236899/step/1',
          'https://stepik.org/lesson/236903/step/1',
          'https://stepik.org/lesson/236904/step/1',
          'https://stepik.org/lesson/236905/step/1']

    @pytest.mark.parametrize('links', cl)
    def test_guest_should_see_login_link(self, browser, links):
        browser.get(links)
        time.sleep(10)
        textarea = browser.find_element_by_css_selector('//*[@placeholder="Напишите ваш ответ здесь..."]')
        textarea.send_key(str(math.log(int(time.time()))))
        #button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '.submit-submission')))
        #button.click()


