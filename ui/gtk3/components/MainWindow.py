import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject,GLib

from ui.gtk3.components.Footer import Footer
from ui.gtk3.components.SideBar import SideBar
from ui.gtk3.components.WorkingStack import WorkingStack

class MainWindow():

    def __init__(self):
        pass
    def create(self):

        builder = Gtk.Builder.new_from_file("./ui/gtk3/components/MainWindow.glade")
        sidebar = SideBar()
        PanedBox = builder.get_object("PanedBox")
        PanedBox.add1(sidebar.create())
        self.workingStack = WorkingStack()
        PanedBox.add2(self.workingStack.create())
        footer = Footer()
        hBoxFooter = builder.get_object("hBoxFooter")
        hBoxFooter.pack_start(footer.create(),True,True,0 )
        win = builder.get_object("MainWindow")
        win.connect("delete-event", Gtk.main_quit)
        sidebar.connectSignals(self.rowChanged)
        return win

    def rowChanged(self,widget,path,column):
        print("Row changed...")
        model = widget.get_model()
        menu_entry = model[path][0]
        self.workingStack.set_visible_stack(menu_entry)
