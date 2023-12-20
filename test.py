from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def find_element(driver, xpath):
    return WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))

def click_element(driver, xpath):
    element = find_element(driver, xpath)
    element.click()
    return element

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
        # Open the login page
        driver.get("http://54.183.238.1/")

        # Define XPaths as variables
        user_id_xpath = '/html/body/app-root/app-login/div/div/div[2]/div/div/div/div/div[3]/div/form/div[1]/input'
        password_xpath = '/html/body/app-root/app-login/div/div/div[2]/div/div/div/div/div[3]/div/form/div[2]/input'
        login_button_xpath = '/html/body/app-root/app-login/div/div/div[2]/div/div/div/div/div[3]/div/form/div[3]/button'
        dashboard_button_xpath = '/html/body/app-root/app-dt/app-sidebar/div/div/a[1]/span'
        stats_text_xpath = '/html/body/app-root/app-dashboard/div[2]/div/div[1]/h2'
        welcome_text_xpath = '/html/body/app-root/app-dashboard/app-headbar/div/div/div[2]/div/span[1]'
        profile_tab_xpath = '/html/body/app-root/app-dashboard/app-headbar/div/div/div[2]/div/span[2]/span/span[1]'
        profile_settings_xpath = '/html/body/app-root/app-dt/div/div/h2'
        tele_consultation_tab_xpath = '/html/body/app-root/app-dashboard/app-sidebar/div/div/a[3]/span/div'
        tele_consultation_text_xpath = '/html/body/app-root/app-teleconsultdashboard/div/div[1]/h3'
        member_services_xpath = '/html/body/app-root/app-teleconsultdashboard/app-sidebar/div/div/a[2]/span/div'
        select_your_association_xpath = '/html/body/app-root/app-affiliated-users/div/div[1]/div/h3'
        dev_testing_xpath = '/html/body/app-root/app-affiliated-users/div/div[2]/div/div[2]/div/span'
        dev_testing_text_xpath = '/html/body/app-root/app-affiliated-users/div/div[1]/div[1]/h3'
        financial_wellbeing_xpath = '/html/body/app-root/app-affiliated-users/div/div[2]/div/div[3]/div/span'
        accept_button_xpath = '/html/body/div[3]/div[2]/div/mat-dialog-container/app-modal/div/div[2]/div[2]/button[2]'
        consultants_list_xpath = '/html/body/app-root/app-affiliated-category-users/div/div[1]/div[2]/h5'
        call_button_xpath = '/html/body/app-root/app-affiliated-category-users/div/div[1]/div[2]/div/div[6]/div/div/div[3]/span[1]'
        visit_xpath = '/html/body/app-root/app-teleconsult-confirm-visit/div[1]/div[2]/div[3]/div[1]/div/mat-form-field/div/div[1]/div/input'
        confirm_button_xpath = '/html/body/app-root/app-teleconsult-confirm-visit/div[1]/div[2]/div[3]/div[2]/div/div[2]/button'
        user_name_xpath = '/html/body/app-root/app-login/div/div/mat-card/mat-card-content/form/mat-form-field[1]/div/div[1]/div[3]/input'
        pwd_xpath = '/html/body/app-root/app-login/div/div/mat-card/mat-card-content/form/mat-form-field[2]/div/div[1]/div[3]/input'
        submit_button_xpath = '/html/body/app-root/app-login/div/div/mat-card/mat-card-content/form/mat-card-actions/div/button'
        

        # Interact with the user ID input field
        user_id_input = find_element(driver, user_id_xpath)
        user_id_input.send_keys("deepak.mathi@indiahealthlink.com")
        time.sleep(10)

        # Interact with the password input field
        password_input = find_element(driver, password_xpath)
        password_input.send_keys("Test@123")
        time.sleep(10)

        # Click the login button
        click_element(driver, login_button_xpath)
        print("Login successful")
        time.sleep(10)

        # Verify Welcome Text
        find_element(driver, welcome_text_xpath)
        print("Welcome Text is displayed.")
        time.sleep(10)

        # Click on the profile tab
        click_element(driver, profile_tab_xpath)
        time.sleep(10)

        # Verify profile settings text
        find_element(driver, profile_settings_xpath)
        print("Clicked on profile, and profile setting text is verified.")
        time.sleep(10)

        # Click on the dashboard icon button
        click_element(driver, dashboard_button_xpath)
        time.sleep(10)

        # Verify the stats text
        find_element(driver, stats_text_xpath)
        print("Clicked on dashboard, and stats text is verified.")
        time.sleep(10)

        # Click on the tele consultation tab
        click_element(driver, tele_consultation_tab_xpath)
        time.sleep(10)

        # Verify the tele consultation text
        find_element(driver, tele_consultation_text_xpath)
        print("Clicked on tele consultation tab and tele consultation text is verified.")
        time.sleep(10)

        # Click on the member services tab
        click_element(driver, member_services_xpath)
        print("Clicked on member services tab")
        time.sleep(10)

        # Verify the select your association text
        find_element(driver, select_your_association_xpath)
        print("Clicked on member services and select your association text is verified.")
        time.sleep(10)

        # Click on the Dev Testing tab
        click_element(driver, dev_testing_xpath)
        print("Clicked on Dev Testing tab")
        time.sleep(10)

        # Verify the Dev Testing text
        find_element(driver, dev_testing_text_xpath)
        print("Clicked on Dev Testing tab and Dev Testing text is verified.")
        time.sleep(10)

        # Click on the Financial Wellbeing tab
        click_element(driver, financial_wellbeing_xpath)
        print("Clicked on Financial Wellbeing tab")
        time.sleep(10)

        # Click on the Accept button
        click_element(driver, accept_button_xpath)
        print("Clicked on Accept button")
        time.sleep(20)

        # Verify the Consultants list text
        find_element(driver, consultants_list_xpath)
        print("consultants list text is verified.")
        time.sleep(20)

        # Click on the Call button
        click_element(driver, call_button_xpath )
        print("Clicked on call button")
        time.sleep(20)

        # Interact with the visit Xpath field
        visit_xpath_input = find_element(driver, visit_xpath)
        visit_xpath_input.send_keys("sample")
        time.sleep(10)

        # Click on the Confirm button
        click_element(driver, confirm_button_xpath )
        print("Clicked on confirm button")
        time.sleep(10)

        # Open a new tab
        driver.execute_script("window.open('about:blank', '_blank');")

        # Switch to the newly opened tab
        driver.switch_to.window(driver.window_handles[1])

        # Navigate to the desired URL
        new_tab_url = "https://apps.indiahealthlink.com/consultant/"
        driver.get(new_tab_url)

        # Add a delay if needed to ensure the page is fully loaded
        time.sleep(10)



        # # Switch back to the original tab
        # driver.switch_to.window(driver.window_handles[0])

        # Interact with the user ID input field
        user_name_input = find_element(driver, user_name_xpath)
        user_name_input.send_keys("Janhavidr")
        time.sleep(10)

        # Interact with the password input field
        password_input = find_element(driver, pwd_xpath)
        password_input.send_keys("Test@123")
        time.sleep(10)

        # Click the submit button
        click_element(driver, submit_button_xpath)
        print("submit successful")
        time.sleep(10)






    except Exception as e:
        print("Login failed. Error:", str(e))

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
