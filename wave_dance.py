import time
import board
import pulseio
import servo

def waveDance(loR, loL, upR, upL, n):
    if (n % 24 == 1):   
        for angle in range(90, 135, 5):      # zigzag twist 1
            upR.angle = angle
            upL.angle = angle
        for angle in range(90, 30, -10):     # move right foot
            loL.angle = angle
            time.sleep(0.03)            
    if (n % 24 == 2): 
        for angle in range(30, 90, 10):      # move back right foot
            loL.angle = angle
            time.sleep(0.01)    
    if (n % 24 == 3):
        for angle in range(135, 90, -5):     # back to origin
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.03)           
    if (n % 24 == 4):      # zigzag to left
        for angle in range(90, 45, -5):
            upR.angle = angle
            upL.angle = angle
        for angle in range(90, 150, 10):      # move left foot
            loR.angle = angle
            time.sleep(0.03)      
    if (n % 24 == 5):
        for angle in range(150, 90, -10):     # move back left foot
            loR.angle = angle
            time.sleep(0.01)         
    if (n % 24 == 6):       # back to origin
        for angle in range(45, 90, 5):
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.03)
          
    if (n % 24 == 7 or n % 24 == 9):      # wave 1
        for angle in range(90, 150, 5):
            loL.angle = angle
        for angle in range(90, 40, -5):
            loR.angle = angle
            time.sleep(0.03)            
    if (n % 24 == 8 or n % 24 == 10):     
        for angle in range(150, 90, -5):
            loL.angle = angle
        for angle in range(40, 90, 5):
            loR.angle = angle
            time.sleep(0.03)   
            
    if (n % 24 == 11):        # zigzag twist 2
        for angle in range(90, 135, 5):      # zigzag to right
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.03)            
    if (n % 24 == 12):        
        for angle in range(90, 150, 10):     # move left foot
            loL.angle = angle
            time.sleep(0.01)           
    if (n % 24 == 13):
        for angle in range(150, 90, -10):    # move back right foot
            loL.angle = angle
            time.sleep(0.01)      
    if (n % 24 == 14):  
        for angle in range(135, 90, -5):     # back to origin
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.03)    
    if (n % 24 == 15):  
        for angle in range(90, 45, -5):      # zigzag to left
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.03)            
    if (n % 24 == 16):   
        for angle in range(90, 30, -10):     # move right foot
            loR.angle = angle
            time.sleep(0.03)           
    if (n % 24 == 17):       
        for angle in range(30, 90, 10):      # move back left foot
            loR.angle = angle
            time.sleep(0.03)  
    if (n % 24 == 18):
        for angle in range(45, 90, 5):       # back to origin
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.03)
               
    if (n % 24 == 19 or n % 24 == 21):       # wave 2 
        for angle in range(90, 40, -5):
            loR.angle = angle
        for angle in range(90, 150, 5):
            loL.angle = angle
            time.sleep(0.03)         
    if (n % 24 == 20 or n % 24 == 22):       
        for angle in range(40, 90, 5):
            loR.angle = angle
        for angle in range(150, 90, -5):
            loL.angle = angle
            time.sleep(0.03)
                 
    if (n % 24 == 23 or n % 24 == 0):     # default   
        loR.angle = 90
        loL.angle = 90
        upR.angle = 90
        upL.angle = 90
