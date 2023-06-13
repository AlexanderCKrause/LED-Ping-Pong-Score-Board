#!/bin/bash

# Define the directory paths
FLICD_DIR="/home/pi/pongv2/fliclib-linux-hci/bin/armv6l"
PONGV2_DIR="/home/pi/pongv2"

# Define the commands to start the services
STOP_DEFAULT_BLUETOOTH="sudo service bluetooth stop"
FLICD_START_CMD="sudo ./flicd -f sqlite_db_file.db"
API_START_CMD="python3 server.py"
MATRIX_START_CMD="sudo python3 $PONGV2_DIR/matrix.py --led-cols=64 --led-pixel-mapper=Rotate:90"
FLIC_HANDLER_START_CMD="python3 flic_handler.py"

# Define the commands to stop the services
FLICD_STOP_CMD="pkill -f flicd"
API_STOP_CMD="pkill -f server.py"
MATRIX_STOP_CMD="pkill -f matrix.py"
FLIC_HANDLER_STOP_CMD="pkill -f flic_handler.py"

# Function to start the services
start_services() {

    $STOP_DEFAULT_BLUETOOTH # Stop Default Bluetooth Daemon
    sleep 2 # Wait for 2 seconds

    cd $FLICD_DIR
    $FLICD_START_CMD &
    sleep 2 # Wait for 2 seconds

    cd $PONGV2_DIR
    source env/bin/activate
    $API_START_CMD &
    sleep 10 # Wait for 10 seconds

    $FLIC_HANDLER_START_CMD &
    sleep 2 # Wait for 2 seconds

    $MATRIX_START_CMD &

}

# Function to stop the services
stop_services() {
    $FLIC_HANDLER_STOP_CMD
    sleep 2 # Wait for 2 seconds

    $MATRIX_STOP_CMD
    sleep 2 # Wait for 2 seconds

    $API_STOP_CMD
    sleep 2 # Wait for 2 seconds

    $FLICD_STOP_CMD
}

# Check the first argument to the script
if [ "$1" = "start" ]; then
    start_services
elif [ "$1" = "stop" ]; then
    stop_services
else
    echo "Usage: $0 {start|stop}"
fi
