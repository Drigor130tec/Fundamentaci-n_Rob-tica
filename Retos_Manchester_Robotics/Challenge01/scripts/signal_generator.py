# !/usr/bin/env/ python
import rospy
import numpy as np
from std_msgs.msg import Float32

def talker():

    time_pub = rospy.Publisher("Time", Float32, queue_size = 10)
    signal_pub = rospy.Publisher("Signal", Float32, queue_size = 10)

    rospy.init_node("signal_generator", anonymous = True)

    rate = rospy.Rate(10)

    main_time = rospy.get_time()

    while not rospy.is_shutdown():

        tm = rospy.get_time() - main_time

        rospy.loginfo("Time: %f" % tm)
        time_pub.publish(tm)

        data = np.sin(tm)

        rospy.loginfo("Value: %f" % data)
        signal_pub.publish(data)

        rate.sleep()
    
if __name__ == '__main__':

    try:
        talker()
        
    except rospy.ROSInterruptExeption:
        pass
