import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject,GLib, Gdk

class MonitoringView():

    def __init__(self):
        pass
    def create(self):

        builder = Gtk.Builder.new_from_file("./ui/gtk3/components/MonitoringView.glade")
        box = builder.get_object("hBoxMonitoringView")
        self.disherStateLbl = builder.get_object("lablDisherState")
        self.heatingStateLbl = builder.get_object("lablHeatingState")
        return box
        
    def update(self, pDatas):
        print("Monitoring View")
        #self.heatingStateIndicator.set_active(False)
        
        if (pDatas != None):
           print (pDatas[0])
           if (pDatas[0].get("actStateHeating")==True):
              self.heatingStateLbl.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse('green'));
              self.heatingStateLbl.set_text("on")
           else:
              print("Heizung soll eigebntlich aus sein")
              self.heatingStateLbl.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse('red'));         
              self.heatingStateLbl.set_text("off")
           if (pDatas[0].get("actStateDisher")==True):
              self.disherStateLbl.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse('green'));
              self.disherStateLbl.set_text("on")
           else:
              self.disherStateLbl.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse('red'));         
              self.disherStateLbl.set_text("off")
    def connectSignals(self,handler):
        pass
