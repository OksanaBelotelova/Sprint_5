from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from helpers import random_email
from data import ExistingUserData


class TestUserRegistration:
    def test_user_registration(self, driver):
        email = random_email()
        password = ExistingUserData.standart_password

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        no_account_button = driver.find_element(*Locators.NO_ACCOUNT_BUTTON)
        no_account_button.click()

        input_email = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        input_email.send_keys(email)

        input_password = driver.find_element(*Locators.INPUT_PASSWORD)
        input_password.send_keys(password)

        confirm_password = driver.find_element(*Locators.INPUT_CONFIRM_PASSWORD)
        confirm_password.send_keys(password)

        create_account = driver.find_element(*Locators.CREATE_ACCOUNT)
        create_account.click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.AVATAR))

        user_name = driver.find_element(*Locators.USER_NAME)
        avatar = driver.find_element(*Locators.AVATAR)
        
        #здесь есть баг - редиректа на главную страницу не происходит
        assert driver.current_url == 'https://qa-desk.stand.praktikum-services.ru' 
        assert avatar.is_displayed()
        assert user_name.is_displayed()

    def test_user_registration_with_incorrect_email(self, driver):

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        no_account_button = driver.find_element(*Locators.NO_ACCOUNT_BUTTON)
        no_account_button.click()

        input_email = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        input_email.send_keys("Incorrectemail")

        create_account = driver.find_element(*Locators.CREATE_ACCOUNT)
        create_account.click()

        error_message = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.ERROR_MESSAGE))
        input_email_wrapper = driver.find_element(*Locators.INPUT_PASSWORD_WRAPPER)
        input_password_wrapper = driver.find_element(*Locators.INPUT_PASSWORD_WRAPPER)
        input_confirm_passowrd_wrapper = driver.find_element(*Locators.INPUT_CONFIRM_PASSWORD_WRAPPER)
        
       
        assert error_message.is_displayed()
        assert input_email_wrapper.value_of_css_property('border') == '1px solid rgb(255, 105, 114)'
        assert input_password_wrapper.value_of_css_property('border') == '1px solid rgb(255, 105, 114)'
        assert input_confirm_passowrd_wrapper.value_of_css_property('border') == '1px solid rgb(255, 105, 114)'

    def test_user_registration_already_existing_user(self, driver):
        exist_email = ExistingUserData.exist_email
        exist_password = ExistingUserData.exist_password

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        no_account_button = driver.find_element(*Locators.NO_ACCOUNT_BUTTON)
        no_account_button.click()

        input_email = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        input_email.send_keys(exist_email)

        input_password = driver.find_element(*Locators.INPUT_PASSWORD)
        input_password.send_keys(exist_password)

        confirm_password = driver.find_element(*Locators.INPUT_CONFIRM_PASSWORD)
        confirm_password.send_keys(exist_password)

        create_account = driver.find_element(*Locators.CREATE_ACCOUNT)
        create_account.click()
       
        error_message = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ERROR_MESSAGE))
        input_email_wrapper = driver.find_element(*Locators.INPUT_PASSWORD_WRAPPER)
        input_password_wrapper = driver.find_element(*Locators.INPUT_PASSWORD_WRAPPER)
        input_confirm_passowrd_wrapper = driver.find_element(*Locators.INPUT_CONFIRM_PASSWORD_WRAPPER)
        
       
        assert error_message.is_displayed()
        assert input_email_wrapper.value_of_css_property('border') == '1px solid rgb(255, 105, 114)'
        assert input_password_wrapper.value_of_css_property('border') == '1px solid rgb(255, 105, 114)'
        assert input_confirm_passowrd_wrapper.value_of_css_property('border') == '1px solid rgb(255, 105, 114)'