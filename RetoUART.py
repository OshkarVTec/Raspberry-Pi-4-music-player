import serial
ser=serial.Serial(
port='/dev/ttyACM0',
baudrate= 19200,
parity= serial.PARITY_NONE,
stopbits= serial.STOPBITS_ONE,
bytesize= serial.EIGHTBITS,timeout=1)
def readUart():
    keypadData = ser.readline(ser.in_waiting)
    return keypadData