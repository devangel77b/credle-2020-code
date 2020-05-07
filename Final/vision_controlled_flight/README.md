# Tello-Video
?

#Credle Notes

First, ensure Tello is connected (Tello command).
Light will flash yellow.
Second, run main.py.
Use python vice python3. 
From Laptop, use this main.py from this folder (V_I2 vice V_I)
Thresholded for yellow color.


Process

Original plan was to integrate gate-detection program into main loop.
Issue with main function initializing loops in control_ui.
Then attempted to make function inside control_ui.
Issue with modifying GUI, we were going to have to edit the library.
Then attempted to change the image after it was retrieved from
drone but before being placed into the GUI.
Image was already in an np array, so no formating issues.
Created a function inside the class with the masking from gate-detection.
Had the class run that function between the image retrieval and GUI update.
Masking was modified from values for laptop camera to values for drone.

Next step is to introduce new function, called inside the mask function.
Function will find center of mask and compare to center of image.
Function will then give flight directions to drone (fly left, fly right).

