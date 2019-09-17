import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject,GLib

class ProgramView():

    def __init__(self):
        self.box = None
        self.__lstStore__ = None
        
    def create(self):

        self.builder = Gtk.Builder.new_from_file("./ui/gtk3/components/ProgramView.glade")
        self.box = self.builder.get_object("hBoxBrewProgramView")
        self.treeVBrewProgramTable = self.builder.get_object("treeVBrewProgramTable")
        
        self.__lstStore__ = Gtk.ListStore(str,str,str)
        
        self.treeVBrewProgramTable.set_model(self.__lstStore__)
        renderer = Gtk.CellRendererText()
        column1 = Gtk.TreeViewColumn("Name", renderer, text=0)
        column2 = Gtk.TreeViewColumn("Temperatur", renderer, text=1)
        column3 = Gtk.TreeViewColumn("Dauer", renderer, text=2)
        self.treeVBrewProgramTable.append_column(column1)
        self.treeVBrewProgramTable.append_column(column2)
        self.treeVBrewProgramTable.append_column(column3)



        return self.box

    def connectSignalHandlers(self, pHandlers):
        self.builder.connect_signals(pHandlers)   
    def setBrewprogramm(self, pBrewProgramm):
        for phase in pBrewProgramm.phases:
            self.__lstStore__.append([phase.getName(),str(phase.getTargetTemp()),str(phase.getDuration())])

    def update(self, pDatas):
        pass
