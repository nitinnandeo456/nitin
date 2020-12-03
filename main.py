import os
import subprocess
import time


def usb():
    print("Connect the phone via usb")
    time.sleep(3)
    strv = str(subprocess.check_output("lsusb"))
    # this is the 22d9 for my usb you can change it for your usb
    x = "22d9" in strv or "2a96" in strv
    if x:
        return True

    else:
        return False


def command():
    comm = ['adb shell input keyevent 3', 'adb shell input keyevent 5',
            'adb shell input keyevent 4', 'adb shell input keyevent 207', 'adb shell input keyevent 3', 'adb shell input keyevent 220', 'adb shell input keyevent 220', 'adb shell input keyevent 26']
    for i in range(0, len(comm)):
        time.sleep(0.7)
        os.system(comm[i])


choise = int(input("Want To run script via usb or wirelessly ? 1 for usb "))
if(choise == 1):
    y = usb()
    if y:
        print("Device Connected Succesfully")
        command()

    else:
        print("Device Not Found")
else:
    print("You Choose wireless connection Firstly you need to connect the USB")
    print("And Turn On THe Developer Option This Script wait for 5 Seconds")
    time.sleep(5)
    z = usb()
    cmd2 = "adb tcpip 5555"
    os.system(cmd2)
    time.sleep(2)
    print("You Can Disconnect the USB")
    ip = input("Enter The IP Address of Your Phone ")
    cmd3 = "adb connect " + ip
    oo = os.system(cmd3)
    command()
    cmd4 = "adb kill-server"
    os.system(cmd4)
