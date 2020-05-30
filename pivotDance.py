import time
import board
import pulseio
import servo


# repeat tilt 1-4 twice 
def tilt1(loR, loL, upR, upL):
    for angle in range(90, 150, 5):  # right foot up, tilt inwards and slide left leg
        loR.angle = angle
        upL.angle = angle
        time.sleep(0.01)

def tilt2(loR, loL, upR, upL):
    for angle in range(150, 90, -3): # right foot down, slide left leg back
        loR.angle = angle
        upL.angle = angle
        time.sleep(0.01)
     
def tilt3(loR, loL, upR, upL):
    for angle in range(90, 30, -5):  # left foot up, slide right leg
        loL.angle = angle
        upR.angle = angle
        time.sleep(0.01)
        
def tilt4(loR, loL, upR, upL):
    for angle in range(30, 90, 3): # left foot down, slide right leg back
         loL.angle = angle
         upR.angle = angle
         time.sleep(0.01)

# repeat slide cycle twice
def slide1(loR, loL, upR, upL):         # slide both feet side to side
    for angle in range(90, 135, 5): 
        upL.angle = angle
        upR.angle = angle
        time.sleep(0.01)
    for angle in range(135, 45, -5):
        upL.angle = angle
        upR.angle = angle
        time.sleep(0.01)
   
def slide2(loR, loL, upR, upL):         # slide both feet side to side
    for angle in range(45, 135, 5):
        upL.angle = angle
        upR.angle = angle
        time.sleep(0.01)
    for angle in range(135, 90, -5):
        upL.angle = angle
        upR.angle = angle
        time.sleep(0.01)

# whole cycle gets repeated twice
# inner pivot loop repeat twice
def pivotLUp(loR, loL, upR, upL):
    for angle in range(90, 45, -3):  # left foot up
        loL.angle = angle
        time.sleep(0.01)
     
# do this twice
def pivotUR(loR, loL, upR, upL):
    for angle in range(90, 45, -5):     # pivot right leg side to side   
        upR.angle = angle       
        time.sleep(0.01)
    for angle in range(45, 90, 5):
        upR.angle = angle
        time.sleep(0.01)
        
def pivotLDown(loR, loL, upR, upL):        
    for angle in range(45, 90, 3): # left foot down
        loL.angle = angle
        time.sleep(0.01)
            
def pivotRUp(loR, loL, upR, upL):
    for angle in range(90, 150, 3):  # right foot up, tilt inwards
        loR.angle = angle
        time.sleep(0.01)

 # repeat twice
def pivotUL(loR, loL, upR, upL):
        for angle in range(90, 135, 5):     # pivot left leg side to side
            upL.angle = angle
        for angle in range(135, 90, -5):
            upL.angle = angle
        
def pivotRDown(loR, loL, upR, upL):
    for angle in range(150, 90, -3): # right foot down
        loR.angle = angle
        time.sleep(0.01)

def goDance(loR, loL, upR, upL, n):  # depending on the value of n (iteration var), execute a specific submove of the dance
    if n % 16 == 0:  # tilt right side up and slide left leg
        tilt1(loR, loL, upR, upL)
    elif n % 16 == 1: # reset to normal and slide back
        tilt2(loR, loL, upR, upL)
    elif n % 16 == 2: # tilt left side up and slide right leg
        tilt3(loR, loL, upR, upL)
    elif n % 16 == 3: # reset to normal and slide back
        tilt4(loR, loL, upR, upL)
    elif ((n % 16 == 4) or (n % 16 == 6)):  # slide both feet together
        slide1(loR, loL, upR, upL)
    elif ((n % 16 == 5) or (n % 16 == 7)):  # slide both feet together
        slide2(loR, loL, upR, upL)
    elif n % 16 == 8:  # tilt left side up
        pivotLUp(loR, loL, upR, upL)
    elif ((n % 16 == 9) or (n % 16 == 10)):  # pivot right foot side to side
        pivotUR(loR, loL, upR, upL) 
    elif n % 16 == 11: # reset back to normal
        pivotLDown(loR, loL, upR, upL)
    elif n % 16 == 12:  # tilt right side up
        pivotRUp(loR, loL, upR, upL)
    elif ((n % 16 == 13) or (n % 16 == 14)):   # pivot left foot side to side
        pivotUL(loR, loL, upR, upL)
    else:  # reset back to normal
        pivotRDown(loR, loL, upR, upL)
        
