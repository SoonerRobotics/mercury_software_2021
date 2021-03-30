import botReceiving
import botSending
import serial
import json

def init():
    botSending.init()
    botReceiving.init()
    # TODO: Set up Receiving to work automatically
    # TODO: Set up Sending to work automatically
    serMotor = serial.Serial() # Connection to Motor Controllers
    serMotor.baudrate = 38400
    serMotor.port = "COM9"
    serMotor.open()
    # TODO: Set up connection to Sensor Relay

# TODO: Add brain/AI functions

# dataSend needs to be a dictionary of data to send
def commandMotors(dataSend):
    serMotor.write(json.dumps(dataSend).encode("utf-8"))
    dataRead = serMotor.readline().decode("utf-8")
    # TODO: Throw errors or something if the Motor Controller pong response notes an issue

def pollSensors():
    # TODO: Add code to retrieve sensor data and format it

def quit():
    lapSending.quit()
    lapReceiving.quit()
    # TODO: Clean up Motor Controller connection
    # TODO: Clean up Sensor Relay connection

# TODO: Add code to run the bot that isn't a function