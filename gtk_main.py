import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
import fuelcalc

class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Aviation Tools")
		self.set_size_request(500, 300)

		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(vbox)

		self.label = Gtk.Label()
		self.label.set_text("What is the fuel consumption (gph)?")
		vbox.pack_start(self.label, True, True, 0)

		self.entry = Gtk.Entry()
		self.entry.get_text()
		self.entry.connect("activate", self.on_click)
		vbox.pack_start(self.entry, False, True, 6)

		self.label2 = Gtk.Label()
		self.label2.set_text("What is the distance (nm)?")
		vbox.pack_start(self.label2, True, True, 0)

		self.entry2 = Gtk.Entry()
		self.entry2.get_text()
		self.entry2.connect("activate", self.on_click)
		vbox.pack_start(self.entry2, False, True, 6)

		self.label3 = Gtk.Label()
		self.label3.set_text("What is your average speed?")
		vbox.pack_start(self.label3, True, True, 0)

		self.entry3 = Gtk.Entry()
		self.entry3.get_text()
		self.entry3.connect("activate", self.on_click)
		vbox.pack_start(self.entry3, False, True, 6)

		button = Gtk.Button.new_with_label("Calculate!")
		button.connect("clicked", self.on_click)
		vbox.pack_start(button, True, True, 0)

	def on_click(self, button):
		first_entry = self.entry.get_text()
		second_entry = self.entry2.get_text()
		third_entry = self.entry3.get_text()

		result = fuelcalc.fuel_calc(first_entry, second_entry, third_entry)
		print(result)

		dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "This is the result")
		dialog.format_secondary_text(result)
		dialog.run()
		print("INFO dialog closed")
		dialog.destroy()

win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
