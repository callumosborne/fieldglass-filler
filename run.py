from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import time
import sys

"""
Exit codes:
0: Success
1: Incorrect Login
2: No Timesheets to fill in
3: Timesheet unsuccessfully filled in
"""

class Fieldglass:

    def __init__(self):

        # Select False if you want to see the browser automatically fill the sheet in
        headless = True

        options = Options()
        options.headless = headless
        self.browser = webdriver.Firefox(options=options)

        # Open url
        self.browser.get("https://www.fieldglass.net/?next=%2Fworker_desktop.do")

    def login(self):

        # Get login elements
        username_element = self.browser.find_element_by_id("usernameId_new")
        password_element = self.browser.find_element_by_id("passwordId_new")
        submit_element   = self.browser.find_element_by_name("action")

        with open ("login.txt", "r") as login_file:
            username = login_file.readline()[:-1]
            password = login_file.readline()

        # Submit username and password
        username_element.send_keys(username)
        password_element.send_keys(password)

        submit_element.click()

        time.sleep(3)

    def incorrect_login(self):
        errors = self.browser.find_elements_by_class_name("globalError")
        if len(errors) != 0:
            return True
        return False

    def get_available_ts(self):

        return self.browser.find_elements_by_link_text("Complete Time Sheet")

    def fill_timesheet(self, timesheet):

        timesheet.click()

        # Fill in form
        for x in range(0, 5):

            cell_in  = "timein0" + str(x)
            cell_out = "timein" + str(x+30)

            time_in = self.browser.find_element_by_name(cell_in)
            time_out = self.browser.find_element_by_name(cell_out)

            # Start at 9am and end at 5pm
            time_in.send_keys('09:00')
            time_out.send_keys('17:00')

            # Worked 8 hours standard time
            cell_time_worked = "t_z12061520440238615056a6f_b_" + str(x + 1) + "_r1"
            duration = self.browser.find_element_by_id(cell_time_worked)
            duration.send_keys('8')
        
        time.sleep(2)

        submit = self.browser.find_element_by_id("fgTSSubmit")
        submit.click()

        # Wait for the submit form to show up
        time.sleep(5)

        update = self.browser.find_element_by_id('update')
        update.click()

print('\nFieldglass Filler')
print('-----------------\n')

print('Logging in...')

fieldglass = Fieldglass()

fieldglass.login()

if fieldglass.incorrect_login():
    print('\nIncorrect login.\n')
    sys.exit(1)

print('Logged in successfully.')

current_no_ts = len(fieldglass.get_available_ts())

# If no availabale timesheets end program
if current_no_ts == 0:
    print('\nNo timesheets to fill in.\n')
    sys.exit(2)

print(str(current_no_ts) + ' timesheet(s) to fill in.' )
    
# Select first timesheet
timesheet = fieldglass.get_available_ts()[0]

print('Filling in timehseet...')

fieldglass.fill_timesheet(timesheet)

# To check the there is 1 less timesheet to fill in
test_fieldglass = Fieldglass()
test_fieldglass.login()
if current_no_ts == len(test_fieldglass.get_available_ts()):
    print('\nUnsuccessfull, please login to check why.\n')
    sys.exit(3)
else:
    print('\nSuccessfully submitted timesheet.\n')
    sys.exit(0)
