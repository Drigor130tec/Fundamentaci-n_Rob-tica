# Instrucciones
Para poder compilar y ejecutar cada uno de los códigos de manera correcta en ROS, es necesario seguir los siguientes pasos:

 - Copia la carpeta *"courseworks"* junto con todo el contenido dentro del folder *"src"* de tu *"catkin_ws"*
 -  `cd ~/catkin_ws`
 - `catkin_make`
 - `source devel/setup.bash`
 - `roscore`
 - En una nueva terminal ejecuta `source devel/setup.bash`
 - `roslaunch courseworks courseworks.launch`
 
 Posteriormente  se podrá ejecutaran 3 ventanas, a la que hay que prestarle atención es la ventana de "rqt_graph", aquí es donde se van a desplegar las graficas de las señales resultantes.
