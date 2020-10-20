from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import telepot
import config

opts = Options()
opts.headless = True
opts.add_argument('--disable-gpu')
opts.add_argument("--window-size=1366,768")
driver = webdriver.Chrome(options=opts)
isWFH = True

if config.botToken != '':
    bot = telepot.Bot(config.botToken)
    response = bot.getUpdates()
    if len(response)>0:
        if response[len(response)-1]['message']['text'].lower() == 'wfo' or response[len(response)-1]['message']['text'].lower() == 'wao':
            isWFH = False
    bot.sendMessage(config.privateId,
                    "Start clock in at %s as %s" % (format(datetime.now()), 'WFH' if isWFH else 'WaO'))

# Open the website
driver.get(config.url_edjpb)

# Locate id and password
id_box = driver.find_element_by_name('username')
pass_box = driver.find_element_by_name('password')

# Send login information
id_box.send_keys(config.username)
pass_box.send_keys(config.password)
sleep(1)
pass_box.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 30)

wait.until(EC.presence_of_element_located((
    By.XPATH, '//a[contains(text(),"[detil]")]')))

driver.find_element_by_partial_link_text('[detil]').click()

wait.until(EC.presence_of_element_located((
    By.XPATH, '//a[contains(text(),"Clock-in")]')))

driver.find_element_by_link_text('Clock-in').click()

if config.botToken != '':
    bot.sendMessage(config.privateId,
                    "Clock in edjpb at {}".format(datetime.now()))

# Lapor Kesehatan
wait.until(EC.presence_of_element_located((
    By.XPATH, '//label[contains(@for, "data2[1]")]')))

for x in range(1, 12):
    button = driver.find_elements_by_xpath(
        '//label[contains(@for, "data2[{}]")]'.format(x))[0]
    button.click()

btnSimpan = driver.find_elements_by_xpath(
    "//button[contains(@class, 'btn-warning') and text()='Simpan']")[0]
btnSimpan.click()

# set WaO
if not isWFH:
    sleep(1)
    driver.find_element_by_partial_link_text('WFH').click()

sleep(3)
if config.botToken != '':
    driver.save_screenshot("screenshot.png")
    bot.sendPhoto(config.privateId, open('screenshot.png', 'rb'))

driver.get(config.url_nadine)

if driver.current_url == config.url_nadine:
    driver.get(config.url_nadine + 'index/index/')
    wait.until(EC.presence_of_element_located((
        By.ID, 'username')))
    inputUser = driver.find_elements_by_xpath("//input[@id='username']")[0]
    inputUser.click()
    inputUser.send_keys(config.username)
    inputUser = driver.find_elements_by_xpath("//input[@id='password']")[0]
    inputUser.click()
    inputUser.send_keys(config.password)
    inputUser = driver.find_elements_by_xpath(
        "//button[@class='login100-form-btn']")[0]
    inputUser.click()

wait.until(EC.presence_of_element_located((
    By.XPATH, "//div[contains(@class, 'title')]")))

# Buka menu Absen
driver.get(config.url_nadine + config.absen_nadine)

wait.until(EC.invisibility_of_element_located((
    By.ID, 'spinner')))

btnClockIn = driver.find_elements_by_xpath(
    "//span[contains(@class, 'mat-button-wrapper') and text()='Clock In']")[0]
btnClockIn.click()

wait.until(EC.presence_of_element_located((
    By.XPATH, '//app-dialog-absen')))
if isWFH:
    wfhChecklist = driver.find_elements_by_xpath(
        "//div[contains(@class, 'mat-radio-label-content') and text()='WFH']")[0]
else:
    wfhChecklist = driver.find_elements_by_xpath(
        "//div[contains(@class, 'mat-radio-label-content') and text()='Non WFH']")[0]

wfhChecklist.click()
sehatChecklist = driver.find_elements_by_xpath(
    "//div[contains(@class, 'mat-radio-label-content') and text()='Sehat']")[0]
sehatChecklist.click()

btnSimpan = driver.find_elements_by_xpath(
    "//span[contains(@class, 'mat-button-wrapper') and text()='Ya, Yakin!']")[0]
btnSimpan.click()

if config.botToken != '':
    bot.sendMessage(config.privateId,
                    "Clock in Nadine at {}".format(datetime.now()))

wait.until(EC.invisibility_of_element_located((
    By.ID, 'spinner')))

sleep(3)
if config.botToken != '':
    driver.save_screenshot("screenshot.png")
    bot.sendPhoto(config.privateId, open('screenshot.png', 'rb'))

driver.quit()
print("All done, self destructing at", datetime.now())
