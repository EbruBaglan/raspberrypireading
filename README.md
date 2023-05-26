# MPU6050 + RPi
A code to view gyro reading from a MPU6050 sensor(attached to Raspberry Pi) on MATLAB on a remote computer.

(Made in Bachelor's 4th year, 03/2018. Due to not having programming related course on the last semester, I went to a professor to assign me and a friend something to work on. He assigned us to help 2 PhD students with their thesis on an satellite system which is driven by MEMS vibration actuators. The testing phase of the study required to measure if the aimed actuation were obtained or not, using MPU6050 and Raspberry Pi.) 

To receive the reading on the MATLAB end:
•	Minimum "MATLAB 2017b" version is required.
•	“MATLAB Support Package for Raspberry Pi Hardware” add-on should be installed. During the installation “Customize the existing operating system running on my hardware” option should be chosen. Then, IP, username and the password of the RPi should be entered.

To get the IP of the RPi:
Method1: Click on the V2 logo on the upper right corner, and choose “Other ways to connect”. 
Method2: Enter 'ifconfig' on the terminal.

wakeywakey.py should be opened once on the Terminal of Rpi, just for the sensor to start sending a reading.

Enter sdt on terminal of RPi, then hit 'python hello_world.py'. After several readings, the code may be stopped.
(Note I don't remember what I assigned on sdt by now. If I have RPi again, I will check for it!)

# The setup is ready to go.

This was not the last version we submitted, but I could not find the newer version of these.
Further improvements of the code included
Having readings with time,
Saving on an Excel or txt file,
Filtering of the readings.

This happened on the way of reading, but then resolved.
![sorun](https://github.com/EbruBaglan/raspberrypireading/assets/71343894/fc146119-118a-47c5-a3ac-afb6b79fc70a)
