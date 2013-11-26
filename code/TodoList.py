import os
import re
from TodoEntry import *
import FileStuff

ENTRY_REGEX = re.compile('.+\.do')

class TodoList:
   def __init__(self):
      self.list = []

   def __str__(self):
      toReturn = ''
      for i in range(len(self.list)):
         entry = self.list[i]
         if i == 0:
            toReturn += entry.__str__()
         else:
            toReturn += '\n' + entry.__str__()
      return toReturn

   def __iter__(self):
      for entry in self.list:
         yield entry

   def addEntry(self, entry):
      self.list.append(entry)

   def addEntryFilename(self, filename):
      self.list.append(FileStuff.parseEntryFile(filename))

   def sort(self):
      self.list.sort(key = lambda entry: -entry.getImportance())

   def sorted(self):
      return self.list.sorted(key = lambda entry: -entry.getImportance())

   def load(self, path = '.'):
      for filename in os.listdir(path):
         if ENTRY_REGEX.match(filename):
            self.addEntryFilename(filename)

   def getEntry(self, index):
      if len(self.list) >= index + 1:
         return self.list[index]
      else:
         return None