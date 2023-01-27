import random

import requests

import helpers as H
from selenium import webdriver
from  selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException, \
    ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
from faker import Faker
faker_class = Faker()
F = Faker()
F.Number = Faker(["en_CA"])









# URL for Xfinity
Xfinity_URL = 'https://www.xfinity.com/overview?INTCMP=ILC:MA:GEN:GEN5b9ab8ad1e540'
# Main Logo
MAIN_page = '//*[@class="media-image full-image-full-fill full-image-large-full \
                md:full-image-large-half md:absolute md:w-full md:h-full"]'

# Account icon
accountIcon = '//*[@aria-label="Account" and @type="button"]'
# overview button
overview_btnk = '//*[@href="https://www.xfinity.com/learn/internet-service"]'
# Internet button
internet_btnk = 'Internet'

#  Time Delay from 1 - 3
def delay1_3():
    time.sleep(random.randint(1, 3))

def delay1_5():
    time.sleep(random.randint(1, 5))


# Check API func()
def check_api(driver):
    code = requests.get(driver.current_url).status_code
    if code == 200:
        print(f'Url has, {requests.get(driver.current_url).status_code}')
    else:
        print("API response code is NOT 200")

# Assert Title
def assert_title(driver, title):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print(f"Page has, {driver.title} as Page title")
    # Scr of page if page has different title
    driver.get_screenshot_as_file(f"Page has different {title}.png")
    if not title in driver.title:
        raise Exception(f"Page {title} has wrong title")

# Check main Logo
def main_page(driver):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, MAIN_page)))
        print("Logo is present on the main page")
    except TimeoutException:
        print('Logo in NOT present on the main page')
        driver.get_screenshot_as_file("Page has different LOGO.png")

# Move to el footer -> "Policy"
def scroll_to_internet(driver):
    footer = driver.find_element(By.XPATH,
        '//*[@class="xc-flex xc-m-auto xc-max-w-[700px] xl:xc-max-w-none xc-flex-wrap xc-justify-center xc-items-center xc-list-none xc-p-0"]')
    actions = ActionChains(driver)
    actions.move_to_element(footer).perform()








# Click on Account icon
def account_icon(driver):
    wait = WebDriverWait(driver, 10)
    # icon
    wait.until(EC.visibility_of_element_located((By.XPATH, accountIcon)))
    wait.until(EC.element_to_be_clickable((By.XPATH, accountIcon)))
    driver.find_element(By.XPATH, accountIcon).click()
    # verify that "sing up" button is present and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Sign In"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Sign In"]')))
    # Click on "sign up button"
    driver.find_element(By.XPATH, '//*[text()="Sign In"]').click()
    # verify Title on the page
    assert_title(driver, "Sign in to Xfinity")
    # Text Sign in with your Xfinity ID is present on the page
    assert 'Sign in with your Xfinity ID' in driver.page_source
    # Verify that "Create a new Xfinity ID" is present and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Create a new Xfinity ID"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Create a new Xfinity ID"]')))
    # Click on "Create a new Xfinity ID"
    driver.find_element(By.XPATH, '//*[text()="Create a new Xfinity ID"]').click()
    # Verify that user's used Mobile for create account
    wait.until(EC.visibility_of_element_located((By.ID, 'mobileMethod_radio')))
    wait.until(EC.element_to_be_clickable((By.ID, 'mobileMethod_radio')))
    # click on radio button
    driver.find_element(By.ID, 'mobileMethod_radio').click()
    # verify "Continue" button
    wait.until(EC.visibility_of_element_located((By.NAME, '_eventId')))
    wait.until(EC.element_to_be_clickable((By.NAME, "_eventId")))
    # click on "continue" button
    driver.find_element(By.NAME, "_eventId").click()


    # First off I did some code, but unfortunately website is pretty secured and not allow me to go forward!
    # in code below I tried to use Faker library for input number
    '''
    # wait for results to be visible
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".list-recent-events li")))
    # verify that user on the right page
    # "Enter the mobile phone number on your account" is present
    assert 'Enter the mobile phone number on your account' in driver.page_source
    # verify that placeholder is present and clickable
    wait.until(EC.visibility_of_element_located((By.ID, 'mobilePhoneNumber')))
    wait.until(EC.element_to_be_clickable((By.ID, 'mobilePhoneNumber')))
    # click on placeholder
    driver.find_element(By.ID, 'mobilePhoneNumber').click()
    # clear placeholder
    driver.find_element(By.ID, "mobilePhoneNumber").clear()
    # Enter number use Faker Library
    driver.find_element(By.ID, 'mobilePhoneNumber').send_keys(F.Number.phone_number())
    time.sleep(3)'''
