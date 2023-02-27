#!/usr/bin/env python
import rospy
import numpy as np
from control.msg import motor_input, motor_output, set_point

global prev_error, target_speed, controller_current_speed

prev_error = 0
target_speed = 0

def pid_controller(_system_error, _Kp, _Kd, _Ki):

    i = 0
    dt = 0.01

    p = _Kp * _system_error
    i = _Ki * (i + _system_error * dt)
    d = _Kd * (_system_error - prev_error) / dt

    pid_response = p + i + d

    return pid_response

def stop():

    global controller_pub

    #Setup the stop message (can be the same as the control message)
    print("Stopping")

    end_point = motor_input()
    end_point.input = 0.0
    end_point.time = rospy.get_time() - start_time

    controller_pub.publish(end_point)
    
    rospy.loginfo("Total Simulation Time = %f" % end_point.time)

def system_response_callback(msg):

    controller_current_speed = msg.output
    system_response_time = msg.time
    system_response_status = msg.status

    rospy.loginfo("Time: %f", system_response_time)
    rospy.loginfo("New Status Recived: %s", system_response_status)
    print("/n")

def system_target_callback(msg):

    target_speed = msg.new_target
    target_time = msg.time

    rospy.loginfo("Time: %f", target_time)
    rospy.loginfo("New Target Recived: %f", target_speed)
    print("/n")

if __name__ == '__main__':

    rospy.init_node("controller", anonymous = True)
    rate = rospy.Rate(100)
    rospy.on_shutdown(stop)

    try:

        print("The Controller is Running")
                
        controller_pub = rospy.Publisher("motor_input", motor_input, queue_size = 1)
        setpoint_sub = rospy.Subscriber("set_point", set_point, system_target_callback)
        system_sub = rospy.Subscriber("motor_output", motor_output, system_response_callback)

        controller_Kp = rospy.get_param("/controller_kp", 1.0)
        controller_Ki = rospy.get_param("/controller_ki", 0.0)
        controller_Kd = rospy.get_param("/controller_kd", 0.0)
        controller_current_speed = rospy.get_param("/controller_current_speed", 0)

        start_time = rospy.get_time()

        while not rospy.is_shutdown():

            system_error = target_speed - controller_current_speed

            pid_output = pid_controller(system_error, controller_Kp, controller_Ki, controller_Kd)

            pid_time = rospy.get_time() - start_time

            new_target = motor_input()
            new_target.input = pid_output
            new_target.time = pid_time

            prev_error = system_error

            controller_pub.publish(new_target)

            rate.sleep()

    except rospy.ROSInitException:
        pass

