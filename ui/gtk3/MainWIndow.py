import gi
import threading
import time
from flowcontrol.Phase import Phase
from flowcontrol.BrewProgramExecuter import BrewProgramExcecuter
from flowcontrol.BrewProgram import BrewProgram
from ui.gtk3.BrewprogrammView import BrewProgrammView
from ui.gtk3.components.Footer import Footer
from ui.gtk3.components.ButtonControlBar import ButtonControlBar
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject,GLib
GObject.threads_init()

class MainWindow(Gtk.Window):

    def __init__(self):

        self.footer = Footer()
        self.buttonControlBar = ButtonControlBar()

        Gtk.Window.__init__(self, title="Brew-Control")
        self.mainVBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.topVBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.middleVBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 6)

        self.actionBar = Gtk.MenuBar()
        self.statusBar = Gtk.Statusbar()
        self.centerPanel = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
        self.statusBarGrid = Gtk.Grid()
        self.statusBarGrid.set_column_homogeneous(True)

        self.topVBox.pack_start(self.actionBar,True,True,0)
        self.middleVBox.pack_start(self.centerPanel,True,True,0)

        self.mainVBox.pack_start(self.buttonControlBar.create(), True, True, 0)
        self.mainVBox.pack_start(self.middleVBox, True, True, 0)

        self.mainVBox.pack_start(self.footer.create(), True, True, 0)
        self.add(self.mainVBox)
        #instances for the center-panel
        self.__lstStore__ = Gtk.ListStore(str)
        self.__treeView__ = Gtk.TreeView()
        
        self.__lstStore__.append(["Hallo"])
        self.__treeView__.set_model(self.__lstStore__)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Title", renderer, text=0)
        self.__treeView__.append_column(column)
        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        #self.centerPanel.pack2(self.__treeView__,False, False)
        self.brewProgrammView = BrewProgrammView()
        self.brewProgrammView.create()
        self.centerPanel.pack2(self.brewProgrammView,False, False)

        handlers = {"onToggled_btnStartPause" : self.on_button2_clicked}
        self.buttonControlBar.connectSignalHandlers(handlers)


        self.connect("destroy", Gtk.main_quit)
        self.ctr = None

    def set_controller(self, pController):
        self.ctr = pController
        retValues = self.ctr.initUi()
        self.footer.update(retValues)

    def initialize_ui(self,pBrewProgram):
        self.brewProgrammView.setBrewprogramm(pBrewProgram)

    def update_gui(self):
        while(True):
            #self.lblActTemp.set_text(str(self.ctr.getTimeDelta()))
            print(self.ctr.getActUiValues())

            GLib.idle_add(self.footer.update,
                          self.ctr.getActUiValues())
            time.sleep(0.1)
    def start(self):
        myThread = threading.Thread(target=self.update_gui)
        myThread.start()
        self.show_all()
        Gtk.main()
    def on_button1_clicked(self, widget):
        print(self.lblActTemp.get_xalign())

    def on_button2_clicked(self, widget):
        if self.ctr.getActBrewProgramState() == BrewProgramExcecuter.STARTED:
            self.ctr.pauseBrewProgram()
            widget.set_label("Start")
        else:
            self.ctr.startBrewProgram()
            widget.set_label("Pause")

