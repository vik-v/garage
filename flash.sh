sudo chmod a+rw /dev/ttyUSB0
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 ./esp32-20220618-v1.19.1.bin

