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
        
        
        return box
        
    def add_stack(self, stack_item, stack_name):
        self.stack.add_named(stack_item,stack_name)


    def set_visible_stack(self, name):
        self.stack.set_visible_child_name(name)
