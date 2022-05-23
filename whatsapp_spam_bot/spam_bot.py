from asyncio import write #what is asyncore
from turtle import pos
import pyautogui as pt
from time import sleep
import pyperclip 
import random

sleep(2)
#to locate the image

position1= pt.locateOnScreen(r'whatsapp_spam_bot/smiley.png',confidence=.6)#gets the position of the mentioned image and without confidence the program will select only those image of smiley which is 100% accurate

x=position1[0]
y=position1[1]
pt.FAILSAFE=False


#posts
def post_response(message):
    global x,y
    position= pt.locateOnScreen(r'whatsapp_spam_bot/smiley.png',confidence=.6)

    x=position[0] #to get the current position of cursor and the index is for x coordinate
    y=position[1] #to get the current position of cursor and the index is for x coordinate

    pt.moveTo(x+250,y+20 ,duration=.5)#to meve towards the chatbox
    pt.click()
    pt.typewrite(message, interval=0)

    pt.typewrite("\n", interval=1)#\n is enter
    
for i in range(50):
    post_response('Spam!')
    i+=1
    if i>50:
        break

    
