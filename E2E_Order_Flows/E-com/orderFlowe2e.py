from openpyxl.styles.builtins import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
#url verification
assert driver.current_url=="https://rahulshettyacademy.com/client/#/auth/login"
email="selenium_practice10@gmail.com"
password="Mypassword@123"
#Login
title_login=driver.find_element(By.CSS_SELECTOR,".p-5 h1").text
print(title_login)
driver.find_element(By.ID,"userEmail").send_keys(email)
driver.find_element(By.XPATH,"//input[@id='userPassword']").send_keys(password)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
wait = WebDriverWait(driver, 10, poll_frequency=0.1)
toast = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(),'Login Successful')]")
    )
)

print(toast.text)
#blinking text we need to use get_attribute to capture text
#blinking_text=driver.find_element(By.XPATH,"//a[@class='blinkingText']").get_attribute('textContent')
#print(blinking_text)
#capture all the products in page
products=driver.find_elements(By.CSS_SELECTOR,".card-body h5 b")
print("total no.of products",len(products))
target="ADIDAS ORIGINAL"
for product in products:
    print(product.text)
    if product.text==target:
        driver.find_element(By.XPATH,"//*[@class='card-body']/child::button[@class='btn w-10 rounded']").click()
    break
wait = WebDriverWait(driver, 10, poll_frequency=0.1)

added_to_cart = wait.until(
EC.visibility_of_element_located(
(By.XPATH, "//*[contains(text(),'Product Added To Cart')]")))

print(added_to_cart.text)
driver.find_element(By.XPATH,"//button[@routerlink='/dashboard/cart']").click()
driver.save_screenshot("cartpage.png")
assert driver.current_url=="https://rahulshettyacademy.com/client/#/dashboard/cart"
cart_page_text=driver.find_element(By.XPATH,"//*[@class='heading cf']/child::h1").text
assert cart_page_text=="My Cart"
cart_product=driver.find_element(By.CSS_SELECTOR,".cartSection h3").text
print(cart_product)
assert cart_product==target
driver.find_element(By.XPATH,"//button[text()='Checkout']").click()
assert driver.current_url=="https://rahulshettyacademy.com/client/#/dashboard/order?prop=%5B%226960eae1c941646b7a8b3ed3%22%5D"
driver.save_screenshot("paymentPage.png")
paymentType=driver.find_element(By.CSS_SELECTOR,".payment__types .payment__type--cc").text
print("Payment type is:",paymentType)
date_dropdowns=driver.find_elements(By.XPATH,"//*[@class='input ddl']")
print(len(date_dropdowns))
dropdown_day=Select(date_dropdowns[0])
dropdown_year=Select(date_dropdowns[1])
dropdown_day.select_by_visible_text("07")
dropdown_year.select_by_visible_text("19")
shipping_email=driver.find_element(By.XPATH,"//div[@class='user__name mt-5']/label").text
print(shipping_email)
assert email==shipping_email
driver.find_element(By.XPATH,"//input[@placeholder='Select Country']").send_keys("ind")
list_countries = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".ta-results button")
    )
)
print("no.of countries",len(list_countries))
for country in list_countries:
    if country.text.strip()=="India":
        country.click()
        break
driver.save_screenshot("shipping.png")
country_selected=driver.find_element(By.XPATH,"//input[@placeholder='Select Country']").get_attribute("value")
print("selected country is:",country_selected)
driver.find_element(By.XPATH,"//a[text()='Place Order ']").click()
#confirmation=driver.find_element(By.CLASS_NAME,"hero-primary").text
#print(confirmation)
confirmation = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "hero-primary"))
).text

print(confirmation)
order_Number=driver.find_element(By.CSS_SELECTOR,".em-spacer-1 .ng-star-inserted").text
print(order_Number)
ordered_item=driver.find_element(By.CSS_SELECTOR,".order-summary .m-3 .title").text
driver.save_screenshot("confirmation.png")
print(ordered_item)
assert ordered_item==target



















