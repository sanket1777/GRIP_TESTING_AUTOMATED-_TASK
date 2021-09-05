import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\Abc\\PROJECTS\\Automated Testing\\chromedriver.exe")  #add path of web-driver

# ----------- Testcase : URL ----------- #
print("Testcase 1 : \U00002714 ")
driver.get("https://www.thesparksfoundationsingapore.org/")
driver.set_window_size(1360, 1047)
print("Url is Valid ")

# ----------- Testcase : TITLE ----------- #
print("\n\nTestcase 2 :", end=" ")
if (driver.title):
    print("\U00002714 ")
    print("Page Title Found", driver.title)
else:
    print("\U0000274C ")
    print("No Title Found")
time.sleep(3)

# ----------- Testcase : LOGO ----------- #
print("\n\nTestcase 3 :", end=" ")
try:
    logo = driver.find_element_by_xpath("//*[@id='home']/div/div[1]/h1/a/img")
    actions = ActionChains(driver)
    actions.move_to_element(logo).click().perform()
    time.sleep(3)
    print("\U00002714 ")
    print("Logo Found!")
except NoSuchElementException:
    print("\U0000274C ")
    print("Logo Not Found!")
time.sleep(2)

# ----------- Testcase : HOME LINK ----------- #
print("\n\nTestcase 4 :", end=" ")
try:
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/h1/a").click()
    print("\U00002714 ")
    print("Home link Works!")
except NoSuchElementException:
    print("\U0000274C ")
    print("Home Link Doesn't Work!")
time.sleep(1)

# ----------- Testcase : DropDown ----------- #
print("\n\nTestcase 5 : Dropdown")
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/a").click()
print("\nDropdown : About Us \U00002714")
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[2]/a").click()
print("Dropdown : Policies and Code \U00002714")
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[3]/a").click()
print("Dropdown : Programs \U00002714")
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[4]/a").click()
print("Dropdown : LINKS \U00002714")
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[5]/a").click()
print("Dropdown : Join Us \U00002714")
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[6]/a").click()

# ----------- Testcase : Contact - Us page ----------- #
print("\n\nTestcase 6 ", end=" ")
print("Link : Contact Us \U00002714")
time.sleep(2)  # Navigates to another page  , Contact - Us page
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[1]/p/span/a").click()
time.sleep(2.5)
print("Link To Linkedin \U00002714")
driver.back()  # back to contact us page
time.sleep(2)
contact_info = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/p[2]")
if (contact_info.text == "+65-8402-8590, info@thesparksfoundation.sg"):
    time.sleep(1.5)
    print("Contact Info Valid \U00002714")
else:
    print("Contact Info Invalid \U0000274C")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # Scrolls
driver.back()  # Back to Home-Page

# ----------- Testcase : Slider ----------- #
print("\n\nTestcase 7 : Slider")
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/section/div/ol/li[1]/a").click()
print("\nSlider 1 : Events \U00002714")
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/section/div/ol/li[2]/a").click()
print("Slider 2 : Internships \U00002714")
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/section/div/ol/li[3]/a").click()
print("Slider 3 : Mentorship \U00002714")
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/section/div/ol/li[4]/a").click()
print("Slider 4 : Support \U00002714")
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/section/div/ol/li[5]/a").click()
print("Slider 5 : Scholarship \U00002714")
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/section/div/ol/li[6]/a").click()
print("Slider 6 : Community \U00002714")
time.sleep(3)

# ----------- Testcase : Scroll ----------- #
print("\n\nTestcase 8 : Scrolled Down ", end=" ")
driver.execute_script("window.scrollBy(0,500)", "")
print("\U00002714")

# ----------- Testcase :  Link to Page [1] ----------- #
time.sleep(1.5)
print("\n\nTestcase 9 : Page - ", end=" ")
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/a").click()  # Link to Vision, Mission And Values
print("Vision, Mission and Values \U00002714")
time.sleep(1.5)
for i in range(0, driver.get_window_size().get("height"), 200):
    driver.execute_script("window.scrollBy(0," + str(i) + ")")
    time.sleep(1)

driver.back()  # Back to Home-Page
print("\n\nScrolled Down")
driver.execute_script("window.scrollBy(0, 900)", "")

# ----------- Testcase : Auto Mouse Hover ----------- #
print("\n\nTestcase 10 : Auto Mouse Hover ", end=" ")
one = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div[1]")
two = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div[2]")
three = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div[3]")
four = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[1]")
five = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[2]")
six = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[3]")
actions = ActionChains(driver)
actions.move_to_element(one).move_to_element(two).move_to_element(three).click().perform()
time.sleep(1)
actions.move_to_element(four).move_to_element(five).move_to_element(six).click().perform()
print("\U00002714 ")
time.sleep(1.5)

# ----------- Testcase : Link to Page [2] ----------- #
time.sleep(1.5)
print("\n\nTestcase 11 : Page - ", end=" ")
button = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a")  # Link to Join Us
actions = ActionChains(driver)
time.sleep(1)
actions.move_to_element(button).click().perform()
print("Join Us \U00002714")
driver.execute_script("window.scrollBy(0,600)", " ")

# ----------- Testcase: AutoFill Form ----------- #
print("\n\nTestcase 12 : Fill Form Automatically ")
driver.find_element(By.NAME, "Name").send_keys("Deeksha" + Keys.ENTER)
print("\nAutoFill Name \U00002714")
time.sleep(2)
Select(driver.find_element(By.CLASS_NAME, "form-control")).select_by_index(1)
print("AutoSelect Student from Dropdown \U00002714")
time.sleep(2)
driver.find_element(By.NAME, "Email").send_keys("deekshapatidar9@gmail.com" + Keys.ENTER)
print("AutoFill Email \U00002714")
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]").click()
driver.back()
print("\nBack to Home-Page")
driver.back()

# ----------- Testcase: Scrolled Down to Bottom ----------- #
print("\n\nScrolled Down to Bottom")
driver.execute_script("window.scrollBy(0, 1350)", "")
time.sleep(1.5)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

# ----------- Testcase: Internship Programs At TSF ----------- #
print("\n\nTestcase 13 : Linkedin Page ", end=" ")
driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/a").click()
driver.refresh()
time.sleep(5)
print("\U00002714")

# ----------- Testcase: Switched To Home Page ----------- #
print("\n\nSwitched to Home Page ", end=" ")
driver.switch_to.window(driver.window_handles[0])
print("\U00002714")

# ----------- Testcase: Test Youtube Video Iframe ----------- #
print("\n\nTestcase 14 : Youtube Video Iframe \U00002714")
yt_iframe = driver.find_element_by_xpath("//iframe[contains(@src,'https://www.youtube.com/embed/kgj_0E_urK0?autoplay=0&theme=light&loop=1&disablekb=1&modestbranding=1&hd=1&autohide=0&color=white&controls=0&showinfo=0&showsearch=0&cc_load_policy=1&rel=0')]")
driver.switch_to.frame(yt_iframe)
button = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/button")
button.click()
print("Youtube video starts playing")
time.sleep(7)
button = driver.find_element_by_xpath("/html/body/div/div/div[1]/video")
button.click()
print("Youtube video paused")
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

# ----------- Testcase: Test Links under Join Us! ----------- #
print("\n\nTestcase 15 : Page - ", end=" ")
test_link_1 = driver.find_element_by_xpath("/html/body/div[6]/div/div[1]/div[2]/ul/li[1]/a")
actions = ActionChains(driver)
time.sleep(1.5)
actions.move_to_element(test_link_1).click().perform()
print("Internship Positions \U00002714")
time.sleep(1.5)
for i in range(0, 600, 200):
    driver.execute_script("window.scrollBy(0," + str(i) + ")")
    time.sleep(1.5)

driver.back()
print("\nBack to Home-Page")

# Scrolled Down to Bottom
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(1.5)

print("\n\nTestcase 16 : Page - ", end=" ")
driver.find_element_by_link_text('Events Volunteer').click()
driver.refresh()
time.sleep(1.5)
print("Events Volunteers \U00002714")
time.sleep(1.5)
for i in range(0, 600, 200):
    driver.execute_script("window.scrollBy(0," + str(i) + ")")
    time.sleep(1.5)

driver.back()

# Scrolled Down to Bottom
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(1.5)

# ----------- Testcase: Test Links under Programs ----------- #
print("\n\nTestcase 17 : Page - ", end=" ")
driver.find_element_by_link_text('Student SOS Program').click()
driver.refresh()
time.sleep(1.5)
print("Student SOS Program \U00002714")
time.sleep(1.5)
for i in range(0, 600, 200):
    driver.execute_script("window.scrollBy(0," + str(i) + ")")
    time.sleep(1.5)

driver.back()

# Scrolled Down to Bottom
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(1.5)

# ----------- Testcase: Test Links under Workshops ----------- #
print("\n\nTestcase 18 : Page - ", end=" ")
driver.find_element_by_link_text('Glimpses for Kids').click()
time.sleep(1.5)
driver.refresh()
print("Glimpses for Kids \U00002714")
time.sleep(1.5)
for i in range(0, 600, 200):
    driver.execute_script("window.scrollBy(0," + str(i) + ")")
    time.sleep(1.5)

driver.back()
time.sleep(2)

# Scrolled Down to Bottom
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(1.5)

print("\n\nTestcase 19 : Page - ", end=" ")
driver.find_element_by_link_text('Career Choices').click()
time.sleep(1.5)
driver.refresh()
print("Career Choices \U00002714")
time.sleep(1.5)
for i in range(0, 600, 200):
    driver.execute_script("window.scrollBy(0," + str(i) + ")")
    time.sleep(1.5)

driver.back()
time.sleep(2)

# Scrolled Down to Bottom
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(1.5)

# ----------- Testcase: Test Links under Partners ----------- #
print("\n\nTestcase 20 : Page - ", end=" ")
driver.find_element_by_link_text('AINE AI').click()
driver.refresh()
time.sleep(1.5)
print("AINE AI \U00002714")
time.sleep(6)

# ----------- Testcase: Switched To Home Page ----------- #
print("\n\nTestcase 21 : Switched to Home Page ", end=" ")
driver.switch_to.window(driver.window_handles[0])
print("\U00002714")

# Scrolled Down to Bottom
time.sleep(2)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(1.5)

# ----------- Testcase: Test Links under Websites ----------- #
print("\n\nTestcase 22 : Page - ", end=" ")
driver.find_element_by_link_text('The Sparks Foundation (Global)').click()
driver.refresh()
time.sleep(1.5)
print("The Sparks Foundation (Global) \U00002714")

time.sleep(10)
driver.switch_to.window(driver.window_handles[0])

# Scrolled Down to Bottom
time.sleep(2)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(1.5)

# ----------- Testcase: Scrolled To Top ----------- #
print("\n\nTestcase 23 : Scrolled to Top ", end=" ")
driver.find_element_by_xpath("/html/body/a/span").click()
print("\U00002714")
time.sleep(4)

driver.quit() #closes all windows
