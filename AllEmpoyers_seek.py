from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import openpyxl
import string

driverEdge = webdriver.Edge()
driverEdge.get('https://www.seek.com.au/')
driverEdge.implicitly_wait(10)
driverEdge.maximize_window()
filepath = "allEmployers.xlsx"
wb = openpyxl.Workbook()
wb.save(filepath)
wb = openpyxl.load_workbook('allEmployers.xlsx')
ws = wb.active


def brow_group(x):
    group = driverEdge.find_element(By.XPATH, '//a[@title="View all companies that starts with ' + x + '"]')
    return group


def scrap_and_save_to_excel():
    employers = driverEdge.find_elements(By.XPATH, '//ul[@class ="_QTUkujC2vtQ0M2wbj7f"]//a')
    for employer in employers:
        ws.append([employer.text])
    wb.save('allEmployers.xlsx')


# Navigate to company review page
driverEdge.find_element(By.XPATH, '//ul[@data-automation="nav-tabs"]//a[text()="Company Reviews"]').click()
# Navigate to all companies directory page

driverEdge.find_element(By.XPATH, '//a[text()="See all companies"]').click()

# View all companies that start with '#'
brow_group('#').click()
#driver.find_element(By.XPATH, '//a[@title="View all companies that starts with #"]').click()
# Click the first group of current page.
driverEdge.find_element(By.XPATH, '//a[@href ="/companies/browse-more-1"]').click()
employers = driverEdge.find_elements(By.XPATH, '//ul[@class ="_QTUkujC2vtQ0M2wbj7f"]//a')
sleep(3)
scrap_and_save_to_excel()

for q in string.ascii_uppercase:

    print(q, end=" ")
    sleep(3)
    brow_group(q).click()
    sleep(3)

    # get the length of list in current page.
    employerslist = driverEdge.find_elements(By.XPATH, '//ul[@class ="_QTUkujC2vtQ0M2wbj7f"]/li')
    num = len(employerslist)
    for i in range(1, num+1):
        driverEdge.find_element(By.XPATH, '//a[@href ="/companies/browse-' + q.lower() + '-' + str(i) + '"]').click()
        sleep(3)
        scrap_and_save_to_excel()
        sleep(3)
        brow_group(q).click()

driverEdge.quit()


