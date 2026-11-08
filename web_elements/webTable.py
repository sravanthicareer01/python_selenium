from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
heading=driver.find_element(By.XPATH,"//legend[text()='Web Table Example']").text
print(heading)
#print all table data
table1=driver.find_elements(By.XPATH,"//table[@name='courses']/tbody/tr/td")
for table_data in table1:
    print("table data is:",table_data.text)
table_headers_columns=driver.find_elements(By.XPATH,"//table[@name='courses']//tr/th")
print("no.of columns are:",len(table_headers_columns))
for header in table_headers_columns:
    print(header.text)
#count rows and columns
table_rows=driver.find_elements(By.XPATH,"//table[@name='courses']/tbody/tr")
print("no.of rows",len(table_rows))

#print 2nd column
second_column=driver.find_element(By.XPATH,"//table[@name='courses']//th[2]").text
print("second_column name is:",second_column)
#print column3 data, so here need to print in every row we need to print third data as per this website table
third_column_data=driver.find_elements(By.XPATH,"//table[@name='courses']//tbody/tr/td[3]")
for data in third_column_data:
    print(data.text)
#print a specific row
row5=driver.find_elements(By.XPATH,"//table[@name='courses']//tbody/tr[5]")
for data5 in row5:
    print("data in row5 is:",data5.text,end=" ")
#retrieve data in specific cell
cell4=driver.find_element(By.XPATH,"//table[@name='courses']//tbody/tr[5]/td[3]").text
print("data in cell4 is:",cell4)

#search for particular name
target_name="sravanthi"
count=0
whole_data = driver.find_elements(By.XPATH,"//table[@name='courses']//tbody//td")
for data1 in whole_data:
    if data1.text==target_name:
        print("target name",target_name,"found in table")

    else:
        print("target name",target_name,"not found in table")
    break









