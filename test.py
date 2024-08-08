from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome()

try:
    driver.get('https://www.saucedemo.com/')

    username = 'standard_user'
    password = 'secret_sauce'
    driver.find_element(By.ID, 'user-name').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)

    add_to_cart_buttons = driver.find_elements(By.XPATH, '//button[contains(@data-test, "add-to-cart")]')

    random_buttons = random.sample(add_to_cart_buttons, 2)

    items_added = []
    for button in random_buttons:
        item_name = button.get_attribute('data-test').replace('add-to-cart-', '').replace('-', ' ').title()
        items_added.append(item_name)
        button.click()
        time.sleep(1)

    print(f"Usuario usado: {username}")
    print(f"Productos agregados al carrito: {', '.join(items_added)}")

    driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//button[@data-test="checkout"]').click()
    time.sleep(2)

    driver.find_element(By.ID, 'first-name').send_keys('John')
    driver.find_element(By.ID, 'last-name').send_keys('Doe')
    driver.find_element(By.ID, 'postal-code').send_keys('10001')

    driver.find_element(By.ID, 'continue').click()
    time.sleep(2)

    driver.find_element(By.ID, 'finish').click()
    time.sleep(2)

    confirmation_text = driver.find_element(By.XPATH, '//h2[text()="Thank you for your order!"]').text
    assert confirmation_text == "Thank you for your order!"
    print(f"Confirmación: {confirmation_text}")

finally:
    driver.quit()
