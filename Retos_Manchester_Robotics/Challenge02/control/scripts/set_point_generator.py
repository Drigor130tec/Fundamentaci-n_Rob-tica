#!/usr/bin/env python
import rospy
import numpy as np
from control.msg import set_point

# Funcion que genera puntos entre -100 y 100 con intervalos de 10
def new_data(_max_power, _min_power, _current_power):

    global flag

    if flag:

        if _current_power < _max_power:

            _current_power = _current_power + 1
                
        else: 

            flag = False

    else:

        if _current_power > _min_power:

            _current_power = _current_power - 1
                
        else:
                    
            flag = True

    return _current_power

if __name__ == '__main__':

    try:

        rospy.init_node("set_point_generator")

        setpoint_pub = rospy.Publisher("/set_point", set_point, queue_size = 1)

        max_power = rospy.get_param("/setpoint_singal_amplitud", 100)
        min_power = rospy.get_param("/setpoint_signal_frecuency", -100)
        current_power = rospy.get_param("/setpoint_current_power", 0)

        start_time = rospy.get_time()

        rate = rospy.Rate(100)

        new_point = set_point()

        flag = True

        while not rospy.is_shutdown():
            
            current_power = new_data(max_power, min_power, current_power)

            new_point.time = rospy.get_time() - start_time
            new_point.new_target = current_power

            rospy.loginfo("Time: %f" % new_point.time)
            rospy.loginfo("New Target: %f" % new_point.new_target)
            print("\n")

            setpoint_pub.publish(new_point)

            rate.sleep()

    except rospy.ROSInitException:

        pass
