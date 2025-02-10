from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest:
                error += 1
        except:
            error += 1
    return error


def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)
while True:
        check = input("Ready to test : yes / no : ")
        if check == "yes" or check == "Yes" or check == "y":
                test = ["A paragraph is a self contained unit of discourse in writing dealing with a particular point or idea.","I am Michael Stern", "This is a Typing speed calculator python code."]
                test1 = r.choice(test)
                print("\n***** Typing Speed *****\n")
                print(test1)
                print()
                print()
                time_1 = time()
                testinput = input("Enter : ")
                time_2 = time()
                print('Speed : ',speed_time(time_1,time_2,testinput), "word/sec")
                print("Error : ",mistake(test1, testinput))
        elif check == "no" or check == "No" or check == "n":
                print("\n ***** Thank You *****")
                break
        else:
                print("Wrong input...")