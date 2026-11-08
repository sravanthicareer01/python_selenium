import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
window_opened=driver.window_handles
driver.switch_to.window(window_opened[1])
text_child1=driver.find_element(By.XPATH,"//h3").text
print(text_child1)
driver.switch_to.window(window_opened[0])
parent1=driver.find_element(By.TAG_NAME,"h3").text
print(parent1)
driver.quit()

