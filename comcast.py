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

class Chrome_Xfinity(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_1_create_account(self):
        driver = self.driver

        driver.get(H.Xfinity_URL)
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        print("____________Positive_test________Create_new_ID_________")
        # Time Delay 1-3s
        H.delay1_3()
        # Check API with library request
        H.check_api(driver)
        # Check Title on the main Page
        H.assert_title(driver, 'Internet, TV, Phone, Smart Home and Security - Xfinity')
        # Check the Main Page is present
        H.main_page(driver)
        # Click on Account icon
        H.account_icon(driver)
        # Test FAIL and i will try to explain, first off when i tried to do manual and create account, i couldn't
        # I'm always got a wrong message
        print("__________________Test_1_is_failed_user_not_able_to_create_new_account_____________")

    def test_2_Internet_overview(self):
        driver = self.driver
        driver.get(H.Xfinity_URL)
        wait = WebDriverWait(driver, 10)
        print("____________Positive_test________Check_Policy_________")
        # Time Delay 1-3s
        H.delay1_3()
        # Check API with library request
        H.check_api(driver)
        # verify title on the main page
        H.assert_title(driver, 'Internet, TV, Phone, Smart Home and Security - Xfinity')
        # Check the Main Page is present
        H.main_page(driver)
        # Move to Footer use action library
        H.scroll_to_internet(driver)
        # Verify button "Customer Guarantee" visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Customer Guarantee"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Customer Guarantee"]')))
        # Click on "Customer Guarantee"
        driver.find_element(By.XPATH, '//*[text()="Customer Guarantee"]').click()
        time.sleep(2)
        # check title on "corporate.comcast.com" website
        H.assert_title(driver, 'Customer Experience')
        # Check main logo on comcast website
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="cc-main-nav-bar"]')))
        assert ' Putting the Customer at the Center of Everything We Do' in driver.page_source
        # time.sleep(3)
        # Scroll to "Learn More About Xfinity Services and Our Response to Coronavirus"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH,
                            '//*[text()=" Putting the Customer at the Center of Everything We Do"]'))
        # Verify that element visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='e-cta-button ']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='e-cta-button ']")))
        # click on button "Learn More About Xfinity Services and Our Response to Coronavirus"
        driver.find_element(By.XPATH, "//a[@class='e-cta-button ']").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        # Check Title
        H.assert_title(driver, 'Stay Connected for Remote Work and Distance Learning - Xfinity')
        # verify that text present on the page
        assert "Xfinity's Commitment to Keeping You Connected" in driver.page_source
        # Check "Stores & Tech Visits"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Stores & Tech Visits"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Stores & Tech Visits"]')))
        # Click on "Stores & Tech Visits"
        driver.find_element(By.XPATH, '//*[text()="Stores & Tech Visits"]').click()
        time.sleep(2)
        # verify that link "Your Services" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Your Services"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Your Services"]')))
        # Click on the link "Your Services"
        driver.find_element(By.XPATH, '//*[text()="Your Services"]').click()
        time.sleep(2)
        # verify that link "Billing" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Billing"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Billing"]')))
        # Click on the link "Billing"
        driver.find_element(By.XPATH, '//*[text()="Billing"]').click()
        time.sleep(2)
        # verify that link "Community Support" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Community Support"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Community Support"]')))
        # Click on the link "Community Support"
        driver.find_element(By.XPATH, '//*[text()="Community Support"]').click()
        time.sleep(2)
        # Scroll to "Need help now?" text
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, '//*[text()="Need help now?"]'))
        # verify that "Get Support" button is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Get support"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Get support"]')))
        # verify that "Xfinity Assistant" button is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Ask Xfinity"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Ask Xfinity"]')))
        print("______________Test_Passed____________")

    def tearDown(self):
        self.driver.quit()




