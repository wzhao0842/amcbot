from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import datetime

class AMCBot:
    def __init__(self, url, PATH, username, password, choice):
        self.driver = webdriver.Chrome(PATH)
        if choice == 2:
            self.driver = webdriver.PhantomJS(PATH)
        self.driver.get(url)
        self.username = username
        self.password = password

    def Execute(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='mainContent']/main/div/div[1]/div/div/div[2]/div[3]/a")))
            element = self.driver.find_element_by_xpath("//*[@id='mainContent']/main/div/div[1]/div/div/div[2]/div[3]/a")
            ActionChains(self.driver).move_to_element(element).perform()
            element.click()
            self.SignIn()

        except Exception as e:
            print("mainExecution: ", e)

    def SignIn(self):
        try:
            userName = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='signInName']")))
            passWord = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='password']")))

            userName.send_keys(self.username)
            passWord.send_keys(self.password)
            self.driver.find_element(By.XPATH, "//*[@id='next']").click()
            self.UseEntry()

        except Exception as e:
            print("SignIn: ", e)

    def UseEntry(self):
        try:
            useEntry = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='mainContent']/main/div/div[1]/div/div/div[1]/div[4]/button")))

            useEntry.click()

            self.Redeem()

        except Exception as e:
            print("UseEntry: ", e)

    def Redeem(self):
        try:
            redeem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='mainContent']/main/div/div[1]/div/div/div[1]/div/div[2]/button")))

            time.sleep(56)
            redeem.click()

            print(self.Result())

        except Exception as e:
            print("Redeem: ", e)

        print(datetime.datetime.now())
        self.closeWeb()



    def Result(self):
        try:
            text = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='mainContent']/main/div/div[1]/div/div/div[1]/div/span/h2")))
            if text.getText() == "Thank you":
                return "Thank you"
            else:
                return "success"
        except:
            return "loading error"

    def closeWeb(self):
        self.driver.close()

    def getHtml(self, file, str):
        with open(file, "w") as f:
            f.write(str)