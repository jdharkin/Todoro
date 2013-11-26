#!/usr/bin/env python3.3
import sys
from TodoList import *

def STUB():
   print("not implemented.")

def template(filename):
   f = open(filename)
   f.write(TEMPLATE)
   f.close


prog_name = None

TEMPLATE = '''[title: ]
[start: ]
[end: ]
[description: ]
'''

if len(sys.argv) >= 0 + 1:
   prog_name = sys.argv[0]

if len(sys.argv) >= 1 + 1:
   if sys.argv[1] == 'add':
      if len(sys.argv) >= 2 + 1:
         for filename in sys.argv[2:]:
            f = open(filename, 'w')
            f.write(TEMPLATE)
            f.close
      else:
         print('no arguments given for add.')

   if sys.argv[1] == 'all':
      todoList = TodoList()
      todoList.load()
      todoList.sort()
      print(todoList)

   if sys.argv[1] == 'what':
      todoList = TodoList()
      todoList.load()
      todoList.sort()
      if todoList.getEntry(0):
         print(todoList.getEntry(0))
      else:
         print('nothing to do.')

   if sys.argv[1] == 'finish':
      STUB()

   if sys.argv[1] == 'help':
      STUB()

   if sys.argv[1] == 'setup':
      STUB()
      
