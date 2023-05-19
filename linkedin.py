from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import pyautogui as p
from python_imagesearch import imagesearch
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
action = ActionChains(browser)  # ACTION CHAINSI BROWSERE GOSTERME

browser.get("https://www.linkedin.com")
time.sleep(2)

page = browser.find_element(By.XPATH, "/html/body/nav/div/a[2]")
page.click()
time.sleep(0.5)
username = browser.find_element(By.XPATH, "//*[@id='username']")
password = browser.find_element(By.XPATH, "//*[@id='password']")

username.send_keys("<youremail>")
time.sleep(0.5)
password.send_keys("<yourpassword>")
time.sleep(0.5)
sign_in = browser.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
time.sleep(0.5)
sign_in.click()

time.sleep(2)
page = 14
beginning_url ="https://www.linkedin.com/search/results/people/?keywords=ankara%20%C3%BCniversitesi%20bilgisayar&origin=CLUSTER_EXPANSION&page="
url = beginning_url + str(page)
browser.get(url)
time.sleep(1)
sayac = 0




id = browser.find_element(By.CSS_SELECTOR, ".entity-result__actions .artdeco-button .artdeco-button__text")
length = len(id.text)
last2 = int(id[length - 2:])
final = "ember" + str(last2)
for i in range(10):
    for j in range(10):
        try:
            click_me = browser.find_element(By.ID, final)

            span_text = click_me.find_element(By.CLASS_NAME, "artdeco-button__text")
            print(span_text.text)
            if span_text.text == "Bağlantı kur":
                click_me.click()
            time.sleep(0.5)
        except:
            pass
        try:
            dismiss = browser.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            dismiss.click()
        except:
            pass
        last2 = last2 + 1
        final = "ember" + str(last2)
        time.sleep(0.5)

    page = page + 1
    url = beginning_url + str(page)
    browser.get(url)
    time.sleep(2)
    id = browser.find_element(By.CSS_SELECTOR, ".entity-result__actions .artdeco-button .artdeco-button__text")
    print(id.text)


    last2 = int(id[length - 2:])
    final = "ember" + str(last2)






