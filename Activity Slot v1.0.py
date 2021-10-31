from datetime import datetime,date
import pyttsx3
while True:
    opt = input("Enter A to write your acitivity \nEnter B to read your Activity")

    def writeActivity():
        Act = input("Kindly Enter Your Acitivity Here\t")
        now=datetime.now()
        t = now.strftime("%H:%M:%S")
        today=date.today()
        todaydate = today.strftime("%B %d, %Y")
        d = todaydate
        file = open("C:/Users/Public/myactivityslot.txt" ,"a+")
        file.write("Acitivity\t" + Act + "\tTime\t" + t + "\tDate\t" + d +"\n")
        file.close()

    def readActivity():
        file = open("C:/Users/Public/myactivityslot.txt", "r")
        c = input("Enter The Keyword That You Want to See")
        Detective = 0
        for mydat in file:
            if c in mydat:
                print(mydat)
                engine = pyttsx3.init()
                engine.say(mydat)
                engine.runAndWait()
                Detective = 1
        if Detective == 0:
            print("Data Not Found")
        file.close()

    if opt == "A" or opt=="a":
        writeActivity()
    elif opt == "B" or opt=="b":
        readActivity()
    else:
        print("invlaid input! try agian with[A/B]\n\n")