import time
import board
import pulseio#from adafruit_motor import servo
import servo

# create a PWMOut object on Pin A2 
right = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50) 
left = pulseio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)

rightleg = servo.Servo(right)
leftleg = servo.Servo(left)

print("Tora presents: Expressive Walk")

while 1:
    # step right
    for angle in range(0, 180, 3):
        rightleg.angle = angle
        leftleg.angle = angle
        time.sleep(0.05)
    # step left
    for angle in range(180, 0, -3):
        rightleg.angle = angle
        leftleg.angle = angle
        time.sleep(0.05)