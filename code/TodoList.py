from datetime import datetime
import xml.etree.ElementTree as ET

class TodoList:
	def __init__(self):
		self.list = []

	def addItem(self, todoItem):
		''' Add an item to this todo list '''
		self.list.append(todoItem)

	def update(self):
		''' Update the importance level of items in the list and sort it '''
		for item in self.list :
			item.update(datetime.today())
		self.sort()

	def importList(self, xmlFileName):
		''' Add items to the list from an xml file'''
		xmlTree = ET.parse(xmlFileName)
		xmlRoot = xmlTree.getroot()
		for item in xmlRoot:
			title = ''
			description = ''
			start, end = '0000-00-00 00:00:00'
			for data in item:
				if data.tag == 'title': title = data.text
				if data.tag == 'description': description = data.text
				if data.tag == 'start': start = data.text
				if data.tag == 'end': end = data.text
			# add the item to the list

	def sort(self):
		''' Sort this list based on importance '''
		self.list.sort(key = lambda l: -l.importance)

	def view(self):
		''' Print valuable information from each item in the list '''
		for item in self.list:
			num = self.list.index(item)
			print(str(num) + ' ' + item.title + ' ') # + str(item.importance))
			print('\t' + item.description)