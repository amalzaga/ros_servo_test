#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

import Adafruit_BBIO.PWM as PWM 

servo_pin = "P9_14" 
duty_min = 3 
duty_max = 14.5 
duty_span = duty_max - duty_min 


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    duty = 100 - ((float(data.data) * 0.00556) * duty_span + duty_min)
    PWM.set_duty_cycle(servo_pin, duty)

def listener():


    rospy.init_node('listener', anonymous=False)
    
    PWM.start(servo_pin,93, 60.0,1)

    rospy.Subscriber('angle', Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    PWM.stop(servo_pin)
    PWM.cleanup()

if __name__ == '__main__':
    listener()
