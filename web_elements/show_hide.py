from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
heading=driver.find_element(By.XPATH,"//legend[text()='Element Displayed Example']").text
print(heading)
show_button=driver.find_element(By.ID,"show-textbox")
hide_button=driver.find_element(By.XPATH,"//input[@id='hide-textbox']")
text_box=driver.find_element(By.XPATH,"//input[@id='displayed-text']")
hide_button.click()
assert not text_box.is_displayed()
print("PASS:Text box not displayed after clicking on HIDE button ")
show_button.click()
assert text_box.is_displayed()
print("PASS:Text box is displayed after clicking oon SHOW button")
driver.quit()
