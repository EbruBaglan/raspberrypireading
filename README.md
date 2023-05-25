# raspberrypireading
A code to view gyro reading from a MPU6050 sensor(attached to Raspberry Pi) on MATLAB installed on another computer.

(Made in Bachelor's 4th year, 03/2018. Due to not having programming related course on the last semester, I went to a professor to assign me and a friend something to work on. He assigned us to help 2 PhD students with their thesis of MEMS actuated satellite. The testing phase required to measure if the aimed actuation were made, using MPU6050 and Raspberry Pi.) 

To receive the reading on the MATLAB end:
•	Minimum "MATLAB 2017b" version.
•	“MATLAB Support Package for Raspberry Pi Hardware” add-on should be installed. During the installation “Customize the existing operating system running on my hardware” option should be chosen. Then, IP, username and the password of the Raspberry Pi should be entered.

To get the IP of the Raspberry Pi:
Method1: V2 logo on the upper right corner should be clicked, and “Other ways to connect” should be chosen. 
Method2: Enter 'ifconfig' on the terminal. yazmak.
hello_world.py should be opened once in the Terminal of Rpi, just for the sensor to start sending a reading.

Enter sdt on terminal of Rasppi, then hit 'python hello_world.py'. After several readings, the code may be stopped.

The setup is ready to go.

Missing functionalities so far:
Having readings with time,
Saving on an Excel or txt file,
Filtering of the readings.

![sorun](https://github.com/EbruBaglan/raspberrypireading/assets/71343894/fc146119-118a-47c5-a3ac-afb6b79fc70a)
