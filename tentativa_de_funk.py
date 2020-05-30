import time
import board
import pulseio
import servo




#Resets all servos to 90 degrees
def reset(right_foot, left_foot, right_leg, left_leg):
         right_leg.angle = 90
         right_foot.angle = 90
         left_leg.angle = 90
         left_foot.angle = 90

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

def br_dancing(right_foot, left_foot, right_leg, left_leg, n):
        if n % 16 == 0:
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


