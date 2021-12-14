import threading
import Bot

PATH = ""
URL = "https://us.coca-cola.com/amoe?promotionId=8417_amc_iw_63987"

def run():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    BrowserChoice = int(input("1 for google chrome(can visually see), 2 for Phantomjs(faster but can't visually see)"))
    if BrowserChoice==1:
        PATH = "./googleChrome"
    else:
        PATH = "./pjs"
    print("!!!Cautious of DDOS and IP Blockage!!!")
    threadAmt = int(input("How Many Threads: "))
    for i in range(1, threadAmt+1):
        try:
            amcBot = Bot.AMCBot(URL, PATH, username, password)
            t = threading.Thread(target=amcBot.Execute())
            t.start()

        except Exception as e:
            print("Unable to start thread ", i)
            print(e)

if __name__ == '__main__':
    run()