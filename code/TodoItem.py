from datetime import datetime

class TodoItem:
	def __init__(self, title, desc, start, end):
		self.title = title
		self.description = desc
		self.start = start
		self.end = end
		self.importance = 0

	def update(self, dt):
		self.importance = (dt - self.start) / (self.end - self.start)

	def view(self):
		print(self.title + " " + str(self.importance))