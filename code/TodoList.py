from datetime import datetime

class TodoList:
	def __init__(self):
		self.list = []

	def addItem(self, todoItem):
		self.list.append(todoItem)

	def update(self):
		for item in self.list :
			item.update(datetime.today())
		self.sort()

	def importList(self, xmlFile) :
		pass # figure this out

	def sort(self):
		self.list.sort(key = lambda l: -l.importance)

	def view(self):
		for item in self.list:
			item.view()