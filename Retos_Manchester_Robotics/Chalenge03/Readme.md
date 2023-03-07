# Instrucciones para descargar y compilar el paquete "control"

Estas instrucciones le guiarán a través del proceso de descarga y compilación de un paquete de ROS. 


![reto](https://user-images.githubusercontent.com/70008088/223325948-b3e972aa-e67c-4b1c-bbfe-f8eb321d0b4f.jpg)

### Descargar el paquete
Abra una terminal y vaya al directorio src de su espacio de trabajo de ROS:

	cd ~/catkin_ws/src

Clone el repositorio que contiene el paquete que desea descargar:

	git clone https://github.com/Drigor130tec/Fundamentaci-n_Rob-tica/tree/main/Retos_Manchester_Robotics/Chalenge03

### Compilar el paquete

 Regrese al directorio raíz de su espacio de trabajo de ROS:

	cd ~/catkin_ws

Compile el paquete utilizando catkin_make:

	catkin_make

Asegúrese de que su espacio de trabajo se haya creado correctamente:

	source devel/setup.bash

### Ejecutar el paquete
Ejecute el nodo que desea ejecutar. Por ejemplo, si el paquete contiene un nodo llamado my_node:

	roslaunch chalenge03 motor.launch

Si todo sale bien, este es el resultado que deberias de obetener


https://user-images.githubusercontent.com/70008088/223326050-6df6cddb-eab5-4be8-8b4b-64c2b8ac7525.mp4



