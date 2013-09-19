class TodoItem:
	def __init__(self, title, desc, start, end):
		self.title = title
		self.description = desc
		self.start = start
		self.end = end
		self.importance = 0

	def update(self, datetime):
		self.importance += 1

	def view(self):
		print(self.title)