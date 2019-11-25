import MPU6050
import time

mpu = MPU6050.MPU6050() #class untuk MPU6050
accel = [0]*3 #untuk store accelerometer data
gyro = [0]*3 #untuk store gyroscope data
def setup():
	mpu.dmp_initialize() #inisialisasi MPU6050

def loop():
	while (True):
		accel = mpu.get_acceleration() 	#get accelerometer data
		gyro = mpu.get_rotation() #get gyroscope data
		print("a/g:%d\t%d\t%d\t%d\t%d\t%d"%(accel[0],accel[1]accel[2],gyro[0],gyro[1],gyro[2]))
		print("a/g:%.2f g\t%.2f g\t%.2f g\t%.2f d/s\t%.2f d/s\t%.2f d/s"%(accel[0]/16384.0,accel[1]/16384.0,accel[2]/16384.0,gyro[0]/131.0,gyro[1]/131.0,gyro[2]/131.0))
		time.sleep(0,1)

if __name__ == '__main__': #mulai program disini
	print("Mulai untuk alat . . . ")
	setup()
	try:
		loop()
	except KeyboardInterrupt: #untuk exit saat menekan Ctrl+C
		pass