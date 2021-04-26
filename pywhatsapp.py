from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

name = input()
msg = input()

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
sleep(4)

search = driver.find_element_by_xpath(
    "//*[@id=\"side\"]/div[1]/div/label/div/div[2]")
sleep(1)
search.click()
search.send_keys(name)
sleep(2)

receiver = driver.find_element_by_xpath(
    "//*[@id=\"pane-side\"]/div[1]/div/div/div[1]/div/div/div[2]")
sleep(1)
receiver.click()
sleep(1)

msgbox = driver.find_element_by_xpath(
    "//*[@id=\"main\"]/footer/div[1]/div[2]/div/div[2]")
msgbox.click()
msgbox.send_keys(msg)

send = driver.find_element_by_xpath(
    "//*[@id=\"main\"]/footer/div[1]/div[3]/button/span")
send.click()
