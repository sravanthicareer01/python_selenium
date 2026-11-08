from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
# select radio2 directly
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")#opening website
# driver.maximize_window()
# print(driver.title)
# radio2=driver.find_element(By.XPATH,"//input[@value='radio2']")
# radio2.click()
# print("radio2 button is selected or not:",radio2.is_selected())
# assert radio2.is_selected()
# driver.quit()

# Select radio3 dynamically
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radio_buttons=driver.find_elements(By.XPATH,"//input[@name='radioButton']")
no_of_radio_buttons=len(radio_buttons)
for radio in radio_buttons:
    if radio.get_attribute("value")=="radio3":
        radio.click()
print("is radio3 button is clicked or not",radio.is_selected())
driver.quit()
