from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import config

driver = webdriver.Chrome()

print("Mulai clock in edjpb at", datetime.now())

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

print("Berhasil clock in edjpb at", datetime.now())

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

print("Selesai lapor kesehatan at", datetime.now())
sleep(3)
print("Pindah ke nadine at", datetime.now())

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
wfhChecklist = driver.find_elements_by_xpath(
    "//div[contains(@class, 'mat-radio-label-content') and text()='WFH']")[0]
wfhChecklist.click()
sehatChecklist = driver.find_elements_by_xpath(
    "//div[contains(@class, 'mat-radio-label-content') and text()='Sehat']")[0]
sehatChecklist.click()

btnSimpan = driver.find_elements_by_xpath(
    "//span[contains(@class, 'mat-button-wrapper') and text()='Ya, Yakin!']")[0]
btnSimpan.click()

print("Selesai Clock in nadine at", datetime.now())

wait.until(EC.invisibility_of_element_located((
    By.ID, 'spinner')))

sleep(3)

driver.quit()
print("All done, self destructing at", datetime.now())
