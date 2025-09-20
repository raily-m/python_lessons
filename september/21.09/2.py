from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/scroll")

wait = WebDriverWait(driver, 10)

def count_quotes():
    return len(driver.find_elements(By.CSS_SELECTOR, ".quote")) #помогает нам понять прибавилость элементов или осталось столько же

prev_count = count_quotes()

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #определяем высоту страницы и от нуля прокручиваем в самый низ

    try:
        wait.until(lambda x: len(x.find_elements(By.CSS_SELECTOR, "quote") > prev_count))
        prev_count = count_quotes()
        time.sleep(1)

    except Exception:
        break
time.sleep(10)
driver.quit()
