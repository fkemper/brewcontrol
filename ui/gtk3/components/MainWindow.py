import threading
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject,GLib


from ui.gtk3.components.Footer import Footer
from ui.gtk3.components.SideBar import SideBar
from ui.gtk3.components.WorkingStack import WorkingStack
from ui.gtk3.components.ProgramView import ProgramView

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
        self.programm_view = ProgramView()
        workingStack_programView = self.programm_view.create() 
        self.workingStack.add_stack(workingStack_programView,"Program")
        handlers_programview_actions = {"on_gtkBtnStart_clicked" : self.startBrewProgramAction, "on_gtkBtnStopp_clicked":self.stopBrewProgramAction, "on_gtkBtnPause_clicked":self.pauseBrewProgramAction}
        self.programm_view.connectSignalHandlers(handlers_programview_actions)            
        self.programm_view.setBrewprogramm(self.ctrl.getBrewProgram())
        return win

    def rowChanged(self,widget,path,column):
        print("Row changed...")
        model = widget.get_model()
        menu_entry = model[path][0]
        self.workingStack.set_visible_stack(menu_entry)
        
    def startBrewProgramAction(self, widget):
        self.ctrl.startBrewProgram()
    
    def stopBrewProgramAction(self, widget):
        self.ctrl.stopBrewProgram()
        
    def pauseBrewProgramAction(self, widget):
        self.ctrl.pauseBrewProgram()
            
    def setController(self, ctrl):
        self.ctrl = ctrl
        
    def update_gui(self):
        while(True):
            #print("UI-Update-Thread started...")
            #self.lblActTemp.set_text(str(self.ctr.getTimeDelta()))
            #print(self.ctr.getActUiValues())

            #GLib.idle_add(self.footer.update,
                          #self.ctr.getActUiValues())
            time.sleep(0.1)
    def start(self):
        myThread = threading.Thread(target=self.update_gui)
        myThread.start()
        win = self.create()
        win.show_all()
        Gtk.main()


