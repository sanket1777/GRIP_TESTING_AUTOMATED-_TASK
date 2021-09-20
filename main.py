from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

options_obj = Options()
options_obj.add_argument("start-maximized")
options_obj.add_argument("--disable-extensions")

wd_chrome = webdriver.Chrome(options=options_obj, executable_path="R:\chromedriver.exe")
wd_chrome.get("https://www.thesparksfoundationsingapore.org/")
print("\nTest Cases")

# TestCase1: Checking for the logo of the webpage
print("\nTestCase 1:")
logo = wd_chrome.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/img')
if logo.is_displayed():
    print("Successful : Logo is Present!!\n")
    time.sleep(2)
else:
    print("Logo is not visible!!\n")

# TestCase2: Checking for the parameter 'nav'
print("TestCase 2:")
try:
    wd_chrome.find_element_by_tag_name('nav')
    print("Verification of navigation bar has been done successfully!!\n")
except NoSuchElementException:
    print("Failed in Verifying of navigation bar!!\n")

# TestCase3: checking for 'About Us'
print("TestCase 3:")
try:
    wd_chrome.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/a').click()
    time.sleep(2)
    wd_chrome.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/ul/li[1]/a').click()
    time.sleep(3)
    print('About Us Page is visited Successfully!!\n')
except NoSuchElementException:
    print("Failed to visit About Us Page!!\n")
    time.sleep(3)

# TestCase4: Checking for the parameter 'Home'
print("TestCase 4:")
try:
    wd_chrome.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home link is working Successfully!!!\n")
except NoSuchElementException:
    print("Home Link is not Working!\n")

# TestCase5: Verifying the parameter 'Title'
print("TestCase 5:")
if wd_chrome.title:
    print("Title has been verified Successfully: ", wd_chrome.title)
else:
    print("Title Verification Failed!!")

# TestCase 6: Checking Policy page
print('\nTestCase 6:')
try:
    wd_chrome.find_element_by_link_text('Policies and Code').click()
    time.sleep(3)
    wd_chrome.find_element_by_link_text("Policies").click()
    time.sleep(2)
    wd_chrome.find_element_by_link_text('Code of Ethics and Conduct').click()
    time.sleep(2)
    print('Policy Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase7: Programs page
print('TestCase 7:')
try:
    wd_chrome.find_element_by_link_text('Programs').click()
    time.sleep(3)
    wd_chrome.find_element_by_link_text('Student Scholarship Program').click()
    time.sleep(3)
    wd_chrome.find_element_by_link_text("Student Mentorship Program").click()
    time.sleep(3)
    wd_chrome.find_element_by_link_text('Student SOS Program').click()
    time.sleep(3)
    wd_chrome.find_element_by_link_text('Workshops').click()
    time.sleep(3)
    wd_chrome.find_element_by_link_text('Corporate Programs').click()
    time.sleep(3)
    print('Programs Page is Verified!!\n')
except NoSuchElementException:
    print('Failed to verify Programs page!\n')

# TestCase8 : verifying Links Page
print("TestCase 8:")
try:
    wd_chrome.find_element_by_link_text('LINKS').click()
    time.sleep(2)
    wd_chrome.find_element_by_link_text('Software & App').click()
    time.sleep(2)
    wd_chrome.find_element_by_link_text('AI in Education').click()
    time.sleep(2)
    print('Successfully verified links page!!\n')
except NoSuchElementException:
    print("Links page Verification Failed!\n")

# Testcase9 : Checking for the parameter 'Join Us'
print('TestCase 9:')
try:
    join_us = wd_chrome.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[5]/a')
    join_us.click()
    time.sleep(2)
    why_join_us = wd_chrome.get('https://www.thesparksfoundationsingapore.org/join-us/why-join-us/')
    time.sleep(2)
    name = wd_chrome.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]')
    email = wd_chrome.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]')
    role = wd_chrome.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/select')

    # Scrolling Action
    wd_chrome.execute_script("window.scrollBy(0,500)", name)
    time.sleep(2)

    name.send_keys('sanket kamble')
    time.sleep(2)

    email.send_keys('sanketkamble1777@gmail.com')
    time.sleep(2)

    choose = Select(role)
    choose.select_by_visible_text('Student')
    print('Join US page is visited and Form filled successfully\n')
except:
    print('Join US page is not visited\n')

time.sleep(3)

# TestCase10 : Checking for the Contact Us Page
print("TestCase 10:")
try:
    wd_chrome.find_element_by_link_text("Contact Us").click()
    time.sleep(2)
    info = wd_chrome.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(2)

    # print(info.text)
    if info.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print('Contact Information is Correct!')
    else:
        print('Incorrect! Information')
    print("Contact Page Verification ha done Successfully!\n")
    wd_chrome.execute_script("window.scrollBy(0,350)", "")
    time.sleep(2)
    wd_chrome.execute_script("window.scrollBy(0,350)", "")
    time.sleep(2)
    wd_chrome.execute_script("window.scrollBy(0,350)", "")
    time.sleep(2)
    wd_chrome.execute_script("window.scrollBy(0,100)", "")
except NoSuchElementException:
    print("Contact Page Verification Unsuccessful!")
