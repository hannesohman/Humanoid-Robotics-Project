import serial
from serial.tools import list_ports
import time

# Open serial connection to Arduino
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Change COM port as needed
time.sleep(2)  # wait for Arduino reset


def sign(letter):
    print(f"SIGNING {letter}")
    arduino.write((letter.upper() + "\n").encode())

def spell(word):
    print(f"SPELLING {word}")
    for letter in word:
        sign(letter)
        time.sleep(0.30)


print("Type commands like: A, B, ABCDEFG")
while True:
    command = input("> ").upper()
    if command == "EXIT":
        break
    elif len(command) > 1:
        message = command
        message = message.replace(" ", "")
        spell(message)
    else:
        arduino.write((command + "\n").encode())  # send command


# A B F K
# LMNOPQRSTUVWXYZÅ