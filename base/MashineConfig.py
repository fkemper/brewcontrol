import os.path
import json

class MachineConfig:
    __shared_state = {}
    conf = None
    def __init__(self):
        if (self.conf == None):

            self.__dict__ = self.__shared_state
            with open("../machine.conf", "r") as conf_file:
                self.conf = json.load(conf_file)


