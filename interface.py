import serial
from serial.tools import list_ports
import time

# for port in list_ports.comports():
#     print(port.pid)
#     if port.pid == 67: # replace with the pid of your device
#         print(port.name)
#         ser = serial.Serial(port.name)

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


## ARDUINO CODE:

# void loop() {
#   if (Serial.available() > 0) {
#     String command = Serial.readStringUntil('\n'); // read incoming text

#     if (command.startsWith("MOVE1")) {
#       int angle = command.substring(6).toInt();
#       servo1.write(angle);
#     } 
#     else if (command.startsWith("MOVE2")) {
#       int angle = command.substring(6).toInt();
#       servo2.write(angle);
#     } 
#     else if (command == "WAVE") {
#       for (int i = 0; i < 3; i++) {
#         servo1.write(0);
#         delay(300);
#         servo1.write(90);
#         delay(300);
#       }
#     }
#   }
# }