# import libraries
import board
import pulseio
import servo
import time
from adafruit_hcsr04 import HCSR04
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

# import music
def C4():
    return 262
def C_sharp():
    return 277
def D4():
    return 294
def E4():
    return 330
def F4():
    return 349
def F_sharp():
    return 370
def G4():
    return 392
def G_sharp():
    return 415
def A4():
    return 440
def B4():
    return 494
def OFF():
    return 1

def pause(buzzer, i):
    if (PAUSES[i % len(PAUSES)]) :
        buzzer.frequency = 1

def play_note(buzzer, i):
    buzzer.frequency = NOTES[i % len(NOTES)]

# list of notes, each an eighth note
NOTES = [
    # OFF(), OFF(), OFF(), OFF(), OFF(), OFF(), OFF(), OFF(),
    A4(),  A4(),  OFF(), OFF(), OFF(), A4(),  G4(),  F4(),
    F4(),  F4(),  OFF(), OFF(), OFF(), OFF(), F4(),  G4(),

    A4(),  A4(),  G4(),  F4(),  G4(),  G4(),  D4(),  D4(),
    OFF(), OFF(), OFF(), OFF(), OFF(), OFF(), OFF(), OFF(),
    A4(),  A4(),  OFF(), OFF(), OFF(), A4(),  G4(),  F4(),

    F4(),  F4(),  OFF(), OFF(), OFF(), D4(),  F4(),  G4(),
    A4(),  A4(),  G4(),  F4(),  G4(),  G4(),  D4(),  D4(),
    OFF(), OFF(), OFF(), OFF(), OFF(), OFF(), OFF(), OFF(),

    C4(),  G4(),  F4(),  F4(),  OFF(), A4(),  G4(),  F4(),
    F4(),  F4(),  OFF(), OFF(), OFF(), OFF(), F4(),  G4(),
    A4(),  A4(),  G4(),  F4(),  G4(),  G4(),  D4(),  D4(),

    OFF(), OFF(), E4(),  F4(),  F4(),  F4(),  OFF(), C4(),
    A4(),  A4(),  OFF(), OFF(), OFF(), A4(),  G4(),  F4(),
    F4(),  F4(),  OFF(), OFF(), OFF(), OFF(), F4(),  G4(),

    A4(),  A4(),  G4(),  F4(),  G4(),  G4(),  D4(),  D4(),
    OFF(), OFF(), E4(),  F4(),  F4(),  F4(),  OFF(), OFF(),
    OFF(), OFF(), C4(),  C4(),  C4(),  B4(),  A4(),  G4(),

    G4(),  A4(),  F4(),  F4(),  E4(),  F4(),  C4(),  F4(),
    D4(),  D4(),  C4(),  C4(),  A4(),  A4(),  F4(),  F4(),
    D4(),  D4(),  C4(),  C4(),  A4(),  A4(),  G4(),  G4(),

    OFF(), OFF(), C4(),  C4(),  C4(),  B4(),  A4(),  G4(),
    G4(),  A4(),  F4(),  F4(),  E4(),  F4(),  F4(),  F4(),
    D4(),  D4(),  C4(),  C4(),  A4(),  A4(),  OFF(), A4(),

    OFF(), C4(),  A4(),  C4(),  A4(),  C4(),  A4(),  A4(),
    F4(),  F4(),  F4(),  F4(),  F4(),  F4(),  F4(),  F4(),
    F4(),  D4(),  F4(),  G4(),  A4(),  A4(),  F4(),  F4(),

    F4(),  F4(),  F4(),  F4(),  F4(),  F4(),  F4(),  C4(),
    C4(),  C4(),  G4(),  G4(),  F4(),  F4(),  OFF(), OFF(),
    F4(),  F4(),  F4(),  F4(),  F4(),  F4(),  F4(),  F4(),

    F4(),  D4(),  F4(),  G4(),  A4(),  A4(),  F4(),  F4(),
    OFF(), C4(),  A4(),  C4(),  A4(),  C4(),  OFF(), A4(),
    OFF(), C4(),  A4(),  C4(),  A4(),  C4(),  A4(),  A4(),

    F4(),  F4(),  F4(),  F4(),  F4(),  F4(),  F4(),  F4(),
    F4(),  D4(),  F4(),  G4(),  A4(),  A4(),  F4(),  F4(),
    F4(),  F4(),  F4(),  F4(),  F4(),  F4(),  F4(),  C4(),

    C4(),  C4(),  G4(),  G4(),  F4(),  F4(),  OFF(), OFF(),
    F4(),  F4(),  F4(),  F4(),  F4(),  F4(),  F4(),  F4(),
    F4(),  D4(),  F4(),  G4(),  A4(),  A4(),  F4(),  F4(),

    OFF(), C4(),  A4(),  C4(),  A4(),  C4(),  OFF(), A4(),
    OFF(), C4(),  A4(),  C4(),  A4(),  C4(),  A4(),  A4(),
    OFF(), C4(),  A4(),  C4(),  A4(),  C4(),  A4(),  A4()
]

# a parallel list of whether or not to pause shortly before each note
PAUSES = [
    # 0, 0, 0, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 1, 1,

    1, 1, 1, 1, 1, 0, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 1, 1, 1,

    1, 0, 0, 0, 0, 1, 1, 1,
    1, 1, 1, 1, 1, 0, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0,

    1, 1, 1, 0, 0, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 1, 1,
    1, 1, 1, 1, 1, 0, 1, 0,

    0, 0, 1, 1, 1, 0, 0, 1,
    1, 1, 0, 0, 0, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 1, 1,

    1, 1, 1, 1, 1, 0, 1, 0,
    0, 0, 1, 1, 1, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 1, 1,

    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 0, 1, 0, 1, 1,
    1, 0, 1, 0, 1, 0, 1, 0,

    0, 0, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 0, 1, 0, 0, 1,

    0, 1, 1, 1, 1, 1, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 0,

    1, 0, 1, 0, 1, 0, 1, 1,
    1, 1, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 1,

    1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 0, 1,
    0, 1, 1, 1, 1, 1, 1, 0,

    1, 0, 1, 0, 1, 0, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 1,

    1, 1, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 1,
    1, 1, 1, 1, 1, 0, 1, 0,

    0, 1, 1, 1, 1, 1, 0, 1,
    0, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 0
]

# import dances

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
        display_text("Swivel dance", 0xd47313)
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
        display_text("Umm... hi?", 0x000000)
        shuffle_right_0(loR, loL, upR, upL)
    elif n % 4 == 1:
        shuffle_right_1(loR, loL, upR, upL)
    elif n % 4 == 2:
        shuffle_left_0(loR, loL, upR, upL)
    else:
        shuffle_left_1(loR, loL, upR, upL)

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

# JUMP DANCE -----------------------------------------------------------------------------------------

# Move both feet perpendicular to the floor
def jump1(loR, loL, upR, upL):
    for i in range(90, 180, 9):
        loL.angle = i
        loR.angle = 180 - i
        time.sleep(0.02)

# Move both feet back parallel to the floor
def jump2(loR, loL, upR, upL):
    for i in range(180, 90, -9):
        loL.angle = 180 - i
        loR.angle = i
        time.sleep(0.02)

# # Move both feet perpendicular to the floor in the other direction
def jump3(loR, loL, upR, upL):
    for i in range(90, 0, -9):
        loL.angle = 180 - i
        loR.angle = i
        time.sleep(0.02)

# Move both feet back parallel to the floor
def jump4(loR, loL, upR, upL):
    for i in range(0, 90, 9):
        loL.angle = i
        loR.angle = 180 - i
        time.sleep(0.02)

# Move legs to front
def jump5(loR, loL, upR, upL):
    for i in range(90, 130, 4):
        upL.angle = i
        upR.angle = 180 - i
        time.sleep(0.02)

# Move legs to back
def jump6(loR, loL, upR, upL):
    for i in range(130, 90, -4):
        upL.angle = i
        upR.angle = 180 - i
        time.sleep(0.02)

# Quickly tap left foot
def jump7(loR, loL, upR, upL):
    for i in range(1, 10, 1):
        loL.angle = 100
        time.sleep(0.01)
        loL.angle = 90
        time.sleep(0.01)

# Quickly tap right foot
def jump8(loR, loL, upR, upL):
    for i in range(1, 10, 1):
        loR.angle = 100
        time.sleep(0.01)
        loR.angle = 90
        time.sleep(0.01)

# Move feet perpendicular to floor
def jump9(loR, loL, upR, upL):
    for i in range(90, 0, -9):
        loL.angle = 180 - i
        loR.angle = i
        time.sleep(0.02)

# Move legs in
def jump10(loR, loL, upR, upL):
    for i in range(130, 90, -4):
        upL.angle = i
        upR.angle = 180 - i
        time.sleep(0.02)

# Move feet parallel to floor
def jump11(loR, loL, upR, upL):
    for i in range(1, 10, 1):
        loL.angle = 100
        time.sleep(0.01)
        loL.angle = 90
        time.sleep(0.01)

# Quickly tap right foot
def jump12(loR, loL, upR, upL):
    for i in range(1, 10, 1):
        loR.angle = 100
        time.sleep(0.01)
        loR.angle = 90
        time.sleep(0.01)

# Select one of 12 dance moves, based on a given index
def moon_walk(loR, loL, upR, upL, n):
    if n % 12 == 0:
        display_text("Jump dance", 0x1cadab)
        jump1(loR, loL, upR, upL)
    elif n % 12 == 1:
        jump2(loR, loL, upR, upL)
    elif n % 12 == 2:
        jump3(loR, loL, upR, upL)
    elif n % 12 == 3:
        jump4(loR, loL, upR, upL)
    elif n % 12 == 4:
        jump5(loR, loL, upR, upL)
    elif n % 12 == 5:
        jump6(loR, loL, upR, upL)
    elif n % 12 == 6:
        jump7(loR, loL, upR, upL)
    elif n % 12 == 7:
        jump8(loR, loL, upR, upL)
    elif n % 12 == 8:
        jump9(loR, loL, upR, upL)
    elif n % 12 == 9:
        jump10(loR, loL, upR, upL)
    elif n % 12 == 10:
        jump11(loR, loL, upR, upL)
    else:
        jump12(loR, loL, upR, upL)


def leg_move_1(right_foot, left_foot, right_leg, left_leg):
         for angle in range(90, 175, 10):  # right and left leg move
            right_leg.angle = angle
            left_leg.angle = angle
            time.sleep(0.02)
         for angle in range(175, 90, -10):  # right and left leg move
            right_leg.angle = angle
            left_leg.angle = angle
            time.sleep(0.02)
def move_foot_1(right_foot, left_foot, right_leg, left_leg):
         for angle in range(90, 170, 5):  # right foot up
            right_foot.angle = angle
            time.sleep(0.01)
         for angle in range(170, 90, -5):  # right foot down
            right_foot.angle = angle
            time.sleep(0.01)
         for angle in range(90, 140, 10):
            right_foot.angle = angle
            time.sleep(0.04)
         for angle in range(140, 90, -10):
            right_foot.angle = angle
            time.sleep(0.04)
def leg_move_2(right_foot, left_foot, right_leg, left_leg):
         for angle in range(90, 0, -10):  # right and left leg move backwards
            right_leg.angle = angle
            left_leg.angle = angle
            time.sleep(0.03)
         for angle in range(0, 90, 10):  # right and left leg return
            right_leg.angle = angle
            left_leg.angle = angle
            time.sleep(0.03)
def left_foot_move_1(right_foot, left_foot, right_leg, left_leg):
         for angle in range(90, 170, 5):  # left foot up
            left_foot.angle = angle
            time.sleep(0.01)
         for angle in range(170, 90, -5):  # left down down
            left_foot.angle = angle
            time.sleep(0.01)
         for angle in range(90, 130, 8):  # left foot up
            left_foot.angle = angle
            time.sleep(0.04)
         for angle in range(130, 90, -8):  # left down down
             left_foot.angle = angle
             time.sleep(0.04)
def right_foot_move_1(right_foot, left_foot, right_leg, left_leg):
         for angle in range(90, 170, 8):  # right foot up
            right_foot.angle = angle
            time.sleep(0.02)
         for angle in range(170, 90, -8):  # right foot down
            right_foot.angle = angle
            time.sleep(0.03)
         for angle in range(90, 130, 8):  # right foot up
            right_foot.angle = angle
            time.sleep(0.04)
         for angle in range(130, 90, -8):  # right foot down
            right_foot.angle = angle
            time.sleep(0.05)
def left_foot_move_2(right_foot, left_foot, right_leg, left_leg):
         for angle in range(90, 0, -5):  # left foot up
            left_foot.angle = angle
            time.sleep(0.03)
         for angle in range(0, 90, 5):  # left down down
            left_foot.angle = angle
            time.sleep(0.05)
def right_foot_move_2(right_foot, left_foot, right_leg, left_leg):
         for angle in range(90, 170, 5):  # right foot up
            right_foot.angle = angle
            time.sleep(0.03)
         for angle in range(170, 90, -5):  # right foot down
            right_foot.angle = angle
            time.sleep(0.01)
def left_foot_move_3(right_foot, left_foot, right_leg, left_leg):
         for angle in range(90, 0, -5):  # left foot up
            left_foot.angle = angle
            time.sleep(0.03)
         for angle in range(0, 90, 5):  # left down down
            left_foot.angle = angle
            time.sleep(0.01)
def leg_move_3(right_foot, left_foot, right_leg, left_leg):
         for angle in range(90, 120, 10):  # right and left leg move
            right_leg.angle = angle
            left_leg.angle = angle
            time.sleep(0.1)
         for angle in range(120, 0, -10):  # right and left leg move backwards
            right_leg.angle = angle
            left_leg.angle = angle
            time.sleep(0.1)
def leg_return(right_foot, left_foot, right_leg, left_leg):
         for angle in range(0, 90, 10):  # right and left leg back to normal
            right_leg.angle = angle
            left_leg.angle = angle
            time.sleep(0.05)
def left_foot_move_4(right_foot, left_foot, right_leg, left_leg):
         for angle in range(90, 170, 10):  # left foot up
            left_foot.angle = angle
            time.sleep(0.03)
         for angle in range(170, 90, -10):  # left down down
            left_foot.angle = angle
            time.sleep(0.03)
def right_foot_move_3(right_foot, left_foot, right_leg, left_leg):
         for angle in range(90, 170, 10):  # right foot up
            right_foot.angle = angle
            time.sleep(0.03)
         for angle in range(170, 90, -10):  # right foot down
            right_foot.angle = angle
            time.sleep(0.03)
# Decide which of the moes will be done , depending on a given index
def br_dancing(right_foot, left_foot, right_leg, left_leg, n):
        if n % 16 == 0:
             display_text("Br dance", 0x343bcf)
             leg_move_1(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 1:
             move_foot_1(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 2:
             leg_move_2(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 3:
             leg_move_2(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 4:
             left_foot_move_1(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 5:
             right_foot_move_1(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 6:
             left_foot_move_2(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 7:
             leg_move_2(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 8:
             right_foot_move_2(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 9:
             left_foot_move_3(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 10:
             leg_move_3(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 11:
             leg_return(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 12:
             left_foot_move_4(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 13:
             leg_move_2(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 14:
             right_foot_move_3(right_foot, left_foot, right_leg, left_leg)
        if n % 16 == 15:
             leg_move_1(right_foot, left_foot, right_leg, left_leg)
        else:
             leg_move_1(right_foot, left_foot, right_leg, left_leg)

# Both legs move to the right or left side in a 45 degree range during the zigzag stage
# The robot lifts the right foot when both legs go to the right and the same applies to the opposite direction
# It starts the wave on one foot, transition through ankles by controlling the lower servo motors,
# then ends the wave on the other foot
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

# configure servos
lower_right = pulseio.PWMOut(board.D10, duty_cycle=2**15, frequency=50)
lower_left = pulseio.PWMOut(board.D9, duty_cycle=2**15, frequency=50)
upper_right = pulseio.PWMOut(board.D12, duty_cycle=2**15, frequency=50)
upper_left = pulseio.PWMOut(board.D11, duty_cycle=2**15, frequency=50)

loR = servo.Servo(lower_right)
loL = servo.Servo(lower_left)
upR = servo.Servo(upper_right)
upL = servo.Servo(upper_left)


# configure buzzer
buzzer = pulseio.PWMOut(board.D5, variable_frequency=True)
buzzer.duty_cycle = 2**15  # 50% duty cycle, a square wave

# configure ultrasonic sensor
echo = board.A2
trig = board.A0

sonar = HCSR04(trig, echo)

i = 0

# set all servos to 90 degrees
reset(loR, loL, upR, upL)

# choose between tora's 6 "happy" dance moves
def happy_dance(loR, loL, upR, upL, i):
    if (i % 180 >= 150):
        swivel_dance(loR, loL, upR, upL, i)

    elif (i % 180 >= 120):
        slide_and_tap(loR, loL, upR, upL, i)

    elif (i % 180 >= 90):
        goDance(loR, loL, upR, upL, i)

    elif (i % 180 >= 60):
        moon_walk(loR, loL, upR, upL, i)

    elif (i % 180 >= 30):
        waveDance(loR, loL, upR, upL, i)

    elif (i % 180 >= 0):
        br_dancing(loR, loL, upR, upL, i)

# chose which dance moves to execute
def dance(dist, prev_dist, loR, loL, upR, upL, i) :
    if ((dist < 20 and prev_dist >= 20) or (dist >= 20 and prev_dist < 20)):
        if (dist >= 20 and prev_dist < 20):
            display_text("  Woohoo \nnobody's \nwatching!", 0xd9b102)
        reset(loR, loL, upR, upL)
    if (dist < 20):
        shuffle_dance(loR, loL, upR, upL, i)
    else:
        happy_dance(loR, loL, upR, upL, i)

# returns the distance reading of the ultrasonic sensor
# returns 50 if there's an error
def get_dist():
    try:
        return sonar.distance
    except (RuntimeError):
        return 50


def display_text(text, color):
    # Release any resources currently in use for the displays
    displayio.release_displays()

    spi = board.SPI()
    tft_cs = board.D3
    tft_dc = board.D4

    display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D7)

    display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1, rotation=270)

    # Make the display context
    splash = displayio.Group(max_size=10)
    display.show(splash)

    # Choose the color of the screen background
    color_bitmap = displayio.Bitmap(128, 128, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = color

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

    # Draw label
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=30, y=64)
    splash.append(text_area)

display_text("Umm... hi?", 0x000000)

dist = 0

while (True):
    pause(buzzer, i)
    prev_dist = dist
    dist = get_dist()
    print(dist)
    time.sleep(0.005)
    play_note(buzzer, i)
    dance(dist, prev_dist, loR, loL, upR, upL, i)

    if (i > 1000):
        i = 0
    else:
        i = i + 1
