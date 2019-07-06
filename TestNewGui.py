import gi
from ui.gtk3.components.MainWindow import MainWindow
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject,GLib
GObject.threads_init()

if (__name__ == "__main__"):
    win = MainWindow()
    gtkWin = win.create()
    gtkWin.show_all()
    Gtk.main()

