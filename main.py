import serial
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
# We are going to create variable to prepare packets
#Adress of the Sabertooth
address=128
command= 1
data = 64
checksum=1



match command:
    case 1 :
        print("Going reverse")
        print(data)
        print([address,command,data,checksum])
        ser.write([address,command,data,checksum])
    case 8:
        print("Going forward at speed")
        print(data)
        print([address,command,data,checksum])
        ser.write([address, command, data, checksum])
    case 20:
        print("waiting")