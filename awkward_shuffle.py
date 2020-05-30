# Awkward shuffle to be run when someone is in range of the ultrasonic sensor
# each move takes the same amount of time (0.18s)
import time
import board
import pulseio
import servo

# # Configure servos
# lower_right = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
# lower_left = pulseio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)

# loR = servo.Servo(lower_right)
# loL = servo.Servo(lower_left)

# Rotate right foot from 90 degrees to 45 degrees
def shuffle_right_0(loR, loL, upR, upL):
    for angle in range(90, 40, -5):
        loR.angle = angle
        time.sleep(0.02)

# Rotate right foot from 45 degrees to 90 degrees
def shuffle_right_1(loR, loL, upR, upL):
    for angle in range(45, 85, 5):
        loR.angle = angle
        time.sleep(0.02)

# Rotate left foot from 90 degrees to 135 degrees
def shuffle_left_0(loR, loL, upR, upL):
    for angle in range(90, 140, 5):
        loL.angle = angle
        time.sleep(0.02)

# Rotate left foot from 135 degrees to 90 degrees
def shuffle_left_1(loR, loL, upR, upL):
    for angle in range(135, 85, -5):
        loL.angle = angle
        time.sleep(0.02)

# Select a dance move based on the given index
def shuffle_dance(loR, loL, upR, upL, n):
    if n % 4 == 0:
        shuffle_right_0(loR, loL, upR, upL)
    elif n % 4 == 1:
        shuffle_right_1(loR, loL, upR, upL)
    elif n % 4 == 2:
        shuffle_left_0(loR, loL, upR, upL)
    else:
        shuffle_left_1(loR, loL, upR, upL)

# # Testing loop, remove when integrating
# while 1:
#     for i in range(0, 4, 1):
#         shuffle_dance(i)
