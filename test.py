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

        # Find and interact with the user ID input field using its XPath
        user_id_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-login/div/div/div[2]/div/div/div/div/div[3]/div/form/div[1]/input'))
        )
        user_id_input.send_keys("pavan.veeramaneni@indiahealthlink.com")

        # Find and interact with the password input field using its XPath
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-login/div/div/div[2]/div/div/div/div/div[3]/div/form/div[2]/input'))
        )
        password_input.send_keys("ABCd@123456")

        # Find and click the login button using its XPath
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-login/div/div/div[2]/div/div/div/div/div[3]/div/form/div[3]/button'))
        )
        login_button.click()

        # Wait for the next page to load and check for the presence of an element with a specific XPath
        tele_consultation_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-take-survey/app-sidebar/div/div/a[2]/span'))
        )

        # Display a message if the element is found
        if tele_consultation_tab:
            print("Tele Consultation tab is displayed.")

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
