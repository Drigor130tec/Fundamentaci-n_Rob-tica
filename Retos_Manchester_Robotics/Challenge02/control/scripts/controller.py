#!/usr/bin/env python
import rospy
import numpy as np
from control.msg import motor_input, motor_output, set_point
from std_msgs.msg import Float64

controller_current_speed = 0
target_speed = 0
i = 0.0

def pid_controller(_system_error, _prev_error,_Kp, _Kd, _Ki):

    global i
    dt = 0.01

    # Sistema proporcional
    p = _Kp * _system_error

    # Sistema integral
    i = _Ki * (i + _system_error * dt)

    # Sistema derivativo
    d = _Kd * (_system_error - _prev_error) / dt

    # Salidad del sistema PID
    pid_response = p + i + d

    return pid_response

# Funcion que simula el estado nulo del motor
def stop():

    global controller_pub

    # Setup the stop message (can be the same as the control message)
    print("Stopping")

    # Creacion y seteo de valores para una variable de tipo "motor_input"
    end_point = motor_input()

    end_point.input = 0.0
    end_point.time = rospy.get_time() - start_time

    # Se publica el estado nulo del motor
    controller_pub.publish(end_point)
    
    rospy.loginfo("Total Simulation Time = %f" % end_point.time)

def system_response_callback(msg):

    global controller_current_speed

    system_response = msg

    controller_current_speed = system_response.output
    system_response_time = system_response.time
    system_response_status = system_response.status

    rospy.loginfo("Motor Time: %f", system_response_time)
    rospy.loginfo("Motor Speed: %f", controller_current_speed)
    rospy.loginfo("Motor Status %s", system_response_status)
    print("\n")

def system_target_callback(msg):

    global target_speed

    system_target = msg
    target_speed = system_target.new_target
    target_time = system_target.time

    rospy.loginfo("Time: %f", target_time)
    rospy.loginfo("New   Recived: %f", target_speed)
    print("/n")

if __name__ == '__main__':

    try:

        rospy.init_node("controller", anonymous = True)

        print("The Controller is Running")
                
        controller_pub = rospy.Publisher("/motor_input", motor_input, queue_size = 1)
        error_pub = rospy.Publisher("/sys_error", Float64, queue_size = 1)

        rate = rospy.Rate(100)
        
        rospy.on_shutdown(stop)

        controller_Kp = rospy.get_param("/controller_kp")
        controller_Ki = rospy.get_param("/controller_ki")
        controller_Kd = rospy.get_param("/controller_kd")

        start_time = rospy.get_time()

        rospy.Subscriber("/set_point", set_point, system_target_callback)
        rospy.Subscriber("/motor_output", motor_output, system_response_callback)

        prev_error = 0.0

        while not rospy.is_shutdown():

            # Error del sistema
            system_error = (target_speed - controller_current_speed) * 0.100

            print("System Error: ", system_error)
            print("Target Speed: ", target_speed)
            print("Current_Speed: ", controller_current_speed)
            print("\n")

            # Respuesta del controlador PID
            pid_output = pid_controller(system_error, prev_error, controller_Kp, controller_Ki, controller_Kd)

            # Time Stamp de cuando entra el 
            pid_time = rospy.get_time() - start_time

            # Creacion y seteo de valores a una variable de tipo "motor_input"
            new_target = motor_input()

            new_target.time = pid_time
            new_target.input = pid_output

            print("Nueva señal de salida: ", new_target.input)

            # Se almacena el error previo
            prev_error = prev_error + system_error

            # Se publica el nuevo target del controlador
            error_pub.publish(system_error)
            controller_pub.publish(new_target)

            rate.sleep()

    except rospy.ROSInitException:
        pass
