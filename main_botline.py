import time as tm
from time import sleep
import pyautogui
import os

noOfMes = 1

while True:
    sleep(3)
    named_tuple = tm.localtime() # get struct_time
    time_string = tm.strftime("%H:%M:%S", named_tuple)
    timeS = time_string.split(":")
    print(time_string,"\n")
    if timeS[0] == "07" :
        pyautogui.typewrite("\n")
        noOfMes -= 1
    if noOfMes == 0:
        print("shutdown in 10 sec.")
        sleep(10)
        os.system("shutdown /s /t 1")
        break
