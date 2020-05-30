# every single move takes the same amount of time (0.18s)
import board
import pulseio
import servo
import time

# # Configure servos
# lower_right = pulseio.PWMOut(board.D10, duty_cycle=2**15, frequency=50)
# lower_left = pulseio.PWMOut(board.D9, duty_cycle=2**15, frequency=50)
# upper_right = pulseio.PWMOut(board.D12, duty_cycle=2**15, frequency=50)
# upper_left = pulseio.PWMOut(board.D11, duty_cycle=2**15, frequency=50)
#
# loR = servo.Servo(lower_right)
# loL = servo.Servo(lower_left)
# upR = servo.Servo(upper_right)
# upL = servo.Servo(upper_left)

# Slide the feet from 0 degrees to 180 degrees
def slide_0(loR, loL, upR, upL):
    for angle in range(0, 190, 10):
        upR.angle = angle
        upL.angle = angle
        time.sleep(0.01)

# Slide the feet from 180 degrees to 0 degrees
def slide_1(loR, loL, upR, upL):
    for angle in range(180, -10 , -10):
        upR.angle = angle
        upL.angle = angle
        time.sleep(0.01)

# Set all servo angles to 90 degrees
# def reset(loR, loL, upR, upL):
#     loR.angle = 90
#     loL.angle = 90
#     upR.angle = 90
#     upL.angle = 90

# Tap the right foot of the robot
def tap_right(loR, loL, upR, upL):
    for angle in range(90, 45, -5):
        loR.angle = angle
        time.sleep(0.01)
    for angle in range(45, 90, 5):
        loR.angle = angle
        time.sleep(0.01)

# Based on a given index, execute one of the dance moves in the sequence
def slide_and_tap(loR, loL, upR, upL, n):
    if (n % 6 == 0) or (n % 6 == 2):
        slide_0(loR, loL, upR, upL)
    elif (n % 6 == 1) or (n % 6 == 3):
        slide_1(loR, loL, upR, upL)
    else:
        tap_right(loR, loL, upR, upL)

# # Testing loop, remove when integrating
# while 1:
#     for i in range(0, 40, 1):
#         slide_and_tap(i)
