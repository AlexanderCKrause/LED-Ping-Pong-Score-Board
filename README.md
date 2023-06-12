# LED-Ping-Pong-Score-Board
This project uses Flic Buttons and a Raspberry Pi LED Matrix to create a Ping Pong Score Board

## Overview
There is a Flask web app that is in charge of the Ping Pong game iteself. This app has API endpoints tracking the game score, and sharing it with other scripts. There is also a flic_handler.py script that detects Flic button presses (Single, Double, Hold) to determine how to update the score. It sends POST requests to the API when update events occur.

A single press increments the score, a double press decrements the score, and a button hold resets the score to 0.

The matrix.py script displays the scores on an LED Matrix, and queries the API to get the current score.

### Web API APP
The Web API is used in order to open the score information up to other devices, and to allow for game settings to be configured through a local web app interface in the future.

## How to Start
To start/stop the necessary scripts run the bash script ./board.sh start OR Run ./board.sh stop
Run this via the crontab on @reboot to start all necessary scripts at once on state up.

Note: You will need to sync your buttons by running the new_scan_wizard.py file within the fliclib-linux-hci directory once the device has booted. This should only need to happen once, and then the flic library will save the button information.
