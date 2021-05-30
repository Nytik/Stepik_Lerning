import pytest
import math
import time
from selenium import webdriver

text = ''
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(text)

class TestLogin:
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
        global text
        browser.get(links)
        time.sleep(3)
        textarea = browser.find_element_by_css_selector('[placeholder="Напишите ваш ответ здесь..."]')
        textarea.send_keys(str(math.log(int(time.time()))))
        button = browser.find_element_by_css_selector('.submit-submission')
        button.click()
        time.sleep(3)
        correct = browser.find_element_by_css_selector('.smart-hints__hint').text
        try:
            assert "Correct!" in correct
        except:
            text += correct






