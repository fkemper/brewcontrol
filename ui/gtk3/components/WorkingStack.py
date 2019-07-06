import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject,GLib

class WorkingStack():

    def __init__(self):
        pass
    def create(self):

        builder = Gtk.Builder.new_from_file("./ui/gtk3/components/WorkingStack.glade")

        box = builder.get_object("hBoxStack")
        self.stack = builder.get_object("stackWorkingStack")
        hBoxBrewProgramView = builder.get_object("hBoxBrewProgramView")
        hBoxMonitoringView = builder.get_object("hBoxMonitoringView")
        self.stack.add_named(hBoxBrewProgramView,"Program")
        self.stack.add_named(hBoxMonitoringView,"Monitoring")
        self.stack.set_visible_child(hBoxMonitoringView)

        return box

    def set_visible_stack(self, name):
        self.stack.set_visible_child_name(name)
