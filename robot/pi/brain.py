import botReceiving
import botSending

def init():
    botSending.init()
    botReceiving.init()
    # TODO: Set up Receiving to work automatically
    # TODO: Set up Sending to work automatically
    # TODO: Set up connection to Motor Controllers
    # TODO: Set up connection to Sensor Relay

# TODO: Add brain/AI functions

def quit():
    lapSending.quit()
    lapReceiving.quit()
    # TODO: Clean up Motor Controller connection
    # TODO: Clean up Sensor Relay connection

# TODO: Add code to run the bot that isn't a function