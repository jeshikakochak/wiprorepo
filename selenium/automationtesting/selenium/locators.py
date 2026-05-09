import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
driver.get("https://google.com")
search_input=driver.find_element(By.ID,"APjFqb")
search_input.send_keys("selenium")
time.sleep(3)
search_input.clear()
time.sleep(30)
and_example=driver.find_element(By.XPATH,)
print(f"AND Example -> found with both conditions :{and_example.text}")
or_example=driver.find_element(By.XPATH,)
print(f"or example ->found with or conditions:{or_example.text}")
rows=driver.find_elements(By.XPATH,)
print(f"child example->{len(rows)}columns in the first table")
email_cell=driver.find_element(By.XPATH,)
parent_row=driver.find_element(By.XPATH,)
print(f"parent example->email'{email_cell.text}'belongs to row with first_name: "
      f"{parent_row.find_element(By.XPATH,)}")
driver.quit()