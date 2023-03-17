import sublime
import sublime_plugin

class MessageInputHandler(sublime_plugin.TextInputHandler):
	def initial_text(self):
		return "Hello, world!"

	def next_input(self, args):
		if 'position' not in args:
			return PositionInputHandler()

class PositionInputHandler(sublime_plugin.ListInputHandler):
	def list_items(self):
		return [
			('Top of the file', 0),
			('Bottom of the file', -1)
		]

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit, message, position):
		if position < 0:
			position = self.view.size()

		self.view.insert(edit,position,message)

	def input(self, args):
		if 'message' not in args:
			return MessageInputHandler()
		elif 'position' not in args:
			return PositionInputHandler()
	def input_description(self):
		return 'Insert'

#class TestInput(sublime_plugin.CommandInputHandler):
#	def name(self):
#		return "Blake"
