from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Locate the dropdown
static_dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))

# Select an option by visible text
static_dropdown.select_by_visible_text("Option2")
selected_text=static_dropdown.first_selected_option.text
print(selected_text)

driver.quit()