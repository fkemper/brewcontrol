import gi
from ui.gtk3.components.MainWindow import MainWindow
from devices.DeviceManager import DeviceManager
from devices.simulation.TempSensorSim import  TempSensor
from Controller import controller
from base.Config import Config
import threading
import json


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject,GLib
GObject.threads_init()

if (__name__ == "__main__"):
   
    #read the config-file and make it accesable "like" a singleton
    with open("brewcontrol.conf", "r") as conf_file:
        data = json.load(conf_file)
    confHolder = Config()
    confHolder.conf = data

    #cycTime = cycleTime()
    ctr = controller()
    #start gtk3 gui
    if (confHolder.conf["interface"]["gtk3"]["enable"]):
        myUi = MainWindow()
        myUi.setController(ctr)
        myThread = threading.Thread(target=myUi.start)
        myThread.start()#
    myDeviceManager = DeviceManager()
    myTempSensorSim = TempSensor()
    threading.Thread(target=ctr.start).start()

