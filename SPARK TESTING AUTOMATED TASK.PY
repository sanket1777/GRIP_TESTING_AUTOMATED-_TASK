# Imports
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

import time
# Init driver
driver = webdriver.Chrome()

# Variable
testUrl = "https://www.thesparksfoundationsingapore.org/"

# Styles
class Style():
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    reset = '\033[0m'

# Output
Success = Style.green +"Success" + Style.reset
Failed = Style.red +"Failed" + Style.reset

# Tests
def Tests(url):
    driver.get(url)
    print("Site: " + Style.yellow + driver.title + Style.reset )
    print("URL: " + Style.yellow + driver.current_url + Style.reset )  
    
    # Test 1 => Title
    def testTitle():
        if driver.title:
            print("Title: " + Success )
        else:
            print("Title: " + Failed )
    testTitle()

    # Test 2 => Site Logo
    def testLogo():
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/h1/a/img').click()
            print("Logo: " + Success )
            time.sleep(3)
        except NoSuchElementException:
            print("Logo: " + Failed )    
    testLogo()

    # Test 3 => Navbar
    def testNavbar():
        try:
            driver.find_element_by_tag_name("nav")
            print("Navbar: " + Success )
        except NoSuchElementException:
            print("Navbar: "  + Failed )
    testNavbar()

    # Test 4 => Home button
    def testHomeButton():
        try:
            driver.find_element_by_class_name("navbar-brand").click()
            print("Home Link: " + Success )
        except NoSuchElementException:
            print("Home Link: " + + Failed )
    testHomeButton()

    # Test 5 => About Us Page
    def testAbout():
        try:
            driver.find_element_by_link_text('About Us').click()
            time.sleep(1.5)
            driver.find_element_by_link_text('News').click()
            time.sleep(3)
            print("About Page: " + Success )
        except NoSuchElementException:
            print("About Page: " + Failed )
    testAbout()

    # Test 6 => Policies Page
    def testPolicy():
        try:
            driver.find_element_by_link_text('Policies and Code').click()
            time.sleep(1.5)
            driver.find_element_by_link_text("Service Quality Values").click()
            time.sleep(3)
            print("Policy Page: " + Success )
        except NoSuchElementException:
            print("Policy Page: " + Failed )
    testPolicy()

    # Test 7 => Programs page
    def testPrograms():
        try:
            driver.find_element_by_link_text('Programs').click()
            time.sleep(1.5)
            driver.find_element_by_link_text("Corporate Programs").click()
            time.sleep(3)
            print("Programs Page: " + Success )
        except NoSuchElementException:
            print("Programs Page" + Failed )
    testPrograms()

    # Test 8 => Links Page
    def testLinks():
        try:
            driver.find_element_by_link_text('LINKS').click()
            time.sleep(1.5)
            driver.find_element_by_link_text('AI in Education').click()
            time.sleep(3)
            print("Links Page: " + Success )
        except NoSuchElementException:
            print("Links Page: " + Failed )
    testLinks()

    # Test 9 => Contact us Page
    def testContact():
        try:
            driver.find_element_by_link_text("Contact Us").click()
            time.sleep(3)
            linkCheckContact = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
            time.sleep(1)
            if linkCheckContact.text == "+65-8402-8590, info@thesparksfoundation.sg":
                print("Contact Info: " + Success )
            else:
                print("Contact Info: " + Failed )
            print("Contact Page: " + Success )
        except NoSuchElementException:
            print("Contact Page: " + Failed )
    testContact()


    # Test 10 => Check the Form
    def testForm():
        try:
            driver.find_element_by_link_text("Join Us").click()
            time.sleep(1.5)
            driver.find_element_by_link_text("Brand Ambassador").click()
            time.sleep(3)
            driver.find_element_by_name('Name').send_keys('sanket')
            time.sleep(1)
            driver.find_element_by_name('Email').send_keys('sanketkamble1777@GMAIL.COM.com')
            time.sleep(1)
            select = Select(driver.find_element_by_class_name('form-control'))
            time.sleep(1)
            select.select_by_visible_text('Intern')
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]").click()
            time.sleep(3)
            print("Form: " + Success )
        except NoSuchElementException:
            print("Form: " + Failed )
            time.sleep(4)
    testForm()             

    # Test 11 => Know More Button
    def testKnowMore():
        try:
            driver.find_element_by_class_name("navbar-brand").click()
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/a")
            print("Know More Button: " + Success )
        except NoSuchElementException:
            print("Know More Button: " + Failed )
    testKnowMore()

    # Test 12 => Hover to Top button
    def hoverTop():
        try:
            driver.find_element_by_id("toTopHover").click()
            time.sleep(1)
            print("Hover Button: " + Success )
        except NoSuchElementException:
            print("Hover: " + Failed )
        hoverTop()

        # Test 13 => Copyright text
        def testCopyright():
            driver.find_element_by_class_name("navbar-brand").click()
            time.sleep(3)
            copyrightText = driver.find_element_by_xpath('/html/body/div[7]/p')
            time.sleep(1)
            if copyrightText.text == "© 2017 The Sparks Foundation. All Rights Reserved | Design by W3layouts":
                print("Copyright Text: " + Success)
            else:
                print("Copyright Text: " + Failed)

        testCopyright()

        # Test 13 => Copyright text
        def testCopyright():
            driver.find_element_by_class_name("navbar-brand").click()
            time.sleep(3)
            copyrightText = driver.find_element_by_xpath('/html/body/div[7]/p')
            time.sleep(1)
            if copyrightText.text == "© 2017 The Sparks Foundation. All Rights Reserved | Design by W3layouts":
                print("Copyright Text: " + Success)
            else:
                print("Copyright Text: " + Failed)

        testCopyright()

    # Exit the test
    def exit():
        driver.close()
    exit()


# Run Final Test
