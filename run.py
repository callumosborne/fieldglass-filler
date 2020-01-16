from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import time
import sys

# Select False if you want to see the browser automatically fill the sheet in
headless = True

options = Options()
options.headless = headless
browser = webdriver.Firefox(options=options)

# Open url
browser.get("https://www.fieldglass.net/?next=%2Fworker_desktop.do")

# Get login elements
username_element = browser.find_element_by_id("usernameId_new")
password_element = browser.find_element_by_id("passwordId_new")
submit_element   = browser.find_element_by_name("action")

with open ("login.txt", "r") as login_file:
    username = login_file.readline()[:-1]
    password = login_file.readline()

# Submit username and password
username_element.send_keys(username)
password_element.send_keys(password)

submit_element.click()

wait = WebDriverWait( browser, 3 )

available_timesheets = browser.find_elements_by_link_text("Complete Time Sheet")

# If no availabale timesheets end program
if len(available_timesheets) == 0:
    print('No timesheets to fill in...')
    print('-- This can also be caused by an incorrect username or password.')
    sys.exit()
    
# Select first timesheet
complete_timesheet = available_timesheets[0]
complete_timesheet.click()

# Fill in form
for x in range(0, 5):

    cell_in  = "timein0" + str(x)
    cell_out = "timein" + str(x+30)

    time_in = browser.find_element_by_name(cell_in)
    time_out = browser.find_element_by_name(cell_out)

    # Start at 9am and end at 5pm
    time_in.send_keys('09:00')
    time_out.send_keys('17:00')

    # Worked 8 hours standard time
    cell_time_worked = "t_z12061520440238615056a6f_b_" + str(x + 1) + "_r1"
    duration = browser.find_element_by_id(cell_time_worked)
    duration.send_keys('8')

wait = WebDriverWait( browser, 3 )

submit = browser.find_element_by_id("fgTSSubmit")
submit.click()

# Wait for the submit form to show up
time.sleep(5)

update = browser.find_element_by_id('update')
update.click()