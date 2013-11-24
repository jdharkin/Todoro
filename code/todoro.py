#!/usr/bin/env python3.3
import sys
from TodoList import *

def STUB():
   print("Not implemented.")


prog_name = None

for argix in range(len(sys.argv)):
   if argix == 0:
      prog_name = sys.argv[argix]

   if argix == 1:
      if sys.argv[argix] == 'add':
         STUB()

      if sys.argv[argix] == 'all':
         todoList = TodoList()
         todoList.load()
         todoList.sort()
         print(todoList)

      if sys.argv[argix] == 'what':
         todoList = TodoList()
         todoList.load()
         todoList.sort()
         print(todoList.getEntry(0))

      if sys.argv[argix] == 'finish':
         STUB()

      if sys.argv[argix] == 'help':
         STUB()

      if sys.argv[argix] == 'setup':
         STUB()

