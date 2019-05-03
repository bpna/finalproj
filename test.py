from selenium import webdriver as wd
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import random
import string
import sys

TEST_USER = "test"
TEST_PW = "supersecretpassword"

def init():
    chrome_options = wd.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = wd.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    return driver

def login(driver):
    username_field = driver.find_element_by_id("username")
    username_field.send_keys(TEST_USER)
    password_field = driver.find_element_by_id("password")
    password_field.send_keys(TEST_PW)
    submit_button = driver.find_element_by_id("submit")
    submit_button.click()

def logout(driver):
    logout_button = driver.find_element_by_link_text("Logout")
    logout_button.click()

def register(driver):
    register_link = driver.find_element_by_link_text("Click to Register!")
    register_link.click()
    form_fields = driver.find_elements_by_class_name("form-control")
    username = form_fields[0]
    username.send_keys(TEST_USER)
    email = form_fields[1]
    email.send_keys("test@test.com")
    password = form_fields[2]
    password.send_keys(TEST_PW)
    repeat_password = form_fields[3]
    repeat_password.send_keys(TEST_PW)
    register = wd.find_element_by_class_name("btn")
    register.click()

def delete_all_entries(driver):
    link_regex = re.compile('/read/test/[0-9]*')
    src = driver.page_source
    entry_urls = re.findall(link_regex, src)
    for u in entry_urls:
        entry_link = driver.find_element_by_xpath('//a[@href="' + u + '"]')
        entry_link.click()
        delete_button = driver.find_element_by_link_text("DELETE THIS ENTRY")
        delete_button.click()
    if driver.title != "Write - JournalPro":
        driver.find_element_by_link_text("Write").click()

def nice_random_string(string_length=10):
    chars = string.ascii_letters
    return ''.join(random.choice(chars) for i in range(string_length))

def random_string(string_length=10):
    chars = string.printable
    return ''.join(random.choice(chars) for i in range(string_length))

def write_x_entries(driver, x, length, string_generator):
    entries = []
    for i in range(x):
        title_field = driver.find_element_by_id("title")
        body_field = driver.find_element_by_id("body")
        title_field.send_keys(i)
        body_text = string_generator(length)
        body_field.send_keys(body_text)
        entries.append(body_text)
        body_field.submit()

    return entries

if __name__ == "__main__":
    driver = init()
    driver.get("http://127.0.0.1:5000")
    if driver.title != "Sign In - JournalPro":
        logout(driver)
    
    login(driver)
    src = driver.page_source
    is_logged_in = (re.search(r"Invalid username or password", src) == None)
    if not is_logged_in:
        register(driver)
        login(driver)
    
    if driver.title != "Write - JournalPro":
        print("ERROR Incorrect page returned after login")
    
    delete_all_entries(driver)
    if (len(sys.argv) == 0):
        entries = write_x_entries(driver, 10, 1000, nice_random_string)
    else:
        entries = write_x_entries(driver, int(sys.argv[1]), int(sys.argv[2]),
                    random_string if int(sys.argv[3]) else nice_random_string)
    entries_on_page = driver.find_elements_by_id("entry-body")
    entry_contents = list(map((lambda x: x.text), entries_on_page))
    pairs = zip(entries, entry_contents)
    all_equal = True
    for pair in pairs:
        if pair[0] != pair[1]:
            all_equal = False
            print('attempted entry:\n\n{}\n\n'.format(pair[0]))
            print('does not equal entry in app:\n\n{}\n\n'.format(pair[1]))

    if all_equal:
        print('all posts created successfully!')
    time.sleep(5)
    driver.quit()
