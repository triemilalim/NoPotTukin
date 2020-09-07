from datetime import datetime

from selenium import webdriver

from time import sleep

from selenium.webdriver.common.keys import Keys 

print("Mulai clock in at", datetime.now())
password = 'putyourpasswordhere'

driver = webdriver.Safari()

# Open the website
driver.get('https://edjpb.kemenkeu.go.id/login.php')

sleep(10)

# Locate id and password
id_box = driver.find_element_by_name('username')
pass_box = driver.find_element_by_name('password')

# Send login information
id_box.send_keys('putyourNIPhere')
pass_box.send_keys(password)
pass_box.send_keys(Keys.RETURN)

sleep(10)

driver.find_element_by_partial_link_text('[detil]').click()

sleep(10)

driver.find_element_by_link_text('Clock-in').click()

driver.quit()
print("All done, self destructing at", datetime.now())