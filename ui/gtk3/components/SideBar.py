import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject,GLib

class SideBar():

    def __init__(self):
        pass
    def create(self):

        builder = Gtk.Builder.new_from_file("./ui/gtk3/components/SideBar.glade")
        self.treeView = builder.get_object("treeView")
        box = builder.get_object("hBoxSideBar")
        treeStore = Gtk.TreeStore(GObject.TYPE_STRING)
        mainRow = treeStore.append(None,['BrewControl'])
        secondRow = treeStore.append(mainRow,['Program'])
        thirdRow = treeStore.append(mainRow,['Monitoring'])
        self.treeView.set_model(treeStore)
        rendererText = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn(None, rendererText, text = 0)
        self.treeView.append_column(column)
        self.treeView.expand_all()
        return box

    def connectSignals(self,handler):
        self.treeView.connect("row_activated",handler)

