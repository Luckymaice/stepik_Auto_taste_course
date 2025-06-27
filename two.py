from selenium import webdriver
import math
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:

    human = ["Ivan","Petrov","kobyakov@mail.ru","89393535678", "Chezia"]
    driver.get("https://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    book_button = driver.find_element(By.ID, 'book')
    book_button.click()

    value = driver.find_element(By.ID, 'input_value').text

    input_button = driver.find_element(By.ID, 'answer')
    driver.execute_script("return arguments[0].scrollIntoView(true);", input_button)
    input_button.send_keys(calc(value))

    button = driver.find_element(By.ID, 'solve')
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    driver.quit()
