from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import get_existing_user_data

class TestUserLogin:

    def test_login_exist_user(self,driver):
        exist_email, exist_password = get_existing_user_data()

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        input_email = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        input_email.send_keys(exist_email)

        input_password = driver.find_element(*Locators.INPUT_PASSWORD)
        input_password.send_keys(exist_password)

        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
        submit_button.click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.AVATAR))
        
        user_name = driver.find_element(*Locators.USER_NAME)
        avatar = driver.find_element(*Locators.AVATAR)

        # здесь есть баг - редиректа на главную страницу непроисходит
        assert driver.current_url == 'https://qa-desk.stand.praktikum-services.ru' 
        assert avatar.is_displayed() is True
        assert user_name.is_displayed() is True
        

