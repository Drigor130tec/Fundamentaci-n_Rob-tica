
#Instrucciones para descargar y compilar el paquete "control"

Estas instrucciones le guiarán a través del proceso de descarga y compilación de un paquete de ROS. 

###Descargar el paquete
Abra una terminal y vaya al directorio src de su espacio de trabajo de ROS:

	cd ~/catkin_ws/src

Clone el repositorio que contiene el paquete que desea descargar:

	git clone https://github.com/Drigor130tec/Fundamentaci-n_Rob-tica/tree/main/Retos_Manchester_Robotics/Challenge02

###Compilar el paquete

 Regrese al directorio raíz de su espacio de trabajo de ROS:

	cd ~/catkin_ws

Compile el paquete utilizando catkin_make:

	catkin_make

Asegúrese de que su espacio de trabajo se haya creado correctamente:

	source devel/setup.bash

###  Ejecutar el paquete
Ejecute el nodo que desea ejecutar. Por ejemplo, si el paquete contiene un nodo llamado my_node:

	roslaunch control motor_control.launch

Si todo sale bien se deberia de desplegar la herramienta rqt_plot

![graphh](https://user-images.githubusercontent.com/70008088/221770987-b20601d5-0f52-47c3-b23f-6f2d71b7b3a2.png)


