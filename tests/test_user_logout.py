from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import ExistingUserData


class TestUserLogout:
    def test_user_logout(self, driver):
        exist_email = ExistingUserData.exist_email
        exist_password = ExistingUserData.exist_password

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        input_email = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        input_email.send_keys(exist_email)

        input_password = driver.find_element(*Locators.INPUT_PASSWORD)
        input_password.send_keys(exist_password)

        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
        submit_button.click()

        logout_button = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()

        user_name = driver.find_element(*Locators.USER_NAME)
        avatar = driver.find_element(*Locators.AVATAR)

        login_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

        assert user_name != True
        assert avatar != True
        assert login_button.is_displayed()
