from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
driver.find_element(By.ID,"autocomplete").send_keys("ind")
countries=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']")
print(len(countries))
for country in countries:
    print(country.text)
for country in countries:
    if country.text=="India":
        country.click()
Selected_value=driver.find_element(By.ID,"autocomplete").get_attribute("value")
print(Selected_value)
driver.quit()
