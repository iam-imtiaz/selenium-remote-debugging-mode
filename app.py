
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Create ChromeOptions object
chrome_options = Options()

# Set the debugger address
chrome_options.add_experimental_option('debuggerAddress', 'localhost:9222')

# Connect to the already open debug version of Chrome
driver = webdriver.Chrome(options=chrome_options)

# open new window with execute_script()
driver.execute_script("window.open('');")
# switch to new window with switch_to.window()
driver.switch_to.new_window('tab')
# open new window with execute_script()
driver.get('https://www.google.com/');

# send text and submit
element = driver.find_element(By.XPATH,"//input[@name='q']")
element.send_keys("Selenium")
element.submit()
driver.quit()
