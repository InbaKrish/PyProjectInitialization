import sys
from selenium import webdriver
from usercredentials import *
from selenium.webdriver.chrome.options import Options

un = un
pwd = pwd
fname = fname

opt = Options()
opt.add_argument("--headless")
browser = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=opt)
browser.get('http://github.com/login')


def remove():
    print("\n Script is deleting your remote repository in headless mode...wait for sometime")
    browser.find_elements_by_xpath(
        "//input[@name='login']")[0].send_keys(un)
    browser.find_elements_by_xpath(
        "//input[@name='password']")[0].send_keys(pwd)
    browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
    browser.get('https://github.com/' + un + chr(47) + fname + '/settings')
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')[0].click()
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0].send_keys(un + chr(47)+fname)
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')[0].click()
    print("\nSuccessfully Removed "+fname +"remote repository in GitHub")


if __name__ == "__main__":
    remove()
    print("\n Opening your current state repository in browser...")
    driver = webdriver.Chrome()
    driver.get("https://github.com/" + un)
