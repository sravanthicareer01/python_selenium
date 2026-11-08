from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
print(driver.title)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name=driver.find_element(By.XPATH,"//legend[text()='Switch Window Example']").text
print("name of the element is:",name)
driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
openWindow=driver.window_handles
driver.switch_to.window(openWindow[1])
new_window_text=driver.find_element(By.XPATH,"//span[@class='inline-block']").text
print("Text in new window is:",new_window_text)
driver.quit()







