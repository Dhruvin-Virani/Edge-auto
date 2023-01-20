#! /usr/bin/env python
import pyautogui as p
import time
import random
from hashlib import sha256

def search(query):
    p.hotkey("ctrl","e")
    time.sleep(.1)
    p.write(query)
    p.press("enter")
    time.sleep(.67)

def imageFind(image,g,double):
    a = 0
    b = 0
    while(a==0 and b==0):
        try:
            a,b = p.locateCenterOnScreen(image,confidence=0.65 ,grayscale=g)
        except TypeError:
            pass

    if double == True:
        p.doubleClick(a,b)
    else:
        p.click(a,b)

    return a,b

passw = p.password("Enter password: ")
while(sha256(passw.encode('utf-8')).hexdigest() != "d3de071faddd8e2e37ced5e90add67f2ed34b5489ad70381c9328ab00ad9fe34"):
    print("Wrong password")
    passw = p.password("Enter password: ")
    
p.hotkey("win","d")
imageFind("Edge.JPG",False,True)
time.sleep(3)
# p.hotkey("win","up")
search("bing ")
time.sleep(5)

c,d = imageFind("SignIn.png",True,True)
time.sleep(3)
# login = p.locateCenterOnScreen("LogIn.JPG",confidence=0.6, grayscale=True)

# while(login == None):
#       login = p.locateCenterOnScreen("LogIn.JPG",confidence=0.7, grayscale=True)            

p.write("for.browsing.on.edge2@gmail.com")
p.press("enter")

enterpassword = p.locateCenterOnScreen("EnterPassword.png",confidence=0.7, grayscale=True)
while(enterpassword == None):
      enterpassword = p.locateCenterOnScreen("EnterPassword.png",confidence=0.7, grayscale=True)
p.write(passw)
for q in range(3):
    time.sleep(5)
    p.press("enter")
    time.sleep(3)

searchOps = "qwertyuiopasdfghjklzxcvbnm1234567890!\"£$%^&*()/-+.|¬`[];'#,/{}:@~<>?"
searchQ = ""

for z in range(38):
    searchQ += searchOps[random.randint(0,len(searchOps)-1)]

for y in range(len(searchQ)):
    search(searchQ[:y])

time.sleep(2)
# imageFind("Rewards.JPG",True,False)

# p.click(c,d)
# imageFind("LogOut.JPG",True,False)
# time.sleep(.5)
# p.hotkey("ctrl","w")
