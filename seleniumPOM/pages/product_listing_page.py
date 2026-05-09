from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ProductListingPage:
    PRODUCT.TITLES=(By.CSS_SELECTOR,"a h2 span")
    def __init__(self,driver):
        