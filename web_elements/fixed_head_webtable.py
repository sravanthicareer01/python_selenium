from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
table_data = driver.find_elements(By.XPATH,"//div[@class='tableFixHead']/table//tr//td")
print("total data items in table are:",len(table_data))
target_name="Ivory"
for data in table_data:
    if data.text== target_name:
        print("target_name",target_name,"found in table")
        break
else:
        print("target name",target_name,"not found in table")

#Verify header remain visible while scrolling








