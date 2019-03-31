import os.path
import json

class Config:
    __shared_state = {}
    conf = None
    def __init__(self):
        if (self.conf == None):

            self.__dict__ = self.__shared_state
            with open("brewcontrol.conf", "r") as conf_file:
                self.conf = json.load(conf_file)

