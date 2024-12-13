#!/usr/bin/env python3
import gi
import os 
#
# GTK Red Shift
# ==============================
# Python version - requires PyGtk3 and Python 3
#
# ItsT3K, 2024
# https://github.com/itst3k/
#
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class RedShiftWin(Gtk.Window):

    def __init__(self):
        super().__init__(title="gtkRedShift")
        self.set_border_width(2)
        hbox = Gtk.Box(spacing=2)
        self.add(hbox)
        # 3000K Button
        button = Gtk.Button.new_with_label("3000K")
        button.connect("clicked", self.bt3000_click)
        hbox.pack_start(button, True, True, 0)
        # 3600K Button
        button = Gtk.Button.new_with_mnemonic("3600K")
        button.connect("clicked", self.bt3600_click)
        hbox.pack_start(button, True, True, 0)
        # 4000K Button
        button = Gtk.Button.new_with_mnemonic("4000K")
        button.connect("clicked", self.bt4000_click)
        hbox.pack_start(button, True, True, 0)
        # 4600K Button
        button = Gtk.Button.new_with_mnemonic("4600K")
        button.connect("clicked", self.bt4600_click)
        hbox.pack_start(button, True, True, 0)
        # 5600K Button
        button = Gtk.Button.new_with_mnemonic("5600K")
        button.connect("clicked", self.bt5600_click)
        hbox.pack_start(button, True, True, 0)
        # 6400K Button
        button = Gtk.Button.new_with_mnemonic("6400K")
        button.connect("clicked", self.bt6400_click)
        hbox.pack_start(button, True, True, 0)
# this part contains the secret sauce to getting the stuff to actually function
    def bt3000_click(self, button):
        os.system('qredshift -t 3000')
    def bt3600_click(self, button):
        os.system('qredshift -t 3600')
    def bt4000_click(self, button):
        os.system('qredshift -t 4000')
    def bt4600_click(self, button):
        os.system('qredshift -t 4600')
    def bt5600_click(self, button):
        os.system('qredshift -t 5600')
    def bt6400_click(self, button):
        os.system('qredshift -t 6400')

win = RedShiftWin()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
