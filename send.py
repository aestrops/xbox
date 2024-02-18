import serial
ser = serial.Serial("/dev/cu.usbserial-0001", 9600)
byte_to_send = 0x43
ser.write(byte_to_send.to_bytes(1, "little"))
while True:
    command=input()
    if command=="close":
        ser = serial.Serial("/dev/cu.usbserial-0001", 9600)
        byte_to_send = 0x42
        ser.write(byte_to_send.to_bytes(1, "little"))
    if command=="open":
        ser = serial.Serial("/dev/cu.usbserial-0001", 9600)
        byte_to_send = 0x41
        ser.write(byte_to_send.to_bytes(1, "little"))