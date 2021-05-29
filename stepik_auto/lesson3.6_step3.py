import pytest
import math
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def links():
    l = "https://stepik.org/lesson/236895/step/1" \
        "https://stepik.org/lesson/236896/step/1" \
        "https://stepik.org/lesson/236897/step/1" \
        "https://stepik.org/lesson/236898/step/1" \
        "https://stepik.org/lesson/236899/step/1" \
        "https://stepik.org/lesson/236903/step/1" \
        "https://stepik.org/lesson/236904/step/1" \
        "https://stepik.org/lesson/236905/step/1"
    l_split = l.split()
    for i in l_split:
        print(i)