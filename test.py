from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_element(driver, xpath):
    return WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))

def click_element(driver, xpath):
    element = find_element(driver, xpath)
    element.click()
    return element

def main():
    # Set up the Selenium WebDriver with options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Use this if you're running headless
    options.binary_location = '/usr/bin/google-chrome'  # Actual path to Chrome binary
    driver = webdriver.Chrome(options=options)

    try:
        # Open the login page
        driver.get("http://172.171.252.63/")

        # Define XPaths as variables
        user_id_xpath = '/html/body/app-root/app-login/div/div/div[2]/div/div/div/div/div[3]/div/form/div[1]/input'
        password_xpath = '/html/body/app-root/app-login/div/div/div[2]/div/div/div/div/div[3]/div/form/div[2]/input'
        login_button_xpath = '/html/body/app-root/app-login/div/div/div[2]/div/div/div/div/div[3]/div/form/div[3]/button'
        welcome_text_xpath = '/html/body/app-root/app-dashboard/app-headbar/div/div/div[2]/div/span[1]'
        profile_tab_xpath = '/html/body/app-root/app-dashboard/app-headbar/div/div/div[2]/div/span[2]/span/span[1]'
        profile_settings_xpath = '/html/body/app-root/app-dt/div/div/h2'
        dashboard_button_xpath = '/html/body/app-root/app-dashboard/app-sidebar/div/div/a[1]/span'
        stats_text_xpath = '/html/body/app-root/app-dashboard/div[2]/div/div[1]/h2'
        tele_consultation_tab_xpath = '/html/body/app-root/app-dashboard/app-sidebar/div/div/a[2]/span/div'
        tele_consultation_text_xpath = '/html/body/app-root/app-teleconsultdashboard/div/div[1]/h3'

        # Interact with the user ID input field
        user_id_input = find_element(driver, user_id_xpath)
        user_id_input.send_keys("pavan.veeramaneni@indiahealthlink.com")

        # Interact with the password input field
        password_input = find_element(driver, password_xpath)
        password_input.send_keys("ABCd@123456")

        # Click the login button
        click_element(driver, login_button_xpath)
        print("Login successful")

        # Verify Welcome Text
        find_element(driver, welcome_text_xpath)
        print("Welcome Text is displayed.")

        # Click on the profile tab
        click_element(driver, profile_tab_xpath)

        # Verify profile settings text
        find_element(driver, profile_settings_xpath)
        print("Clicked on profile, and profile setting text is verified.")

        # Click on the dashboard icon button
        click_element(driver, dashboard_button_xpath)

        # Verify the stats text
        find_element(driver, stats_text_xpath)
        print("Clicked on dashboard, and stats text is verified.")

        # Click on the tele consultation tab
        click_element(driver, tele_consultation_tab_xpath)

        # Verify the tele consultation text
        find_element(driver, tele_consultation_text_xpath)
        print("Clicked on tele consultation tab and tele consultation text is verified.")

        # Click on the profile tab
        click_element(driver, profile_tab_xpath)

        # Verify profile settings text
        find_element(driver, profile_settings_xpath)
        print("Clicked on profile, and profile setting text is verified.")

        # Click on the dashboard button again
        click_element(driver, dashboard_button_xpath)

        # Verify the stats text after clicking on the dashboard button again
        find_element(driver, stats_text_xpath)
        print("Clicked on dashboard again, and stats text is verified.")

        

        
        

    except Exception as e:
        print("Login failed. Error:", str(e))

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
