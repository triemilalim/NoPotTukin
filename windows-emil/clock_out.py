from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import authenticator as a
import os
import config

def get_code():
    cd = (a.data
          .ClientFile(
            os.environ['AUTHENTICATOR_PASSWORD'])
          .load(
            os.path.expanduser('~/.authenticator/authenticator.data')
          )[0])
    return (a.hotp.HOTP()
            .generate_code_from_time(
                 cd.shared_secret(),
                 code_length=cd.password_length(),
                 period=cd.period())[0])

def clockOutEdjpb():
    
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

    sleep(3)

def clockOutOA():
    
    sleep(4)

    loginButton = driver.find_elements_by_xpath("//div[@id='container-3']/toolbar/div/div[2]/div/button")[0]
    loginButton.click()

    wait.until(EC.presence_of_element_located((
        By.ID, 'username')))
    inputUser = driver.find_elements_by_xpath("//input[@id='username']")[0]
    inputUser.click()
    inputUser.send_keys(config.username)
    inputUser = driver.find_elements_by_xpath("//input[@id='password']")[0]
    inputUser.click()
    inputUser.send_keys(config.passwordOA)

    inputUser.send_keys(Keys.RETURN)
    
    sleep(2)

    try:
        authCode = get_code()
        inputUser = driver.find_elements_by_xpath("//input[@id='code']")[0]
        inputUser.click()
        inputUser.send_keys(authCode)
        inputUser.send_keys(Keys.RETURN)
    except:
        pass

    sleep(2)
    # xpath tombol clock:
    clockButton = driver.find_elements_by_xpath("//div[@id='container-3']/toolbar/mat-toolbar/div/div[2]/div/clockin/button/span/div")[0]
    clockButton.click()
    sleep(2)

    yakinButton = driver.find_elements_by_xpath("//mat-dialog-container/app-dialog-absen/div/div[2]/button[1]")[0]
    yakinButton.click()

    sleep(3)



try:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)
    # Buka Nadine
    driver.get(config.url_nadine)
    print("Mulai clock out nadine at", datetime.now())
    clockOutOA()
    print("Selesai Clock out nadine at", datetime.now())
except Exception as e:
    print("error saat clock out oa: ", e) 
    print("coba lagi ")
    clockOutOA()
finally:
    driver.quit()

# try:
#     driver = webdriver.Chrome()
#     wait = WebDriverWait(driver, 30)
#     # Buka Edjpb
#     print("Mulai clock out edjpb at", datetime.now())
#     driver.get(config.url_edjpb)
#     clockOutEdjpb()
#     print("Selesai clock out edjpb at", datetime.now())
# except Exception as ee:
#     print("error saat clock out edjpb: ", ee) 
#     print("coba lagi ")
#     clockOutEdjpb()
# finally:
#     driver.quit()


print("All done, self destructing at", datetime.now())
