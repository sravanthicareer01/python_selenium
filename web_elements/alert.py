from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
text1=driver.find_element(By.XPATH,"//legend[text()='Switch To Alert Example']").text
print(text1)
driver.find_element(By.ID,"name").send_keys("sravanthi")
driver.find_element(By.ID,"alertbtn").click()
alert1=driver.switch_to.alert
print("text present in alert box",alert1.text)
message=alert1.text
alert1.accept()
assert "sravanthi" in message
driver.quit()
