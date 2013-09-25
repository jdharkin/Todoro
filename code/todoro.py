from TodoItem import *
from TodoList import *
from datetime import *

todoList = TodoList()

quit = False

todoList.addItem(TodoItem("Trash", "Take it out.", datetime(2013, 9, 17), datetime(2013, 9, 19)))

todoList.addItem(TodoItem("Groceries", "Go to Safeway.", datetime(2013, 9, 17), datetime(2013, 9, 20)))

while True :
	args = input("->").split()

	# VIEW
	if args[0] == "view" :
		if len(args) > 1 :
			print("Too many arguments after '" + args[0] + "'")
		else :
			todoList.view()

	# ADD
	elif args[0] == "add" :
		if len(args) > 1 :
			print("Too many arguments after '" + args[0] + "'")
		else :
			todoList.addItem(TodoItem(input("Title: "), input("Description: "), datetime.today(),
				datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))))

	# UPDATE
	elif args[0] == "update" :
		if len(args) > 1 :
			print("Too many arguments after '" + args[0] + "'")
		else :
			todoList.update()

	# EXIT
	elif args[0] == "exit" :
		if len(args) > 1 :
			print("Too many arguments after '" + args[0] + "'")
		else :
			exit()

	# EDIT
	elif args[0] == "edit" :
		if len(args) != 2 :
			print("'edit' requires one argument")
		else :
			print( "Edit: " + todoList.list[int(args[1])].title)
