import pyautogui as gui
import webbrowser
import time
import numpy as np
def Game_Start():
    webbrowser.open("http://games.twtop.net/fgameplay.php?id=2424", new=1, autoraise=True)
    time.sleep(3)
    for i in range(0,7):
        gui.press('down')
    gui.click(859,567)
    time.sleep(3)
def Order(client):
    gui.FAILSAFE = True
    order = np.array([0,0,0,0,0,0,0])
    for i in range(4):
        a = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        try:
            a[0] = gui.locateOnScreen('1.png', grayscale=True, confidence=.7, region=(700+200*(client-1),224+20*i,120,35))
        except:
            pass
        try:
            a[1] = gui.locateOnScreen('2.png', grayscale=True, confidence=.7, region=(700+200*(client-1),224+20*i,120,35))
        except:
            pass
        try:
            a[2] = gui.locateOnScreen('3.png', grayscale=True, confidence=.7, region=(700+200*(client-1),224+20*i,120,35))
        except:
            pass
        try:
            a[3] = gui.locateOnScreen('4.png', grayscale=True, confidence=.7, region=(700+200*(client-1),224+20*i,120,35))
        except:
            pass
        try:
            a[4] = gui.locateOnScreen('5.png', grayscale=True, confidence=.7, region=(700+200*(client-1),224+20*i,120,35))
        except:
            pass
        try:
            a[5] = gui.locateOnScreen('6.png', grayscale=True, confidence=.7, region=(700+200*(client-1),224+20*i,120,35))
        except:
            pass
        try:
            a[6] = gui.locateOnScreen('7.png', grayscale=True, confidence=.7, region=(700+200*(client-1),224+20*i,120,35))
        except:
            pass
        for k in range(7):
            if a[k,0] != 0:
                order[k] += 1
    return order
def Prepare_Dish(dish,pos):
    for i in range (4):
        for j in range(dish[i]):
            gui.moveTo(705,481+45*i)
            for k in range(5):
                if pos[k]==0:
                    gui.dragTo(787+k*84, 636)
                    gui.click(787+k*84, 636)
                    pos[k]+=1
                    break
    for i in range (4,7):
        for j in range(dish[i]):
            gui.moveTo(1210, 505+45*(i-4))
            for k in range(5):
                if pos[k]==0:
                    gui.dragTo(787+k*84, 636)
                    gui.click(787+k*84, 636)
                    pos[k]+=1
                    break
    return pos
def Give_to_Client(client,pos):
    for i in range(5):
        if pos[i] != 0:
            gui.moveTo(787+i*84, 636)
            gui.dragTo(820+(client-1)*200, 420)
            gui.click(820+(client-1)*200, 420)
            pos[i] = 0
def Game_Over():
    over = np.array([0,0])
    try:
        over = gui.locateCenterOnScreen('Game_Over.png', region=(700,240,250,60))
    except:
        pass
    return over
     
Game_Start()
gameover = Game_Over()
while gameover[0] == 0:
    for client in range (1,4):
        position = np.array([0,0,0,0,0])
        orders = Order(client)
        if sum(orders) != 0:
            print(orders)
            position = Prepare_Dish(orders,position)
            time.sleep(5.5)
            Give_to_Client(client,position)
    gameover = Game_Over()
