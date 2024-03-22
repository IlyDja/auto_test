from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_busket_button(browser):
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    except:
        raise AssertionError("the button doesn't presence")
