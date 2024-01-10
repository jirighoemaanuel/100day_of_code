from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.python.org/")

# year = driver.find_element(By.CLASS_NAME, value="say-no-more")
dates = driver.find_elements(By.TAG_NAME, value="time")
names = driver.find_elements(
    By.CSS_SELECTOR, value='#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > a')

event_zip = zip(dates, names)

event = {}
counter = 0
for date, name in event_zip:
    print(date.text, name.text)
    event[f"{counter}"] = {"time": date.text,
                           "name": name.text
                           }
    counter += 1

print(event)
driver.quit()
