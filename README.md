# SR-Compiler

Designed as a replacement to the robotics IDE if you have code on your computer or on github or somewhere and want to compile it without having to copy it all onto the Student Robotics IDE.


Any code you wish to compile goes outside of the compiler folder and then you modify compiler/files.json to hold the path from just outside the compiler folder as the base, such as example.py and then the destination address once it is inside the robot.zip. This can also handle folders in the example of folder-example.py

Once you have done that you run compiler/compiler.py and it creates compiler/robot.zip which can then be copied into your memory stick to run.
