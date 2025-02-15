import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from test_locators import TestLocators
from helpers import DataHelper
from conftest import driver



class TestRegistration:

    def test_registration(self, driver):
        name = DataHelper.get_name()
        email = DataHelper.get_email(10, 20)
        password = DataHelper.get_password()

        WebDriverWait(driver, 17).until(expected_conditions.element_to_be_clickable(TestLocators.INPUT_NAME_FOR_REG))
        driver.find_element(*TestLocators.INPUT_NAME_FOR_REG).send_keys(name)
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_REG).send_keys(email)
        driver.find_element(*TestLocators.FIRST_BUTTON_NEXT).click()

        WebDriverWait(driver, 17).until(expected_conditions.element_to_be_clickable(TestLocators.INPUT_PASSWORD_FOR_REG))
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_REG).send_keys(password)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_REG_REPEAT).send_keys(password)

        driver.find_element(*TestLocators.SECOND_BUTTON_NEXT).click()

        WebDriverWait(driver, 45).until(expected_conditions.element_to_be_clickable(TestLocators.FOOTER_MISS_ADDING_CARD))

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        driver.find_element(*TestLocators.FOOTER_MISS_ADDING_CARD).click()

        WebDriverWait(driver, 25).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_NEXT_SECRET_KEY))
        driver.find_element(*TestLocators.BUTTON_NEXT_SECRET_KEY).click()

        WebDriverWait(driver, 25).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_DOWNLOAD_PASSWORD))

        action = ActionChains(driver)
        action.send_keys(Keys.ESCAPE).perform()

        driver.find_element(*TestLocators.FIRST_BUTTON_LATER).click()
        driver.find_element(*TestLocators.SECOND_BUTTON_LATER).click()

        assert driver.find_element(*TestLocators.FIELD_ID_INFO).is_displayed()
