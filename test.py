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
        user_id_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-login/div/div/div[2]/div/div/div/div/div[3]/div/form/div[1]/input'))
        )
        user_id_input.send_keys("pavan.veeramaneni@indiahealthlink.com")

        # Find and interact with the password input field using its XPath
        password_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-login/div/div/div[2]/div/div/div/div/div[3]/div/form/div[2]/input'))
        )
        password_input.send_keys("ABCd@123456")

        # Find and click the login button using its XPath
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-login/div/div/div[2]/div/div/div/div/div[3]/div/form/div[3]/button'))
        )
        login_button.click()

        # Wait for the element on the next page to be displayed
        success_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-dashboard/div[2]/div/div[1]/h2'))
        )

        # If the element is displayed, print "Login successful"
        print("Login successful")

        # Wait for the Welcome Text to be displayed
        welcome_text_tab = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-dashboard/app-headbar/div/div/div[2]/div/span[1]'))
        )

        # If the Welcome Text is found, print a message
        if welcome_text_tab:
            print("Welcome Text is displayed.")

        # Click on the profile tab
        profile_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-dashboard/app-headbar/div/div/div[2]/div/span[2]/span/span[1]'))
        )
        profile_tab.click()

        # Verify the profile settings text
        profile_settings_text = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-dt/div/div/h2'))
        )

        # If the profile settings text is found, print the message
        if profile_settings_text:
            print("Clicked on profile, and profile setting text is verified.")

        # Click on the dashboard icon button
        dashboard_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-dt/app-sidebar/div/div/a[1]/span'))
        )
        dashboard_button.click()

        # Verify the stats text
        stats_text = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-dashboard/div[2]/div/div[1]/h2'))
        )

        # If the stats text is found, print the message
        if stats_text:
            print("Clicked on dashboard, and stats text is verified.")

        # Click on the tele consultation tab
        tele_consultation_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-dashboard/app-sidebar/div/div/a[2]/span/div'))
        )
        tele_consultation_tab.click()

        # Verify the tele consultation text
        tele_consultation_text = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-teleconsultdashboard/div/div[1]/h3'))
        )

        # If the tele consultation text is found, print the message
        if tele_consultation_text:
            print("Clicked on tele consultation tab and tele consultation text is verified.")

    except Exception as e:
        print("Login failed. Error:", str(e))

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
