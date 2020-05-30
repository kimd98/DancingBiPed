import time
import board
import pulseio
import servo

# create a PWMOut objects, use the LOWER servos
pwm1 = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
pwm2 = pulseio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
pwm3 = pulseio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)
pwm4 = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
#buzzer = pulseio.PWMOut(board.D7, varaible_frequency = True)

# Create a servo object, my_servo.
right_leg = servo.Servo(pwm1)
right_foot = servo.Servo(pwm2)
left_leg = servo.Servo(pwm3)
left_foot = servo.Servo(pwm4)


def reset():
    right_leg.angle = 90
    right_foot.angle = 90
    left_leg.angle = 90
    left_foot.angle = 90
def leg_move(first, last, incr, time):
    for angle in range(first, last, incr):  # right and left leg move
        right_leg.angle = angle
        left_leg.angle = angle
        time.sleep(time)

def right_foot_move(first, last, incr, time):
    for angle in range(first, last, incr):  # right foot up
        right_foot.angle = angle
        time.sleep(time)

def left_foot_move(first, last, incr, time):
    for angle in range(first, last, time):  # left foot up
        left_foot.angle = angle
        time.sleep(time)

def leg_return():
    for angle in range(0, 90, 10):  # right and left leg back to normal
        right_leg.angle = angle
        left_leg.angle = angle
        time.sleep(0.05)

def br_dancing(n):

    // leg move 1
    leg_move(90, 110, 10, 0.01)
    leg_move(110, 124, 10, 0.01)
    leg_move(124, 141, 10, 0.01)
    leg_move(141, 158, 10, 0.01)
    leg_move(158, 175, 10, 0.01)

    leg_move(175, 158, -10, 0.01)
    leg_move(158, 141, -10, 0.01)
    leg_move(141, 124, -10, 0.01)
    leg_move(124, 110, -10, 0.01)
    leg_move(110, 90, -10, 0.01)

    // move foot 1
    right_foot_move(90, 100, 5, 0.01)
    right_foot_move(100, 110, 5, 0.01)
    right_foot_move(110, 120, 5, 0.01)
    right_foot_move(120, 130, 5, 0.01)
    right_foot_move(130, 140, 5, 0.01)
    right_foot_move(140, 150, 5, 0.01)
    right_foot_move(150, 170, 10, 0.01)


    right_foot_move(170, 160, -10, 0.01)
    right_foot_move(160, 150, -10, 0.01)
    right_foot_move(150, 140, -10, 0.01)
    right_foot_move(140, 135, -5, 0.01)
    right_foot_move(135, 130, -5, 0.01)
    right_foot_move(130, 120, -10, 0.01)
    right_foot_move(120, 110, -10, 0.01)
    right_foot_move(110, 100, -10, 0.01)
    right_foot_move(100, 95, -5, 0.01)
    right_foot_move(95, 90, -5, 0.01)

    //leg move 2

    leg_move(90, 72, -18, 0.01)
    leg_move(72, 54, -18, 0.01)
    leg_move(54, 36, -18, 0.01)
    leg_move(36, 18, -18, 0.01)
    leg_move(18, 0, -18, 0.01)

    leg_move(0, 18, 18, 0.01)
    leg_move(18, 36, 18, 0.01)
    leg_move(36, 54, 18, 0.01)
    leg_move(54, 72, 18, 0.01)
    leg_move(72, 90, 18, 0.01)

    //left foot move 1

    left_foot_move(90, 170, 5, 0.03)
    left_foot_move(170, 90, -5, 0.03)

    //right foot move 1

    right_foot_move(90, 170, 5, 0.03)

    right_foot_move(170, 140, -5, 0.01)
    right_foot_move(140, 110, -5, 0.01)
    right_foot_move(110, 90, -5, 0.01)

    //left foot move 2

    left_foot_move(90, 0, -5, 0.03)
    left_foot_move(0, 45,5, 0.05)
    left_foot_move(45, 90, 5, 0.05)

    // right foot move 2

    right_foot_move(90, 170, 5, 0.03)
    right_foot_move(170, 90, -5, 0.01)

    // Left foot move 3

    left_foot_move(90, 0, -5, 0.03)
    left_foot_move(0, 90, 5, 0.01)

    //leg_move_3

    leg_move(90, 120, 10, 0.05)

    leg_move(120, 100, -10, 0.01)
    leg_move(100, 80, -10, 0.01)
    leg_move(80, 60, -10, 0.01)
    leg_move(60, 40, -10, 0.01)
    leg_move(40, 20, -10, 0.01)
    leg_move(20, 0, -10, 0.01)

    //leg return

    leg_move(0, 90, 10, 0.05)

    // left foot move 4

    left_foot_move(90, 170, 10, 0.03)

    left_foot_move(170, 90, -10, 0.03)

    // Right foot move 3

    right_foot_move(90, 170, 10, 0.03)
    right_foot_move(170, 90, -10, 0.03)







try:
    while True:
        br_dancing()



except KeyboardInterrupt:
    right_leg.angle = 90
    right_foot.angle = 90
    left_leg.angle = 90
    left_foot.angle = 90
    GPIO.cleanup()
