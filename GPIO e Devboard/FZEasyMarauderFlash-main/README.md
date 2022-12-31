# Easy Flipper Zero Marauder Flash
This is for easily flashing Marauder on an ESP32 or WiFi Devboard for a Flipper Zero!
![Screenshot of EasyInstall](https://raw.githubusercontent.com/SkeletonMan03/FZEasyMarauderFlash/main/EasyInstall_Screenshot.png)

## Windows Users:
You have two prerequisites. 
You must install [Git for Windows from here](https://gitforwindows.org/).  
If you are flashing an ESP32 board, you need to install the [driver from here](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads) in order for your device to be recognized

## It is now simple to install or update Marauder on Linux, Mac OS X, or Windows.
# How to use: 
* Step 0 only has to be ran once
0) run `pip3 install -r requirements.txt`. 
1) Connect the devboard or ESP32 board via USB.
2) Press and hold the `BOOT` button on the module, press and release the `RESET` button.
3) Release the BOOT button. 
5) run `python3 EasyInstall.py`. 
6) Select the option of what you want to do

* Important note: You may need to run this script with `sudo` or as Administrator in Windows   

## This project is based on the Windows Marauder flasher batch script

You can find it [here in UberGuidoZ's repo](https://github.com/UberGuidoZ/Flipper/blob/main/Wifi_DevBoard/FZ_Marauder_Flasher)

## About this script
This script pulls all of its resources from the proper Github repositories in order to make sure you are up-to-date.  
The only dependencies it does not get by itself are the required Python modules and Windows tools.  
This script is now capable of flashing Marauder onto an ESP32-WROOM, ESP32-S2-WROVER, and some knock-off boards.  
This script should work on most devices that can run Python 3 and can access serial ports via USB.  

## Compatible boards
* Flipper Zero WiFi Devboard  
* ESP32-S2 (The ESP chip that is on the WiFi Devboard)  
* ESP32-S2-WROVER
* ESP32-WROOM  
* ESP32-S3

## How to connect an ESP32-WROOM,WROVER,etc to the Flipper Zero
ESP32 -> Flipper Zero  
TX0 -> RX  
RX0 -> TX  
GND -> GND  
3v3 -> 3v3  

## TODO:
* Code cleanup.  
* Add more chip compatibility.
* Fix Windows bug where files cannot be deleted in order to be updated
* Attempt to accommodate 3rd-party knock-off chips that are not from Espressif
