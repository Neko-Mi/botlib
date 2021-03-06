import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


URL = 'https://mangalib.me/user/351818'

LOGIN = 'asdf@asdf.com'
PASSWORD = 'asdfasdfasfd'


def sendmessage(browser, i):
    elem = browser.find_element_by_xpath("//div["
                                         "@class='post-reply-placeholder__text']") # Find the query box
    elem.click()
    elem = browser.find_element_by_xpath("//div["
                                         "@class='ql-editor ql-blank']")  #
    elem.send_keys("hello" + str(i))
    time.sleep(0.2)
    elem = browser.find_element_by_xpath("//button["
                                         "@class='button button_primary button_md button_primary']")
    elem.click()


def domessage(browser):
    i = 0
    while i < 60000:
        sendmessage(browser, i)
        time.sleep(0.2)
        i += 1


def ignoring(browser):
    time.sleep(0.01)
    elem = browser.find_element_by_xpath("//div["
                                         "@id='block-toggle']")
    elem.click()


def doignor(browser):
    elem = browser.find_element_by_xpath("//button["
                                         "@class='button button_sm button_icon']") # Find the query box
    elem.click()
    i = 0
    while i < 60000:
        j = 0
        while j < 10:
            time.sleep(0.04)
            ignoring(browser)
            j += 1
        i += 1
        print(j*i)


def auth(browser, login, password):
    elem = browser.find_element_by_xpath("//button["
                                         "@data-open-modal='#sign-in-modal']")
    elem.click()

    elem = browser.find_element_by_xpath("//input["
                                         "@name='email']")

    elem.send_keys(login + Keys.RETURN)
    elem = browser.find_element_by_xpath("//input["
                                         "@type='password']")

    elem.send_keys(password + Keys.RETURN)
    time.sleep(1)


def start(url, login, password):
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url) 

    auth(browser, login, password)

    browser.get(url)

    doignor(browser)


if __name__ == '__main__':
    start(URL, LOGIN, PASSWORD)