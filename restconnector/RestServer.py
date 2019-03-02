import cherrypy
from restconnector.DTOJsonCreator import DTOJsonCreator
from base.Config import Config
import json


class RestServer(object):

    __brewController = None
    __confHolder = None

    def __init__(self):
        self.confHolder = Config()

    def setBrewController(self,bctr):
        self.__brewController = bctr

    def index(self):
        return "Hello World!"
    index.exposed = True

    def get_phases(self):
        phases = self.__brewController.get_actual_phases_list()
        json_string = "["
        for phase in phases:
            json_string = json_string + json.dumps(phase, cls=DTOJsonCreator)
        json_string = json_string + "]"
        return json_string
    get_phases.exposed = True

    def start_server(self):
        cherrypy.config.update({'server.socket_host':
                                self.confHolder.conf["interface"]["web_interface"]["host"],'server.socket_port':self.confHolder.conf["interface"]["web_interface"]["port"]})
        cherrypy.quickstart(self, '/') 


