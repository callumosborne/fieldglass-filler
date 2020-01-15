import re
from mechanize import Browser

br = Browser()


br.set_handle_robots( False )
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.open("https://www.fieldglass.net/?next=%2Fworker_desktop.do")

br.select_form(name="loginForm")
br["username"] = "callum.osborne"
br["password"] = ":Tk9P/x[25W\\xh]Vc"

response = br.submit()  # submit current form

# print(response.read().decode('UTF-8'))

response = br.follow_link(br.find_link(text="Complete Time Sheet"))

br.select_form(name="timeSheetForm")

for x in range(0, 5):
    cell_in  = "timein0" + str(x)
    cell_out = "timein" + str(x+30)

    br[cell_in] = "09:00"
    br[cell_out] = "17:00"

    time_worked = "t_z12061520440238615056a6f_b_" + str(x + 1) + "_r1"

    br.find_control(id=time_worked).value = "8"

# response = br.submit(id="fgTSSubmit")

# br.select_form(name="formNavigationContainer")

# response = br.find_control(id="fgTSSubmit").click()

# br.form.action = "fgTSSubmit"

response = br.submit(id="fgTSSubmit",nr=0)

print(response)

# print(response.read().decode('UTF-8'))
