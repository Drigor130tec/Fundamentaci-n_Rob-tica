# !/usr/bin/env/ python
import rospy
import numpy as np
from std_msgs.msg import Float32

tmp = 0.0
value = 0.0

def callback_time(msg):
    
    global tmp
    tmp = msg.data

    rospy.loginfo("Tiempo Recibido: %f" % tmp)

def callback_signal(msg):

    global value
    value = msg.data

    rospy.loginfo("f(x) Recibido %f" % value)

def init():

    rqt_pub = rospy.Publisher("Proc_signal", Float32, queue_size = 10)

    rospy.init_node("process", anonymous = True)

    rospy.Subscriber("Time", Float32, callback_time)
    rospy.Subscriber("Signal", Float32, callback_signal)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        global tmp
        global value

        new_value = 0.5 * ((np.sin(tmp) * np.cos(np.pi)) + (np.cos(tmp) * np.sin(np.pi))) + 0.5

        rospy.loginfo("Dato modificado: %f" % new_value)
        rqt_pub.publish(new_value)

        rate.sleep()

if __name__ == '__main__':

    
    try:
        init()
        
    except rospy.ROSInterruptExeption:
        pass
