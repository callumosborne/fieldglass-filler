from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import time

# Do you want the browser to show as it fills in?
headless = True

options = Options()
options.headless = headless

browser = webdriver.Firefox(options=options)

browser.get("https://www.fieldglass.net/?next=%2Fworker_desktop.do")

username = browser.find_element_by_id("usernameId_new")
password = browser.find_element_by_id("passwordId_new")
submit   = browser.find_element_by_name("action")

username.send_keys("callum.osborne")
password.send_keys(":Tk9P/x[25W\\xh]Vc")


submit.click()

wait = WebDriverWait( browser, 3 )

complete_timesheet = browser.find_elements_by_link_text("Complete Time Sheet")[0]
complete_timesheet.click()

for x in range(0, 5):
    cell_in  = "timein0" + str(x)
    cell_out = "timein" + str(x+30)

    time_in = browser.find_element_by_name(cell_in)
    time_out = browser.find_element_by_name(cell_out)

    time_in.send_keys('09:00')
    time_out.send_keys('17:00')

    cell_time_worked = "t_z12061520440238615056a6f_b_" + str(x + 1) + "_r1"

    duration = browser.find_element_by_id(cell_time_worked)

    duration.send_keys('8')

wait = WebDriverWait( browser, 3 )

submit = browser.find_element_by_id("fgTSSubmit")
submit.click()

time.sleep(5)

update = browser.find_element_by_id('update')
update.click()