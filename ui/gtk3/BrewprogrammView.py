import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject,GLib

class BrewProgrammView(Gtk.HBox):

    __lstStore__ = None
    __treeView__ = None

    def create(self):
        self.__lstStore__ = Gtk.ListStore(str,str,str)
        self.__treeView__ = Gtk.TreeView()
        
        self.__treeView__.set_model(self.__lstStore__)
        renderer = Gtk.CellRendererText()
        column1 = Gtk.TreeViewColumn("Name", renderer, text=0)
        column2 = Gtk.TreeViewColumn("Temperatur", renderer, text=1)
        column3 = Gtk.TreeViewColumn("Dauer", renderer, text=2)
        self.__treeView__.append_column(column1)
        self.__treeView__.append_column(column2)
        self.__treeView__.append_column(column3)
        self.pack_start(self.__treeView__,True,True,0)
        self.add(self.__treeView__)

    def setBrewprogramm(self, pBrewProgramm):
        for phase in pBrewProgramm.phases:
            self.__lstStore__.append([phase.getName(),str(phase.getTargetTemp()),str(phase.getDuration())])

