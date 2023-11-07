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

        # Fill in the username and password fields with valid values
        username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))

        valid_username = "sai.tarakaram@indiahealthlink.com"
        valid_password = "@vengeR123"

        username_field.send_keys(valid_username)
        password_field.send_keys(valid_password)

        # Find and click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="Login"][value="Login"]')
        login_button.click()

        # Wait for the welcome message element to appear
        welcome_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "welcomeMessage"))
        )

        # Get the text content of the welcome message
        welcome_message_text = welcome_message_element.find_element(By.TAG_NAME, "h3").text

        # Verify the welcome message
        expected_welcome_message = "Welcome"
        if welcome_message_text == expected_welcome_message:
            print("Test passed! Welcome message displayed.")
        else:
            print(f"Test failed! Expected: '{expected_welcome_message}', Actual: '{welcome_message_text}'")

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
