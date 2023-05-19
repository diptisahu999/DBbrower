from selenium import webdriver

# Set up the Selenium webdriver
driver = webdriver.Chrome('path_to_chromedriver')  # Replace with the path to your chromedriver executable

# Open the registration page
driver.get('https://example.com/register')  # Replace with the URL of your registration page

# Find the registration form input fields and enter the required information
username_input = driver.find_element_by_id('username')  # Replace 'username' with the actual ID or CSS selector of the username input field
email_input = driver.find_element_by_id('email')  # Replace 'email' with the actual ID or CSS selector of the email input field
password_input = driver.find_element_by_id('password')  # Replace 'password' with the actual ID or CSS selector of the password input field

username_input.send_keys('your_username')  # Replace 'your_username' with the desired username
email_input.send_keys('your_email@example.com')  # Replace 'your_email@example.com' with the desired email address
password_input.send_keys('your_password')  # Replace 'your_password' with the desired password

# Find and click the registration button
register_button = driver.find_element_by_id('register_button')  # Replace 'register_button' with the actual ID or CSS selector of the registration button
register_button.click()

# Perform any additional actions after registration if needed
# ...

# Close the browser window
driver.quit()