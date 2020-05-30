import time
import board
import pulseio

# import california_gurls.py

# def C4():
#     return 262
# def C_sharp():
#     return 277
# def D4():
#     return 294
# def E4():
#     return 330
# def F4():
#     return 349
# def F_sharp():
#     return 370
# def G4():
#     return 392
# def G_sharp():
#     return 415
# def A4():
#     return 440
# def B4():
#     return 494

# LITTLE_STAR = [C4(), C4(), G4(), G4(),
#                A4(), A4(), G4(), G4(),
#                F4(), F4(), E4(), E4(),
#                D4(), D4(), C4(), C4(),
#                G4(), G4(), F4(), F4(),
#                E4(), E4(), D4(), D4(),
#                G4(), G4(), F4(), F4(),
#                E4(), E4(), D4(), D4(),
#                C4(), C4(), G4(), G4(),
#                A4(), A4(), G4(), G4(),
#                F4(), F4(), E4(), E4(),
#                D4(), D4(), C4(), C4()]

# PAUSES =      [1, 1, 1, 1,
#                1, 1, 1, 0,
#                1, 1, 1, 1,
#                1, 1, 1, 0,
#                1, 1, 1, 1,
#                1, 1, 1, 0,
#                1, 1, 1, 1,
#                1, 1, 1, 0,
#                1, 1, 1, 1,
#                1, 1, 1, 0,
#                1, 1, 1, 1,
#                1, 1, 1, 0]

# Create piezo buzzer PWM output
# Change the pin number!
buzzer = pulseio.PWMOut(board.D7, variable_frequency = True)

# Start at the first note and start making sound
# buzzer.frequency = TONE[0]
buzzer.duty_cycle = 2**15  # 50% duty cycle, a square wave

pause_length = 0.1
quarter_note = 0.4


# Main loop will go thru each tone in order up and down
# while True:
    # Play tones going from start to end of list
for i in range(len(LITTLE_STAR)) :
    if (PAUSES[i] == 1) :
        buzzer.frequency = 0.1 # off
        time.sleep(pause_length)
        buzzer.frequency = NOTES[i]
        time.sleep(quarter_note - pause_length)
    else :
        buzzer.frequency = NOTES[i]
        time.sleep(quarter_note)

    #     # Then play tones going from end to start of list
    #  for i in range(len(LITTLE_STAR) -1, -1, -1):
    #      buzzer.frequency = TONE[i]
    #      time.sleep(0.5)
