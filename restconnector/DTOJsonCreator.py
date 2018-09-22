import json
from flowcontrol.Phase import Phase

class DTOJsonCreator(json.JSONEncoder):

    def default(self, obj):

        if isinstance(obj, Phase):
            return {"Name":obj.getName(),"Duration":str(obj.getDuration()),"Ziel-Temperatur":str(obj.getTargetTemp())+"°C","Notification":obj.getNotificationFlag()}

        return json.JSONEncoder.default(self, obj)