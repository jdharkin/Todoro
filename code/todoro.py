from TodoItem import *
from TodoList import *

todoList = TodoList()

quit = False

while(not quit) :
	command = input("->")
	if command == "view":
		todoList.view()
	if command == "add":
		todoList.addItem(TodoItem(input("Title: "), input("Description: "), 0, 0))
	if command == "update":
		todoList.update()
	if command == "exit":
		exit()