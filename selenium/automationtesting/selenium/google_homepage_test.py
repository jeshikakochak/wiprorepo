
from selenium import webdriver
import time
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser=input("wht browser do u want to use")
match(browser.lower()):
    case "chrome":
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    case "edge":
        driver=webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
    case _:
        print("Enter VALID browser!!!")

driver.get("https://google.com")

time.sleep(50)
pagetitle=driver.title
if pagetitle=='Google':
    print("google homepage loaded-pass")
else:
    print("google homepage not loaded-fail")

driver.quit()

