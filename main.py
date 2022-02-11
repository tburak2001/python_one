from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://championklf.com/fpm")

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/user/login')]"))
#     )
#     element.click()
# except TimeoutException:
#     print("Time exceeded!")
#
# time.sleep(3)
#
# try:
#     input_username = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))
#     )
#     input_password = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
#     )
#
#     input_username.send_keys("ТЕД")
#     input_password.send_keys("zq1376d2ag")
#
#     entry = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//input[@id='submit']"))
#     )
#
#     entry.click()
# except TimeoutException:
#     print("Time exceeded!")
time.sleep(5)
try:
    elems = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//p[contains(@class, 'fpm_team')]"))
    )
    actions = ActionChains(driver)

    for elem in elems:
        actions.move_to_element(elem).perform()
        elem.click()

        time.sleep(2)
        # players = WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By.XPATH, "//div[@class='fpm_player']/span/a"))
        # )
        #
        # for player in players:
        #     print(player.text)
        # time.sleep(0.5)
        elem.click()

    time.sleep(4)

except TimeoutException:
    print("Time exceeded!")
driver.quit()


