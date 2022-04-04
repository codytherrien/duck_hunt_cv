# duck_hunt_cv

This is a computer vision project to play the classic NES game Duck Hunt. The auto-aim algorithm used in this implementation uses a YOLOv5 nano model fine tuned on a corpus of 250 images of game play. YOLOv5 is a state-of-the-art object detection model. Here it is used to locate ducks and the algorithm move the crosshairs to the location indicated by the model. 

This project requires a python 3.7 environment. To run simply install the requirements and the .whl file using pip. 
