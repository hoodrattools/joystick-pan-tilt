from adafruit_motor import servo
import pwmio
import board
import time
import analogio

x = analogio.AnalogIn(board.A0)
y = analogio.AnalogIn(board.A2)


pwm1 = pwmio.PWMOut(board.TX, duty_cycle=2 ** 15, frequency=50)
serv = servo.Servo(pwm1)
pwm2 = pwmio.PWMOut(board.RX, duty_cycle=2 ** 15, frequency=50)
serv2 = servo.Servo(pwm2)

serv.angle = 20
angle = 0
angle2 = 50

while True:
    if x.value > 40000:
        if serv.angle < 179:
            print('up')
            angle = (angle+1)
            serv.angle = (angle)
            time.sleep(0.002)
    if x.value < 15000:
        if serv.angle > 1:
            print('down')
            angle = (angle - 1)
            serv.angle = angle
            time.sleep(0.002)
            
    if y.value > 40000:
        if serv2.angle < 179:
            print('up')
            angle2 = (angle2+1)
            serv2.angle = (angle2)
            time.sleep(0.002)
    if y.value < 15000:
        if serv2.angle > 2:
            print('down')
            angle2 = (angle2 - 1)
            serv2.angle = angle2
            time.sleep(0.002)
