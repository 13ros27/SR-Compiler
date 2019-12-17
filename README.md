# SR-Compiler

Designed as a replacement to the robotics IDE if you have code on your computer or on github or somewhere and want to compile it without having to copy it all onto the Student Robotics IDE.


Before this runs the first time you will need to create any robot.zip from the Student Robotics IDE, extract it and find the wifi.yaml file. This will need to be copied into the compiler folder of this code, replacing the blank file there

Any code you wish to compile goes outside of the compiler folder and then you modify compiler/files.json to hold the path from just outside the compiler folder as the base, such as example.py and then the destination address once it is inside the robot.zip. This can also handle folders in the example of folder_example.py

Once you have done that you run compiler/compiler.py and it creates compiler/robot.zip which can then be copied into your memory stick to run.

v1.1 also allows you to specify a `__destination__` in files.json which will aim where the robot.zip is created so that it can be created directly onto your USB drive if it is plugged in.
