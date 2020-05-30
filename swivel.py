# every single move takes the same amount of time (0.18s)
import board
import pulseio
import servo
import time

# # configure servos
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
    for i in range(90, 140, 5):
        loL.angle = i
        time.sleep(0.02)

# Move the right foot from 45 degrees to 90 degrees
def right_foot_45_to_90(loR, loL, upR, upL):
    for i in range(45, 95, 5):
        loR.angle = i
        time.sleep(0.02)

# Move the left foot from 135 degrees to 90 degrees
def left_foot_135_to_90(loR, loL, upR, upL):
    for i in range(135, 85, -5):
        loL.angle = i
        time.sleep(0.02)

# Move the right foot from 90 degrees to 45 degrees
def right_foot_90_to_45(loR, loL, upR, upL):
    for i in range(90, 40, -5):
        loR.angle = i
        time.sleep(0.02)

# Move left leg from 90 degrees to 0 degrees, and left foot from 135 degrees to 90 degrees.
# Then, move left leg from 0 degrees to 90 degrees, and left foot from 90 degrees to 135 degrees.
def swivel_left0(loR, loL, upR, upL):
    for i in range(90, -10, -10):
        loL.angle = 135 - 2.5 * (90 - i) / 5
        upL.angle = i
        time.sleep(0.01)
    for i in range(0, 100, 10):
        loL.angle = 90 + 2.5 * i / 5
        upL.angle = i
        time.sleep(0.01)

# Move left leg from 90 degrees to 180 degrees, and left foot from 135 degrees to 90 degrees.
# Then, move left leg from 180 degrees to 90 degrees, and left foot from 90 degrees to 135 degrees.
def swivel_left1(loR, loL, upR, upL):
    for i in range(90, 190, 10):
        loL.angle = 135 - 2.5 * (i - 90) / 5
        upL.angle = i
        time.sleep(0.01)
    for i in range(180, 80, -10):
        loL.angle = 90 + 2.5 * (180 - i) / 5
        upL.angle = i
        time.sleep(0.01)
    
# Move right leg from 90 degrees to 180 degrees, and right foot from 45 degrees to 90 degrees.
# Then, move right leg from 180 degrees to 90 degrees, and right foot from 90 degrees to 45 degrees.
def swivel_right0(loR, loL, upR, upL):
    for i in range(90, 190, 10):
        loR.angle = 45 + 2.5 * (i - 90) / 5
        upR.angle = i
        time.sleep(0.01)
    for i in range(180, 80, -10):
        loR.angle = 90 - 2.5 * (180 - i) / 5
        upR.angle = i
        time.sleep(0.01)

# Move right leg from 90 degrees to 0 degrees, and right foot from 45 degrees to 90 degrees.
# Then, move right leg from 0 degrees to 90 degrees, and right foot from 90 degrees to 45 degrees.
def swivel_right1(loR, loL, upR, upL):
    for i in range(90, -10, -10):
        loR.angle = 45 + 2.5 * (90 - i) / 5
        upR.angle = i
        time.sleep(0.01)
    for i in range(0, 100, 10):
        loR.angle = 90 - 2.5 * i / 5
        upR.angle = i
        time.sleep(0.01)

# Select one of 12 dance moves, based on a given index
def swivel_dance(loR, loL, upR, upL, n):
    if n % 8 == 0:
        left_foot_90_to_135(loR, loL, upR, upL)
    elif n % 8 == 1:
        swivel_left0(loR, loL, upR, upL)
    elif n % 8 == 2:
        swivel_left1(loR, loL, upR, upL)
    elif n % 8 == 3:
        left_foot_135_to_90(loR, loL, upR, upL)
    elif n % 8 == 4:
        right_foot_90_to_45(loR, loL, upR, upL)
    elif n % 8 == 5:
        swivel_right0(loR, loL, upR, upL)
    elif n % 8 == 6:
        swivel_right1(loR, loL, upR, upL)
    else:
        right_foot_45_to_90(loR, loL, upR, upL)

# # Testing loop, remove when integrating
# while 1:
#     for i in range(0, 12, 1):
#         swivel_dance(i)
