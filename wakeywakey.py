import smbus
import math
import time
import timeit

# Power Management Registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

text_file = open("Outputs.txt", "w")
text_file.write("\t\t   Time\t     gyro_xout\t\tgyro_yout\t\tgyro_zout\t\taccel_xout\t\taccel_yout\t\taccel_zout\t\tx_dond\t\ty_dond\n")

def read_byte(adr):
 return bus.read_byte_data(address, adr)

def read_word(adr):
 high = bus.read_byte_data(address, adr)
 low = bus.read_byte_data(address, adr+1)
 val = (high << 8) + low
 return val

def read_word_2c(adr):
 val = read_word(adr)
 if (val >= 0x8000):
	return -((65535 - val) + 1)
 else:
	return val

def dist(a,b):
 return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
 radians = math.atan2(x, dist(y,z))
 return -math.degrees(radians)

def get_x_rotation(x,y,z):
 radians = math.atan2(y, dist(x,z))
 return math.degrees(radians)


bus = smbus.SMBus(1)
address = 0x68 #MPU6050 I2C address

# The following line is to wake MPU6050s up, since they are in sleep mode initially
bus.write_byte_data(address, power_mgmt_1, 0)

now_initial = timeit.default_timer()

while True:
 time.sleep(0.1)

 # Read the gyro registers
 gyro_xout = read_word_2c(0x43)
 gyro_yout = read_word_2c(0x45)
 gyro_zout = read_word_2c(0x47)

 print "Gyro X : ", gyro_xout, " scaled: ", (gyro_xout / 131)
 print "Gyro Y : ", gyro_yout, " scaled: ", (gyro_yout / 131)
 print "Gyro Z : ", gyro_zout, " scaled: ", (gyro_zout / 131)
 
 # Read accelerometer registers
 accel_xout = read_word_2c(0x3b)
 accel_yout = read_word_2c(0x3d)
 accel_zout = read_word_2c(0x3f)

 accel_xout_scaled = accel_xout / 16384.0
 accel_yout_scaled = accel_yout / 16384.0
 accel_zout_scaled = accel_zout / 16384.0

 print "Acc X: ", accel_xout, " scaled: ", accel_xout_scaled
 print "Acc Y: ", accel_yout, " scaled: ", accel_yout_scaled
 print "Acc Z: ", accel_zout, " scaled: ", accel_zout_scaled
 
 x_dond = get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
 y_dond = get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
 now_now = timeit.default_timer()

 print "X rot: " , x_dond
 print "Y rot: " , y_dond
 #print "Z rot: " , get_z_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
 
 print now_now - now_initial
 
 text_file.write("Outputs: %f\t%f\t\t%f\t\t%f\t\t%f\t\t%f\t\t%f\t\t%f\t%f\n" %(now_now - now_initial,gyro_xout/ 131.0,gyro_yout/ 131.0,gyro_zout/ 131.0,accel_xout_scaled,accel_yout_scaled,accel_zout_scaled,x_dond,y_dond))


 time.sleep(0.05)
