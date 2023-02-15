from selenium import webdriver
import time

# Set up the webdriver for your browser
driver = webdriver.Chrome()

# Navigate to the Twitter login page
driver.get('https://twitter.com/login')

# Enter your login credentials
username = driver.find_element_by_xpath('//input[@name="session[SKYPAHUNCHO]"]')
password = driver.find_element_by_xpath('//input[@name="session[@blackhat10#]"]')
username.send_keys('your_username')
password.send_keys('your_password')

# Click the login button
login_button = driver.find_element_by_xpath('//div[@data-testid="LoginForm_Login_Button"]')
login_button.click()

# Wait for the page to load
time.sleep(5)

# Navigate to the Twitter search page
driver.get('https://twitter.com/search')

# Enter the search keywords and filters
search_box = driver.find_element_by_xpath('//input[@data-testid="SearchBox_Search_Input"]')
search_box.send_keys('#newhandles')
search_box.submit()

# Wait for the page to load
time.sleep(5)

# Like each tweet containing the hashtag "newhandles"
like_buttons = driver.find_elements_by_xpath('//div[@data-testid="like"]')
for button in like_buttons:
    button.click()
    time.sleep(1)
