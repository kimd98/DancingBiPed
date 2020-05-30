import time
import board
from adafruit_hcsr04 import HCSR04
import pulseio
import servo

echo = board.A2
trig = board.A0

# create a PWMOut object on Pin A2 
right = pulseio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50) 
left = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)

LR = servo.Servo(right)
LL = servo.Servo(left)

#sonar = HCSR04(trig, echo)

with HCSR04(trig, echo) as sonar:
    while True:
        dist = sonar.distance
        if (dist > 10):
        # Shuffle right foot
            for angle in range(90, 45, -3):  
                LR.angle = angle
                time.sleep(0.05)
            for angle in range(45, 90, 3):
                LR.angle = angle
                time.sleep(0.05)
        else:
            # Shuffle right foot
            for angle in range(90, 45, -3):  
                LR.angle = angle
                time.sleep(0.05)
            for angle in range(45, 90, 3):
                LR.angle = angle
                time.sleep(0.05)

                # Shuffle left foot
            for angle in range(90, 135, 3):  
                LL.angle = angle
                time.sleep(0.05)
            for angle in range(135, 90, -3): 
                LL.angle = angle
                time.sleep(0.05)

        
#sonar.deinit()
