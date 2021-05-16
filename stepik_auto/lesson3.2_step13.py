from selenium import webdriver
import time
import unittest

def send_link(link):
    browser = webdriver.Chrome()
    browser.get(link)

    #Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('div.first_block > .form-group.first_class > .form-control.first').send_keys("Loompa")
    input2 = browser.find_element_by_css_selector('div.first_block > .form-group.second_class > .form-control.second').send_keys("Pumpa")
    input3 = browser.find_element_by_css_selector('div.first_block > .form-group.third_class > .form-control.third').send_keys("Loompa_pumpa@pumpum.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text = browser.find_element_by_tag_name("h1").text
    return welcome_text

class TestLesson1611(unittest.TestCase):
    def test_link1(self):
        self.assertEqual(send_link("http://suninjuly.github.io/registration1.html"), 'Congratulations! You have successfully registered!', "no such element 1 ran test")

    def test_link2(self):
        self.assertEqual(send_link("http://suninjuly.github.io/registration2.html"), 'Congratulations! You have successfully registered!', "no such element 2 ran test")

if __name__ == "__main__":
    unittest.main()

