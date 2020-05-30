import time
import board
import pulseio
import servo

# lower_right = pulseio.PWMOut(board.D9, duty_cycle=2**15, frequency=50)
# lower_left = pulseio.PWMOut(board.D10, duty_cycle=2**15, frequency=50)
# upper_right = pulseio.PWMOut(board.D12, duty_cycle=2**15, frequency=50)
# upper_left = pulseio.PWMOut(board.D11, duty_cycle=2**15, frequency=50)
# buzzer = pulseio.PWMOut(board.D7, variable_frequency = True)

# buzzer.duty_cycle = 2**15  # 50% duty cycle, a square wave

# loR = servo.Servo(lower_right)
# loL = servo.Servo(lower_left)
# upR = servo.Servo(upper_right)
# upL = servo.Servo(upper_left)

def A4():
    return 440
def A5():
    return 880
def E5b():
    return 622
def F5():
    return 698

#YEAH_INTRO = [A4(), E5b(), A4(), F5(), A4(), E5b(), A4(), F5()]
#YEAH_YEAH = [A5(), A5(), A5(), E5b(), A5(), A5(), A5(), E5b()]

def default():
    loR.angle = 90
    loL.angle = 90
    upR.angle = 90
    upL.angle = 90

def zigzag_outbounce():
    for i in range(0, 2, 1):
        # zigzag to right
        for angle in range(90, 135, 5):
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.01)
        buzzer.frequency = A4()
        time.sleep(0.01)

        # move right foot
        for angle in range(90, 30, -10):
            loL.angle = angle
            time.sleep(0.01)
        buzzer.frequency =  E5b()
        time.sleep(0.02)

        # move back right foot
        for angle in range(30, 90, 10):
            loL.angle = angle
            time.sleep(0.01)
        buzzer.frequency = A4()
        time.sleep(0.01)

        # back to origin
        for angle in range(135, 90, -5):
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.01)
        buzzer.frequency = F5()
        time.sleep(0.02)

        # zigzag to left
        for angle in range(90, 45, -5):
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.01)
        buzzer.frequency = A4()
        time.sleep(0.01)

         # move left foot
        for angle in range(90, 150, 10):
            loR.angle = angle
            time.sleep(0.01)
        buzzer.frequency = E5b()
        time.sleep(0.02)

        # move back left foot
        for angle in range(150, 90, -10):
            loR.angle = angle
            time.sleep(0.01)
        buzzer.frequncy = A4()
        time.sleep(0.01)

        # back to origin
        for angle in range(45, 90, 5):
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.01)
        buzzer.frequency = F5()
        time.sleep(0.02)

def zigzag_inbounce():
    for i in range (0, 2, 1):
        # zigzag to right
        for angle in range(90, 135, 5):
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.04)
        # move left foot
        for angle in range(90, 150, 10):
            loL.angle = angle
            time.sleep(0.01)
        # move back right foot
        for angle in range(150, 90, -10):
            loL.angle = angle
            time.sleep(0.01)
        # back to origin
        for angle in range(135, 90, -5):
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.04)
        # zigzag to left
        for angle in range(90, 45, -5):
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.04)
         # move right foot
        for angle in range(90, 30, -10):
            loR.angle = angle
            time.sleep(0.01)
        # move back left foot
        for angle in range(30, 90, 10):
            loR.angle = angle
            time.sleep(0.01)
        # back to origin
        for angle in range(45, 90, 5):
            upR.angle = angle
            upL.angle = angle
            time.sleep(0.04)

def waveleft():
    for i in range (0, 1, 1):
        for angle in range(90, 150, 5):
            loL.angle = angle
        for angle in range(90, 40, -5):
            loR.angle = angle
            time.sleep(0.02)
            buzzer.frequency = A5()
            time.sleep(0.01)

        for angle in range(150, 90, -5):
            loL.angle = angle
        for angle in range(40, 90, 5):
            loR.angle = angle
            time.sleep(0.02)
            buzzer.frequency = A5()
            time.sleep(0.01)

        for angle in range(90, 150, 5):
            loL.angle = angle
        for angle in range(90, 40, -5):
            loR.angle = angle
            time.sleep(0.02)
            buzzer.frequency = A5()
            time.sleep(0.01)

        for angle in range(150, 90, -5):
            loL.angle = angle
        for angle in range(40, 90, 5):
            loR.angle = angle
            time.sleep(0.03)

    for i in range (0, 1, 1):
        for angle in range(90, 150, 5):
            loL.angle = angle
        for angle in range(90, 40, -5):
            loR.angle = angle
            time.sleep(0.02)
            buzzer.frequency = A5()
            time.sleep(0.01)

        for angle in range(150, 90, -5):
            loL.angle = angle
        for angle in range(40, 90, 5):
            loR.angle = angle
            time.sleep(0.02)
            buzzer.frequency = A5()
            time.sleep(0.01)

        for angle in range(90, 150, 5):
            loL.angle = angle
        for angle in range(90, 40, -5):
            loR.angle = angle
            time.sleep(0.02)
            buzzer.frequency = A5()
            time.sleep(0.01)

        for angle in range(150, 90, -5):
            loL.angle = angle
        for angle in range(40, 90, 5):
            loR.angle = angle
            time.sleep(0.02)
            buzzer.frequency = E5b()
            time.sleep(0.01)

def waveright():
    for i in range (0, 5, 1):
        for angle in range(90, 40, -5):
            loR.angle = angle
        for angle in range(90, 150, 5):
            loL.angle = angle
            time.sleep(0.03)
        for angle in range(40, 90, 5):
            loR.angle = angle
        for angle in range(150, 90, -5):
            loL.angle = angle
            time.sleep(0.03)

# ugly dance move
def moveleft():
    for i in range (0, 2, 1):
        for angle in range(90, 130, 10):
            loL.angle = angle
            time.sleep(0.05)
        for angle in range(90, 150, 10):
            loR.angle = angle
            time.sleep(0.05)
        for angle in range(150, 90, -10):
            loR.angle = angle
        for angle in range(130, 170, 10):
            loL.angle = angle
            time.sleep(0.05)
        for angle in range(170, 90, -10):
            loL.angle = angle
            time.sleep(0.05)

default()

while 1:
    zigzag_outbounce()  # intro music
    default()
    waveleft()  # yeah part
    default()
    zigzag_inbounce()
    default()
    waveright()
    default()
