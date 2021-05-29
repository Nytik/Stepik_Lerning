import pytest
import math
import time
from selenium import webdriver

answer = math.log(int(time.time()))
code_link = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('code', code_link)
def test_guest_should_see_login_link(browser, code):
    link = f"https://stepik.org/lesson/{code}/step/1"
    browser.get(link)
    # textarea = browser.find_element_by_css_selector("#ember85")
    # textarea.send_keys(answer)
    # button = browser.find_element_by_css_selector(".submit-submission")
    # button.click()

