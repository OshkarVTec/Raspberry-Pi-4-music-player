import serial
ser=serial.Serial(
port='/dev/ttyACM0',
baudrate= 19200,
parity= serial.PARITY_NONE,
stopbits= serial.STOPBITS_ONE,
bytesize= serial.EIGHTBITS,timeout=1)
while(1):
    letra = ser.readline(ser.in_waiting)
    if letra != b'':
        print(letra)