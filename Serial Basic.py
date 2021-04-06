import serial

arduino = serial.Serial("COM3",9600,timeout=1)

while True:
    arduino.write(b"Hello")
    x = arduino.read(20)
    print(x)

arduino.close()