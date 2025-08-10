from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import get_existing_user_data


class TestCreateAdvertisement:
    def test_create_advertisement_unlogged_user_(self, driver):

        create_advertisement = driver.find_element(*Locators.CREATE_ADVERTISEMENT)
        create_advertisement.click()

        message = driver.find_element(*Locators.MESSAGE_POPUP)

        assert message.is_displayed() is True

    def test_create_advertisement_logged_user_(self, driver):
        exist_email, exist_password = get_existing_user_data()

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        input_email = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        input_email.send_keys(exist_email)

        input_password = driver.find_element(*Locators.INPUT_PASSWORD)
        input_password.send_keys(exist_password)

        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
        submit_button.click()

        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(Locators.AVATAR))

        add_advertisement = driver.find_element(*Locators.ADD_ADVERTISEMENT)
        add_advertisement.click()

        name_field = driver.find_element(*Locators.NAME_FIELD)
        name_field.send_keys('Букварь')

        description_field = driver.find_element(*Locators.DESCRIPTION_FIELD)
        description_field.send_keys('Книга, чтобы научиться читать')

        price_field = driver.find_element(*Locators.PRICE_FIELD)
        price_field.send_keys('1000')

        radio_button = driver.find_element(*Locators.RADIO_BUTTON)
        radio_button.click()

        category = driver.find_element(*Locators.CATEGORY)
        category.click()

        choose_category = driver.find_element(*Locators.CHOOSE_CATEGORY)
        choose_category.click()

        city = driver.find_element(*Locators.CITY)
        city.click()

        choose_city = driver.find_element(*Locators.CHOOSE_CITY)
        choose_city.click()

        publish_button = driver.find_element(*Locators.PUBLISH_BUTTON)
        publish_button.click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.APPLY_BUTTON))

        avatar = driver.find_element(*Locators.AVATAR)

        avatar.click()

        my_advertisement = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MY_ADVERTISEMENTS))

        assert my_advertisement.is_displayed() is True
