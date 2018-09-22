import cherrypy
from restconnector.DTOJsonCreator import DTOJsonCreator
import json


class RestServer(object):

    __brewController = None

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
        cherrypy.quickstart(self, '/', 'app.conf')


