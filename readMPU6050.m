% Ebru Baglan
% 11/4/2018

% VNC Viewer
% UserName: xxx
% Password: xxx

clc
clear
close all

mypi = raspi('144.122.115.193', 'pi', 'sifre'); %'IP address', 'RPi UserName', 'RPi Password'
disableI2C(mypi) % disable to set reading rate first
mypi.I2CBusSpeed % display previous reading rate to make sure it changes with the prompt
enableI2C(mypi,400000) % set new speed in Hz
mypi.I2CBusSpeed % print the new speed, to make sure it changed

addr = scanI2CBus(mypi,'i2c-1'); % get the addresses of sensors on I2C

i2csensor_1 = i2cdev(mypi,'i2c-1',char(addr(1))); % get the first sensor
%i2csensor_2 = i2cdev(mypi,'i2c-1',char(addr(2))); %ikinci adresi atiyoruz
i=1; 

figure(1) 
xlabel('Sample #')
ylabel('Acceleration [g]')
%ylabel('Rotation rate [{\circ}/s]]') %y label attik, gyrolar icin
hold on
%legend('X','Y','Z') %legend atiyoruz

while 1
    x(i)=i; % number the samplings
    acc_x_out(i) = -double(readRegister(i2csensor_1,59,'int8'))/64.0; % 8-bit integers
    acc_y_out(i) = -double(readRegister(i2csensor_1,61,'int8'))/64.0;
    acc_z_out(i) = -double(readRegister(i2csensor_1,63,'int8'))/64.0;
%   figure(1)
    subplot(211), plot(x,acc_x_out(1:i),'LineWidth',1.5,'Color','r'), hold on
    plot(x,acc_y_out(1:i),'LineWidth',1.5,'Color','g')  % y acc
    plot(x,acc_z_out(1:i),'LineWidth',1.5,'Color','b')  % z acc
    xlim([i-200 i+200]) % limit for x axis, last 200 readings on the screen
    ylim([-2 2])   % acceleration in g cinsinden +- 2g max

    gyro_x_out(i) = -double(readRegister(i2csensor_1,67,'int8'))*250.0/128.0;
    gyro_y_out(i) = -double(readRegister(i2csensor_1,69,'int8'))*250.0/128.0;
    gyro_z_out(i) = -double(readRegister(i2csensor_1,71,'int8'))*250.0/128.0;
    subplot(212),    plot(x,gyro_x_out(1:i),'LineWidth',1.5,'Color','r'), hold on
    
    plot(x,gyro_y_out(1:i),'LineWidth',1.5,'Color','g')
    plot(x,gyro_z_out(1:i),'LineWidth',1.5,'Color','b')
    
    xlim([i-200 i+200])
    ylim([-250 250])
    i=i+1;
end

%%%%%%%%%%%%%%%%%%%%%read(i2csensor_1,8)
%%%%%%%%%%%%%%%%%%%%%read(i2csensor_2,8)
%%%%%%%%%%%%%%%%%%%%%temp = readRegister(i2csensor_1,42) %/255 * (340)
%writeRegister(dev,register,dataIn)    %registerlara bi sey gonderilecekse
%bu komut kullaniliyo. simdiki kodda bi islevi yok