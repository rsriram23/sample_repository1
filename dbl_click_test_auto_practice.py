from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

dr=webdriver.Chrome()
dr.get('https://testautomationpractice.blogspot.com/')
# print('field 1->',dr.find_element("id","field1").get_attribute('value'))
# dr.find_element("id","field1").click()
sleep(5)
act_obj=ActionChains(dr)
act_obj.double_click(dr.find_element('xpath',"//button[text()='Copy Text']")).perform()
sleep(2)
print('field 2->',dr.find_element('id',"field2").get_attribute('value'))
sleep(10)
print("Enabled webhook for github auto triggering jenkins")
