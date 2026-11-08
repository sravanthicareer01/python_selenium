from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.implicitly_wait(5)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='singleframe']"))
frame_text=driver.find_element(By.XPATH,"//h5[text()='iFrame Demo']").text
print(frame_text)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("sravanthi")
updated_text=driver.find_element(By.XPATH,"//input[@type='text']").get_attribute('value')
print(updated_text)
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//a[text()='WebTable']").click()
driver.quit()




