from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    # Set up the Selenium WebDriver with options
    options = webdriver.ChromeOptions()
    # Comment the next line if you want to see the browser window
    options.add_argument('--headless')  # Use this if you're running headless
    # Actual path to Chrome binary (change this to the path on your machine)
    options.binary_location = '/usr/bin/google-chrome'
    # options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://apps.indiahealthlink.com/ihl_kiosk_ui_abha_old/#/welcome")
        driver.maximize_window()  # Replace with your URL
        time.sleep(20)

        # Wait for the welcome element to be present for a maximum of 15 seconds
        wait = WebDriverWait(driver, 5)
        welcome_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[40]/div[2]/div/div[2]/div[4]/div/div/div[1]')))
                                                                        
        # time.sleep(10)

        if welcome_element:
            print("Page loaded successfully")

            # click on BP test 
            click_BP_test_xpath = "//a[@id='bp_test_btn']" 
            click_BP_test = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, click_BP_test_xpath)))
            click_BP_test.click()
            time.sleep(10)
            # Wait for the Start button and click it
            start_button_xpath = '/html/body/div[40]/div[2]/div/div[2]/div[4]/div/div/a'
            start_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, start_button_xpath)))
            start_button.click()
            print("Clicked Start test")
            time.sleep(5)
            # Wait for the username text field to be present
            username_field_xpath = '/html/body/higi-modal/div[1]/div[2]/login-modal/div/div[1]/div[1]/higi-text-field/input'
            username_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, username_field_xpath)))
            time.sleep(5)
            print("Username Field Verified")

            # Enter the username "pavan.veeramaneni@indiahealthlink.com" into the username field
            username_field.send_keys("janhavi.nagarajan@indiahealthlink.com")
            time.sleep(5)
            print("Username Entered Successfully")

            # Wait for the password text field to be present
            password_field_xpath = '/html/body/higi-modal/div[1]/div[2]/login-modal/div/div[1]/div[2]/higi-text-field/input'
            password_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, password_field_xpath)))
            time.sleep(5)
            print("Password field verified")

            # Enter the password "ABCd@123456" into the password field
            password_field.send_keys("Janhavi@041")
            time.sleep(2)
            print("Password entered successfully")

            delete_button_xpath = '/html/body/keyboard/div[3]/ul/div[1]/li[11]/a'
            delete_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, delete_button_xpath)))
            delete_button.click()
            time.sleep(2)
            print("Deleted Last character from password field successfully")
            # Locate and click the submit button
            submit_button_xpath = '/html/body/higi-modal/div[1]/div[2]/login-modal/div/div[1]/div[2]/a'
            submit_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
            submit_button.click()
            time.sleep(10)
            print("Clicked submit button successfully")
            # click on close icon for last checkin result
            close_button_xpath = "(//div[@id='higi_keyboard_close_btn'])[3]"
            close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, close_button_xpath)))
            close_button.click()
            print("close icon clicked successfully")

            # Full body test BP click on continue button
            BP_button_xpath = "//a[@class='bp_warning_modal_box_button_continue']"
            BP_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, BP_button_xpath)))
            BP_button.click()
            print("Clicked continue button successfully")
            time.sleep(10)
            # Start test button
            start_button_xpath = "//a[@class='global_continue_next_button ng-scope button-enter-right']"
            start_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, start_button_xpath)))
            start_button.click()
            print("Clicked on Start Test button")
            time.sleep(25)
            # click on final result page
            finalresult_button_xpath = "//a[@class='global_continue_next_button ng-scope button-enter-right']"
            finalresult_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, finalresult_button_xpath)))
            finalresult_button.click()
            print("final result page clicked successfully")
            time.sleep(15)

            # Click on email result
            emailresult_button_xpath = "//a[@class='global_continue_next_button no-print ng-scope button-enter-right']"
            emailresult_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, emailresult_button_xpath)))
            emailresult_button.click()
            print("email result clicked successfully")
            # click on send button
            sendmail_button_xpath = "//div[@class='email_my_results_submit_button  email_my_results_submit_active_btn']"
            sendmail_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, sendmail_button_xpath)))
            sendmail_button.click();
            print("Email sent successfully")
            time.sleep(10)
            # Click on logout button
            logout_button_xpath = "//div[@class='global_logout_button exit_logout_enabled']"
            logout_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, logout_button_xpath)))
            logout_button.click()
            time.sleep(5)
            print("clicked logged out successfully")
            # final logout button
            final_logout_xpath = "//div[@id='exit_confirm_confirm_btn']"
            final_logout = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, final_logout_xpath)))
            final_logout.click()
            print("Logged out successfully")

        else:
            print("Page not loaded")

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
