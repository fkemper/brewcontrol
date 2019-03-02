import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject,GLib

class ButtonControlBar():

    def __init__(self):
        self.box = None
        self.builder = None
    def create(self):

        self.builder = Gtk.Builder.new_from_file("./ui/gtk3/components/ButtonControlBar.glade")
         
        self.box = self.builder.get_object("boxButtonBar")
        return self.box
    
    def connectSignalHandlers(self, pHandlers):
        self.builder.connect_signals(pHandlers)
        
    def update(self, pDatas):
        pass
