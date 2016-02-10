#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import termios, sys, os

def getkey():
    term = open("/dev/tty", "r")
    fd = term.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] &= ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
        term.close()
    return c

def talker():
    pub = rospy.Publisher('angle', Float32, queue_size=10)
    rospy.init_node('talker', anonymous=True)  
    angle = 90.0
    c = ' '
    print 'Use +- keys to increase/decrease servo angle'
    while not rospy.is_shutdown():
        c = getkey()
        if c == '-':
            angle = angle - 1
            pub.publish(angle)
        if c == '+':
            angle = angle + 1
            pub.publish(angle)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
