#!python3

"""
application_status_checker.py - automatically open the the application
status webpage and fill in required user inputs. In my case, I am
checking the status of my NY CPA license application, so the url
string is filled in with that website url.
"""

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def wait_for(sec=2):
    """Pause for a couple seconds between requests."""
    time.sleep(sec)


first = input("Enter first name: ")
last = input("Enter last name: ")
lookup_name = f"{last} {first}"

PATH = "/usr/bin/geckodriver" # geckodriver path
URL = "http://www.op.nysed.gov/opsearches.htm" # url to state license lookup

profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(
    firefox_profile=profile, executable_path= PATH
)

try:
    driver.get(URL)

    # the xpath is specific to my CPA application lookup
    elem = driver.find_element_by_xpath("//select/option[@value='07']")
    wait_for(1)
    elem.click() # sets the lookup value to "Accountant, Certified Public"

    wait_for(1)

    # tab to name input, enter user inputted name, and click enter
    elem.send_keys(Keys.TAB, lookup_name, Keys.RETURN)
    wait_for(1)

except Exception as any_error: # yeah yeah don't catch a blank Exception
    print(any_error)
    wait_for(4)

wait_for(60)
driver.close()
