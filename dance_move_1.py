import time
import board
import pulseio
import servo

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

# Define a list of tones/music notes to play
TONE = [262, 294, 330, 349, 392, 440, 494]
LITTLE_STAR = [E4(), E4(), B4(), B4(), C_sharp(), C_sharp(), B4(),
            A4(), A4(), G_sharp(), G_sharp(), F_sharp(), F_sharp(), E4(),
            B4(), B4(), A4(), A4(), G_sharp(), G_sharp(), F_sharp(),
            B4(), B4(), A4(), A4(), G_sharp(), G_sharp(), F_sharp(),
            E4(), E4(), B4(), B4(), C_sharp(), C_sharp(), B4(),
            A4(), A4(), G_sharp(), G_sharp(), F_sharp(), F_sharp(), E4()]

# Create piezo buzzer PWM output
# Change the pin number!
buzzer = pulseio.PWMOut(board.D5, variable_frequency = True)

# Start at the first note and start making sound
melody_index = 0
buzzer.frequency = TONE[melody_index]
buzzer.duty_cycle = 2**15  # 50% duty cycle, a square wave

lower_right = pulseio.PWMOut(board.D9, duty_cycle=2**15, frequency=50)
lower_left = pulseio.PWMOut(board.D10, duty_cycle=2**15, frequency=50)
upper_right = pulseio.PWMOut(board.D12, duty_cycle=2**15, frequency=50)
upper_left = pulseio.PWMOut(board.D11, duty_cycle=2**15, frequency=50)

loR = servo.Servo(lower_right)
loL = servo.Servo(lower_left)
upR = servo.Servo(upper_right)
upL = servo.Servo(upper_left)

# Main loop for dance movement and melody
while (buzzer.frequency):
    for angle in range(45, 135, 5):
        loR.angle = angle
        time.sleep(0.5)
    for angle in range(135, 45, -5):
        loL.angle = angle
        time.sleep(0.5)
    for angle in range(135, 0, -5):
        upR.angle = angle
        time.sleep(0.5)
    for angle in range(45, 135, 5):
        upL.angle = angle
        time.sleep(0.5)
    buzzer.frequency = TONE[melody_index++]
    time.sleep(2.0)
    
#while True:
    # Play tones going from start to end of list
    # for i in range(len(LITTLE_STAR)):
    #    buzzer.frequency = TONE[i]
    #    time.sleep(0.5) # Half second delay

    # Then play tones going from end to start of list
    # for i in range(len(LITTLE_STAR) -1, -1, -1):
    #    buzzer.frequency = TONE[i]
    #    time.sleep(0.5)
