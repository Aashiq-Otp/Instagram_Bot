import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from random_image_selector import should_like_or_not


from insta import driver


def like_by_newsfeed(max_like: int):
    total_liked: int = 0
    fetched_images = 0
    while total_liked <= max_like:
        print(" Starting New Round Number")
        time.sleep(2)
        like_elements_list = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((
                By.XPATH, "//div/section/span/button/div/span/*[contains(@aria-label,'Like')] ")))
        time.sleep(4)
        print("collected")
        fetched_images = fetched_images + len(like_elements_list)
        for like_element in like_elements_list:
            try:
                choice = should_like_or_not()
                if choice:
                    like_element.click()
                    print("Photo ----> liked")
                    total_liked = total_liked + 1
                    time.sleep(random.randrange(2, 8, 1))
                else:
                    print("Photo Skipped ")
            except NoSuchElementException:
                print("No Such Element")
            except ElementNotSelectableException:
                print("Cannot Select Element")
            except StaleElementReferenceException:
                print("Element removed From DOM")
            except WebDriverException:
                print("Not Clickable")
                continue
        driver.execute_script("window.scrollBy(0,9000);")
    print("Program Ended --->  Liked :" + str(total_liked) + "\n Fetched : " + str(fetched_images))
    time.sleep(180)
