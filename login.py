from driver import driver
import time


def user_login(username, password):
    driver.get("http://instagram.com")
    time.sleep(5)
    username_loc = driver.find_element_by_xpath("//input[@name='username']")
    password_loc = driver.find_element_by_xpath("//input[@name='password']")
    login_button = driver.find_element_by_xpath("//div/button/div[text()='Log In']")
    username_loc.send_keys(username)
    password_loc.send_keys(password)
    login_button.click()
    time.sleep(5)
    dismiss_elem_loc = driver.find_element_by_xpath("//button[text()='Not Now']")
    dismiss_elem_loc.click()
    time.sleep(5)
    notification_elem_loc = driver.find_element_by_xpath("//button[text()='Not Now']")
    notification_elem_loc.click()
    time.sleep(10)

