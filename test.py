from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # Set up the Selenium WebDriver with options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Use this if you're running headless
    options.binary_location = '/usr/bin/google-chrome'  # Actual path to Chrome binary
    driver = webdriver.Chrome(options=options)
    try:
        # Open the login page
        driver.get("http://172.171.252.63/")

        # Find and interact with the email input field using its XPath
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="tab1"]/form/div[1]/input'))
        )
        email_input.send_keys("pavan.veeramaneni@indiahealthlink.com")

        # Find and interact with the password input field using its XPath
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="tab1"]/form/div[2]/input'))
        )
        password_input.send_keys("ABCd@123456")

        # Find and click the login button using the provided XPath
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tab1"]/form/div[3]/button'))
        )
        login_button.click()

        # You can add a delay here to wait for the page to load and check for login success
        # For example, sleep for a few seconds:
        import time
        time.sleep(5)  # Adjust the sleep time as needed

        # Check if the page URL has changed, indicating a successful login
        if driver.current_url == "URL_AFTER_LOGIN_SUCCESS":
            print("Test passed! Username and password are correct.")
        else:
            print("Test failed! Username or password is incorrect.")

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
