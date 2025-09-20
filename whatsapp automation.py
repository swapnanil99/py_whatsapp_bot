import pywhatkit as pw
import pyautogui as pg
import time
number = input("Enter number with country code :") # Taking input from the user for the phone number with country code
message = input("Enter the message to send: ")
repeat = int(input("How many times do you want to send the message? ")) # Taking input from the user for the number of times to send the message

pw.sendwhatmsg_instantly(number, message, wait_time=15, tab_close=False)
time.sleep(5) # Waiting for 5 seconds to allow the WhatsApp web to load
for i in range(repeat - 1): # Looping through the range of count - 1
    pg.typewrite(message) # Typing the message using pyautogui
    pg.press("enter") # Pressing enter to send the message
    time.sleep(1) 

