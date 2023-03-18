# Virtual-Piano
A virtual piano made using Python is a software application that simulates a piano keyboard on a computer. The program uses Python programming language to create a  virtual piano keyboard on the screen.

In the present digital world, It would be difficult for the composers or musicians without an instrument to play music. This project has dominance over here. It enables/allow the musician to play an instrument without the actual instrument. he only needs to play with hands in space.

The virtual piano can be played using the hand Gestures . When a key is pressed by gestures, using thumb and index finger, the corresponding sound is played through the computer's speakers or external audio interface.

The program can be accessed and downloaded from Github. The code for the virtual piano is stored in a repository, which contains all the files and code necessary to run the program.

The virtual piano can be customized by changing the keyboard layout, adding new sounds. It can also be integrated into other Python projects or used as a standalone application for music education or entertainment purposes.

MODULES TO BE IMPORTED:

import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import cvzone
import math
from time import sleep
import pyglet

The layout of Piano is very simple. It contains one octave of notes ranging from C4 to C5.

It works good and accurate with a FHD camera

NOTE: A minor bug related to virtual piano is that the note might play for more than one time when pressed. To avoid that remove that hand from the key position as soon as you read it.
please dont forget to add the samples of sound to the project directory
 
VERY IMPORTANT: Some libraries does not work in the latest version. So downgrade it to the previous version.
