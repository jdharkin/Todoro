from TodoItem import *
from TodoList import *
from datetime import *

todoList = TodoList()

quit = False

todoList.addItem(TodoItem("Trash", "Take it out.", datetime(2013, 9, 17), datetime(2013, 9, 19)))

todoList.addItem(TodoItem("Groceries", "Go to Safeway.", datetime(2013, 9, 17), datetime(2013, 9, 20)))

while(not quit) :
	command = input("->")

	if command == "view":
		todoList.view()
	if command == "add":
		todoList.addItem(TodoItem(input("Title: "), input("Description: "), datetime.today(),
			datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))))
	if command == "update":
		todoList.update()
	if command == "exit":
		exit()