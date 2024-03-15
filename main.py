import serial
from time import sleep
ser = serial.Serial(port='/dev/tty8', baudrate=9600)
# We are going to create variable to prepare packets
# configuration de la baurate de la sabertooth
sleep(2)
ser.write(170)
#Adress of the Sabertooth
address=128
#Il y a 13 commande disponible elle sont dispo a la fin du programes
command= int(input("Quel commande souhaitez vous executer ?(1 ou 8):"))
data = int(input("donnez la valeur :"))
checksum= (address+command+data) & 0b01111111



if command == 1:
    print("Going reverse")
    print(data)
    print([address, command, data, checksum])
    ser.write([address, command, data, checksum])
elif command == 8:
    print("Going forward at speed")
    print(str(data))
    print([address, command, data, checksum])
    ser.write([address, command, data, checksum])
elif command == 20:
    print("Waiting")
else:
    print("Invalid command")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
0: Drive forward motor 1 (decimal 0, binary 0b00000000, hex 0h00)
This is used to command motor 1 to drive forward. Valid data is 0-127 for off to full forward
drive. If a command of 0 is given, the Sabertooth will go into power save mode for motor 1 after
approximately 4 seconds.
1: Drive backwards motor 1 (decimal 1, binary 0b00000001, hex 0h01)
This is used to command motor 1 to drive backwards. Valid data is 0-127 for off to full reverse
drive. If a command of 0 is given, Sabertooth will go into power save mode for motor 1 after
approximately 4 seconds.
2: Min voltage (decimal 2, binary 0b00000010, hex 0h02)
This is used to set a custom minimum voltage for the battery feeding the Sabertooth. If the
battery voltage drops below this value, the output will shut down. This value is cleared at startup,
so much be set each run. The value is sent in .2 volt increments with a command of zero
corresponding to 6v, which is the minimum. Valid data is from 0 to 120. The function for
converting volts to command data is
Value = (desired volts-6) x 5
3: Max voltage (decimal 3, binary 0b0000011, hex 0h03)
This is used to set a custom maximum voltage. If you are using a power supply that cannot sink
current such as an ATX supply, the input voltage will rise when the driver is regenerating
(slowing down the motor.) Many ATX type supplies will shut down if the output voltage on the
12v supply rises beyond 16v. If the driver detects an input voltage above the set limit, it will put
the motor into a hard brake until the voltage drops below the set point again. This is inefficient,
because the energy is heating the motor instead of recharging a battery, but may be necessary.
The driver comes preset for a maximum voltage of 30V. The range for a custom maximum
voltage is 0v-25v. The formula for setting a custom maximum voltage is
Value = Desired Volts*5.12
If you are using any sort of battery, then this is not a problem and the max voltage should be left
at the startup default.
4: Drive forward motor 2 (decimal 4, binary 0b00000100, hex 0h04)
This is used to command motor 2 to drive forward. Valid data is 0-127 for off to full forward
drive. If a command of 0 is given, the Sabertooth will go into power save mode for motor 2 after
approximately 4 seconds.
5: Drive backwards motor 2 (decimal 5, binary 0b00000101, hex 0h05)
This is used to command motor 2 to drive backwards. Valid data is 0-127 for off to full reverse
drive. If a command of 0 is given, the Sabertooth will go into power save mode after
approximately 4 seconds.
6: Drive motor 1 7 bit (decimal 6, binary 0b00000110, hex 0h06)
This command is used to drive motor 1. Instead of the standard commands 0 and 1, this one
command can be used to drive motor 1 forward or in reverse, at a cost of lower resolution. A
command of 0 will correspond to full reverse, and a command of 127 will command the motor to
drive full forward. A command of 64 will stop the motor.
7: Drive motor 2 7 bit (decimal 7, binary 0b00000111, hex 0h07)
This command is used to drive motor 2. Instead of the standard commands 4 and 5, this one
command can be used to drive motor 1 forward or in reverse, at a cost of lower resolution. A
command of 0 will correspond to full reverse, and a command of 127 will command the motor to
drive full forward. A command of 64 will stop the motor.
Mixed mode commands:
Sabertooth can also be sent mixed drive and turn commands. When using the mixed mode
commands, please note that the Sabertooth requires valid data for both drive and turn before it
will begin to operate. Once both initial data packets have been sent, then turn or drive commands
may be sent as needed. You should design your code to either use the independent or the mixed
commands. Switching between the command sets will cause the vehicle to stop until new data is
sent for both motors.
8: Drive forward mixed mode (decimal 8, binary 0b00001000, hex 0h08)
This is used to command the vehicle to drive forward in mixed mode. Valid data is 0-127 for off
to full forward drive.
9: Drive backwards mixed mode (decimal 9, binary 0b00001001, hex 0h09)
This is used to command the vehicle to drive backwards in mixed mode. Valid data is 0-127 for
off to full reverse drive.
10: Turn right mixed mode (decimal 10, binary 0b00001010, hex 0h0a)
This is used to command the vehicle to turn right in mixed mode. Valid data is 0-127 for zero to
maximum turning speed.
11: Drive turn left mixed mode (decimal 11, binary 0b00001011, hex 0h0b)
This is used to command the vehicle to turn left in mixed mode. Valid data is 0-127 for zero to
maximum turning speed.
12: Drive forwards/back 7 bit (decimal 12, binary 0b00001100, hex 0h0c)
This is used to command the vehicle to move forwards or backwards. A command of 0 will
cause maximum reverse, 64 will cause the vehicle to stop, and 127 will command full forward.
13: Turn 7 bit (decimal 13, binary 0b00001101, hex 0h0d)
This is used to command the vehicle to turn right or left. A command of 0 will cause maximum
left turn rate, 64 will cause the vehicle to stop turning , and 127 will command maximum right
turn rate.
'''
