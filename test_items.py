from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_has_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30) # можно убедитьтся, что язык соответствует выбранному
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_cart_button, "Button 'Add to cart' is not found on the page"