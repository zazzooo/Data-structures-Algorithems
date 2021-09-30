
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriverfrom selenium.webdriver import manage

driver = webdriver.Firefox(executable_path = r'C:\Users\zazzo\OneDrive\Documenti\geckodriver.exe')

driver.get('https://www.hertie-school.org/en/')

driver.implicitly_wait(10)

# driver.manage().deleteAllCookies()
coockie = driver.find_elements_by_class_name("select-all btn btn--primary")
for chk in coockie:
    print(chk)
    chk.click()




# search = driver.find_elements_by_name('q')
# search.send_keys('MDS')
# search.send_keys(Keys.RETURN)
