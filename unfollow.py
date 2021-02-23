from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import login

driver = webdriver.Firefox(executable_path="C:\\Executable Programs\\geckodriver.exe")

username = login.username
password = login.password
uprofile = login.profile

igurl = "https://www.instagram.com/"

driver.get(igurl+"accounts/login/")
sleep(3)

def login_ig():
    while True:
        try:
            print("Logging in...")
            driver.find_element_by_name("username").send_keys(username)
            sleep(1)
            driver.find_element_by_name("password").send_keys(password)
            sleep(1)
            driver.find_element_by_xpath("//div[3]/button").click()
            sleep(3)
            print("Successfully logged in!")
            driver.get(igurl)
            print("Accessing home page...")
            sleep(3)
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
            print("All set!")
            sleep(1)
        except:
            print("Login Error, Trying again... if this message presists, please close and launch the script again.")
            sleep(1)
            continue
        break

def unfollow_users(profile):
    nlc = 0
    driver.get(igurl+profile)
    sleep(3)
    driver.find_element_by_xpath("//ul/li[3]/a").click()
    sleep(3)
    print("Getting unfollowers list... ")
    sleep(1)

    for x in range(7):
        try:
            nlc = x + 1
            stnlc = str(nlc)
            unfo_name = driver.find_element_by_xpath("//li["+stnlc+"]/div/div[2]/div[1]/div/div/span/a").text
            print("Selecting user " + unfo_name)
            sleep(5)
            driver.find_element_by_xpath("//li["+stnlc+"]/div/div[3]/button[contains(text(),'Following')]").click()
            print("Unfollowing... ")
            sleep(1)
            driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]").click()
            print("Successfully Unfollowed "+ unfo_name)
            sleep(1)
        except:
            break

    driver.get(igurl)
    sleep(1)
    driver.execute_script("window.scrollTo(0, 720)")
    sleep(2)
    driver.execute_script("window.scrollTo(0, 1080)")
    sleep(2)

if __name__ == "__main__":
    login_ig()
    while True:
        unfollow_users(uprofile)
        print("Waiting 180 seconds...")
        sleep(180)