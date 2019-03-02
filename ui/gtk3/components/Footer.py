import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject,GLib

class Footer():

    def __init__(self):
        self.box = None
        self.lblTargetTempValue = None

    def create(self):

        builder = Gtk.Builder.new_from_file("./ui/gtk3/components/Footer.glade")
         
        self.box = builder.get_object("actPhaseView")
        self.lblTargetTempValue = builder.get_object("lblTargetTempValue")
        self.lblProgramNameValue= builder.get_object("lblProgramNameValue")
        self.lblTotalTimeValue= builder.get_object("lblTotalTimeValue")
        self.lblDurationValue= builder.get_object("lblDurationValue")
        self.lblPhaseName= builder.get_object("lblPhaseName")
        self.lblActTempValue= builder.get_object("lblActTempValue")
        self.lblElapsedTimeValue= builder.get_object("lblElapsedTimeValue")
        return self.box

    def update(self, pDatas):
        if (pDatas.get("programName") != None):
            self.lblProgramNameValue.set_text(pDatas.get("programName"))
        if (pDatas.get("phaseName") != None):
            self.lblPhaseName.set_text(pDatas.get("phaseName"))
        if (pDatas.get("duration") != None):
            self.lblDurationValue.set_text(str(pDatas.get("duration")))
        if (pDatas.get("totalTime") != None):
            self.lblTotalTimeValue.set_text(str(pDatas.get("totalTime")))
        if (pDatas.get("targetTemp") != None):
            self.lblTargetTempValue.set_text(str(pDatas.get("targetTemp")))
        if (pDatas.get("elapsedTime") != None):
            self.lblElapsedTimeValue.set_text(str(pDatas.get("elapsedTime")).split('.',2)[0])
        if (pDatas.get("actTemp") != None):
            self.lblActTempValue.set_text(str(pDatas.get("actTemp")))

