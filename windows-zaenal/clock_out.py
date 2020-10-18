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
import xlrd
import pandas


opts = Options()
opts.headless = True
opts.add_argument('--disable-gpu')
opts.add_argument("--start-fullscreen")
driver = webdriver.Chrome(options=opts)
wait = WebDriverWait(driver, 30)

if config.botToken != '':
    bot = telepot.Bot(config.botToken)


def inputTask(data):
    if data[1] == data[1]:
        # Add new Task
        sleep(1)
        wait.until(EC.invisibility_of_element_located((
            By.ID, 'spinner')))
        addTask = driver.find_elements_by_xpath(
            "//mat-icon[text()='add']")[0]
        addTask.click()

        # Tusi / non Tusi
        wait.until(EC.presence_of_element_located((
            By.XPATH, "//mat-radio-button[contains(@class, 'mat-radio-button')]")))
        wait.until(EC.invisibility_of_element_located((
            By.ID, 'spinner')))
        rdTusi = driver.find_elements_by_xpath(
            "//div[contains(@class, 'mat-radio-label-content')]")
        if data[0] == 'T':
            rdTusi[0].click()
        else:
            rdTusi[1].click()

        # Nama Tugas
        field = driver.find_elements_by_xpath(
            "//input[@formcontrolname='Tugas']")[0]
        field.send_keys(data[3])

        # Rincian Tugas
        field = driver.find_elements_by_xpath(
            "//textarea[@formcontrolname='Rincian']")[0]
        field.send_keys(data[3])

        # Jam Mulai
        field = driver.find_elements_by_xpath(
            "//input[@placeholder='HH']")[0]
        field.clear()
        field.send_keys(str(data[1])[0:2])
        field = driver.find_elements_by_xpath(
            "//input[@placeholder='MM']")[0]
        field.clear()
        field.send_keys(str(data[1])[3:6])

        # Jam Selesai
        field = driver.find_elements_by_xpath(
            "//input[@placeholder='HH']")[1]
        field.clear()
        field.send_keys(str(data[2])[0:2])
        field = driver.find_elements_by_xpath(
            "//input[@placeholder='MM']")[1]
        field.clear()
        field.send_keys(str(data[2])[3:6])

        # Norma Waktu
        field = driver.find_elements_by_xpath(
            "//input[@formcontrolname='NormaWaktu']")[0]
        field.send_keys(data[5])

        # Simpan
        button = driver.find_elements_by_xpath(
            "//span[contains(@class, 'mat-button-wrapper') and text()='Simpan']")[0]
        button.click()


def inputTaskLocal():
    # Buka file
    workbook = xlrd.open_workbook(
        "HitungJamTask.xlsx", on_demand=True)
    worksheet = workbook.sheet_by_index(0)

    for row in range(0, worksheet.nrows):
        if not worksheet.cell_value(row, 3):
            break

        # Add new Task
        sleep(1)
        wait.until(EC.invisibility_of_element_located((
            By.ID, 'spinner')))
        addTask = driver.find_elements_by_xpath(
            "//mat-icon[text()='add']")[0]
        addTask.click()

        # Tusi / non Tusi
        wait.until(EC.presence_of_element_located((
            By.XPATH, "//mat-radio-button[contains(@class, 'mat-radio-button')]")))
        wait.until(EC.invisibility_of_element_located((
            By.ID, 'spinner')))
        rdTusi = driver.find_elements_by_xpath(
            "//div[contains(@class, 'mat-radio-label-content')]")
        if worksheet.cell_value(row, 0) == 'T':
            rdTusi[0].click()
        else:
            rdTusi[1].click()

        # Nama Tugas
        field = driver.find_elements_by_xpath(
            "//input[@formcontrolname='Tugas']")[0]
        field.send_keys(worksheet.cell_value(row, 3))

        # Rincian Tugas
        field = driver.find_elements_by_xpath(
            "//textarea[@formcontrolname='Rincian']")[0]
        field.send_keys(worksheet.cell_value(row, 3))

        # Jam Mulai
        jamMulai = int(worksheet.cell_value(row, 1) * 24 * 3600)
        field = driver.find_elements_by_xpath(
            "//input[@placeholder='HH']")[0]
        field.clear()
        field.send_keys(jamMulai//3600)
        field = driver.find_elements_by_xpath(
            "//input[@placeholder='MM']")[0]
        field.clear()
        field.send_keys((jamMulai % 3600)//60)

        # Jam Selesai
        jamSelesai = int(worksheet.cell_value(row, 2) * 24 * 3600)
        field = driver.find_elements_by_xpath(
            "//input[@placeholder='HH']")[1]
        field.clear()
        field.send_keys(jamSelesai//3600)
        field = driver.find_elements_by_xpath(
            "//input[@placeholder='MM']")[1]
        field.clear()
        field.send_keys((jamSelesai % 3600)//60)

        # Rincian Tugas
        field = driver.find_elements_by_xpath(
            "//input[@formcontrolname='NormaWaktu']")[0]
        if worksheet.cell_type(row, 4) == xlrd.XL_CELL_EMPTY:
            worksheet._cell_values[row][4] = 0
        minus = int(worksheet.cell_value(row, 4))
        field.send_keys((jamSelesai-jamMulai)//60-minus)

        # Simpan
        button = driver.find_elements_by_xpath(
            "//span[contains(@class, 'mat-button-wrapper') and text()='Simpan']")[0]
        button.click()


def clockOut():
    if config.botToken != '':
        bot.sendMessage(config.privateId,
                        "Start clock out at {}".format(datetime.now()))

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

    wait.until(EC.presence_of_element_located((
        By.XPATH, '//a[contains(text(),"[detil]")]')))

    driver.find_element_by_partial_link_text('[detil]').click()

    wait.until(EC.presence_of_element_located((
        By.XPATH, '//a[contains(text(),"Clock-out")]')))

    driver.find_element_by_link_text('Clock-out').click()

    wait.until(EC.presence_of_element_located((
        By.XPATH, '//button[contains(text(),"Clock-out")]')))

    driver.find_element_by_xpath("//button[1]").click()

    if config.botToken != '':
        bot.sendMessage(config.privateId,
                        "Clock out edjpb at {}".format(datetime.now()))

    sleep(3)
    if config.botToken != '':
        driver.save_screenshot("screenshot.png")
        bot.sendPhoto(config.privateId, open('screenshot.png', 'rb'))

    # Buka Nadine
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

    # Buka menu Task
    driver.get(config.url_nadine + config.task_nadine)

    # Loop input task
    # Jika pakai google sheet
    if config.sheetId != '':
        sh.apply(inputTask, axis=1)
    # Jika menggunakan excel
    elif config.localTaskxls != '':
        inputTaskLocal()

    sleep(1)
    wait.until(EC.invisibility_of_element_located((
        By.ID, 'spinner')))
    button = driver.find_elements_by_xpath(
        "//span[contains(@class, 'mat-button-wrapper') and text()='Kirim Semua']")[0]
    button.click()

    sleep(1)
    button = driver.find_elements_by_xpath(
        "//span[contains(@class, 'mat-button-wrapper') and text()='OK']")[0]
    button.click()

    sleep(3)
    if config.botToken != '':
        driver.save_screenshot("screenshot.png")
        bot.sendPhoto(config.privateId, open('screenshot.png', 'rb'))

    # Buka menu Absen
    driver.get(config.url_nadine + config.absen_nadine)

    wait.until(EC.invisibility_of_element_located((
        By.ID, 'spinner')))

    btnClockIn = driver.find_elements_by_xpath(
        "//span[contains(@class, 'mat-button-wrapper') and text()='Clock Out']")[0]
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

    if config.botToken != '':
        bot.sendMessage(config.privateId,
                        "Clock out Nadine at {}".format(datetime.now()))

    wait.until(EC.invisibility_of_element_located((
        By.ID, 'spinner')))

    sleep(3)
    if config.botToken != '':
        driver.save_screenshot("screenshot.png")
        bot.sendPhoto(config.privateId, open('screenshot.png', 'rb'))

    driver.quit()
    print("All done, self destructing at", datetime.now())


# Mulai absen jika total norma waktu >400
while True:
    print ('sini')
    if config.sheetId != '':
        print (f'https://docs.google.com/spreadsheets/d/{config.sheetId}/export?format=csv')
        sh = pandas.read_csv(
            f'https://docs.google.com/spreadsheets/d/{config.sheetId}/export?format=csv')
        print ('sini')
        if int(sh['Total'][0]) > 400:
            clockOut()
            break
        else:
            print('waiting...')
            sleep(10)
    else:
        clockOut()
