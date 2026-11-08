from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value")== "option1":
        checkbox.click()
        assert checkbox.is_selected()
        print("is checkbox selected:",checkbox.is_selected())
