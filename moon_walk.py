# every single move takes the same amount of time (0.18s)
import board
import pulseio
import servo
import time

# configure servos
# lower_right = pulseio.PWMOut(board.D10, duty_cycle=2**15, frequency=50)
# lower_left = pulseio.PWMOut(board.D9, duty_cycle=2**15, frequency=50)
# upper_right = pulseio.PWMOut(board.D12, duty_cycle=2**15, frequency=50)
# upper_left = pulseio.PWMOut(board.D11, duty_cycle=2**15, frequency=50)

# loR = servo.Servo(lower_right)
# loL = servo.Servo(lower_left)
# upR = servo.Servo(upper_right)
# upL = servo.Servo(upper_left)

# Reset all servos to 90 degrees
def reset(loR, loL, upR, upL):
    loR.angle = 90
    loL.angle = 90
    upR.angle = 90
    upL.angle = 90

# Move the left foot from 90 degrees to 135 degrees
def left_foot_90_to_135(loR, loL, upR, upL):
    for i in range(90, 180, 9):
        loL.angle = i
        loR.angle = 180 - i
        time.sleep(0.02)

# Move the right foot from 45 degrees to 90 degrees
def right_foot_45_to_90(loR, loL, upR, upL):
    for i in range(180, 90, -9):
        loL.angle = 180 - i
        loR.angle = i
        time.sleep(0.02)

# Move the left foot from 135 degrees to 90 degrees
def left_foot_135_to_90(loR, loL, upR, upL):
    for i in range(90, 0, -9):
        loL.angle = 180 - i
        loR.angle = i
        time.sleep(0.02)

# Move the right foot from 90 degrees to 45 degrees
def right_foot_90_to_45(loR, loL, upR, upL):
    for i in range(0, 90, 9):
        loL.angle = i
        loR.angle = 180 - i
        time.sleep(0.02)

# Move left leg from 90 degrees to 0 degrees, and left foot from 135 degrees to 90 degrees
def swivel_left0(loR, loL, upR, upL):
    for i in range(90, 130, 4):
        upL.angle = i
        upR.angle = 180 - i
        time.sleep(0.02)

# Move left leg from 0 degrees to 90 degrees, and left foot from 90 degrees to 135 degrees
def swivel_left1(loR, loL, upR, upL):
    for i in range(130, 90, -4):
        upL.angle = i
        upR.angle = 180 - i
        time.sleep(0.02)

# Move left leg from 90 degrees to 180 degrees, and left foot from 135 degrees to 90 degrees
def swivel_left2(loR, loL, upR, upL):
    for i in range(1, 10, 1):
        loL.angle = 100
        time.sleep(0.01)
        loL.angle = 90
        time.sleep(0.01)

# Move left leg from 180 degrees to 90 degrees, and left foot from 90 degrees to 135 degrees
def swivel_left3(loR, loL, upR, upL):
    for i in range(1, 10, 1):
        loR.angle = 100
        time.sleep(0.01)
        loR.angle = 90
        time.sleep(0.01)

# Move right leg from 90 degrees to 180 degrees, and right foot from 45 degrees to 90 degrees
def swivel_right0(loR, loL, upR, upL):
    for i in range(90, 0, -9):
        loL.angle = 180 - i
        loR.angle = i
        time.sleep(0.02)

# Move right leg from 180 degrees to 90 degrees, and right foot from 90 degrees to 45 degrees
def swivel_right1(loR, loL, upR, upL):
    for i in range(130, 90, -4):
        upL.angle = i
        upR.angle = 180 - i
        time.sleep(0.02)

# Move right leg from 90 degrees to 0 degrees, and right foot from 45 degrees to 90 degrees
def swivel_right2(loR, loL, upR, upL):
    for i in range(1, 10, 1):
        loL.angle = 100
        time.sleep(0.01)
        loL.angle = 90
        time.sleep(0.01)

# Move right leg from 0 degrees to 90 degrees, and right foot from 90 degrees to 45 degrees
def swivel_right3(loR, loL, upR, upL):
    for i in range(1, 10, 1):
        loR.angle = 100
        time.sleep(0.01)
        loR.angle = 90
        time.sleep(0.01)

# Select one of 12 dance moves, based on a given index
def moon_walk(loR, loL, upR, upL, n):
    if n % 12 == 0:
        left_foot_90_to_135(loR, loL, upR, upL)
    elif n % 12 == 1:
        swivel_left0(loR, loL, upR, upL)
    elif n % 12 == 2:
        swivel_left1(loR, loL, upR, upL)
    elif n % 12 == 3:
        swivel_left2(loR, loL, upR, upL)
    elif n % 12 == 4:
        swivel_left3(loR, loL, upR, upL)
    elif n % 12 == 5:
        left_foot_135_to_90(loR, loL, upR, upL)
    elif n % 12 == 6:
        right_foot_90_to_45(loR, loL, upR, upL)
    elif n % 12 == 7:
        swivel_right0(loR, loL, upR, upL)
    elif n % 12 == 8:
        swivel_right1(loR, loL, upR, upL)
    elif n % 12 == 9:
        swivel_right2(loR, loL, upR, upL)
    elif n % 12 == 10:
        swivel_right3(loR, loL, upR, upL)
    else:
        right_foot_45_to_90(loR, loL, upR, upL)

# Testing loop, remove when integrating
# while 1:
#     for i in range(0, 12, 1):
#         moon_walk(loR, loL, upR, upL, i)
