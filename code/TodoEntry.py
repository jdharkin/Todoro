from datetime import *
import re

# yr-month-day hour:min:sec
# 2013-05-19 19:50:23
FORMAT_FULL = '%Y-%m-%d %H:%M:%S'
FORMAT_HALF = '%Y-%m-%d'
REGEX_FULL = re.compile('\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d')
REGEX_HALF = re.compile('\d\d\d\d-\d\d-\d\d')

# TodoItem 
# the internal representation of a todo list 
class TodoEntry:
   # title - string - title of the entry
   # desc - string - desctiption of the entry
   # start - datetime - start datetime
   # end - datetime - end datetime
   def __init__(self, title=None, desc=None, start=None, end=None):
      self.title = title
      self.desc = desc
      self.start = start
      self.end = end
      self.importance = 0.0

   def __str__(self):
      return self.title + " : %3.f%%" % (self.getImportance() * 100)\
         + '\n   ' + self.start.__str__() + ' => ' + self.end.__str__()\
         + '\n   ' + self.desc 

   # sets self.start using a string
   def setStartStr(self, string):
      if REGEX_FULL.match(string):
         self.start = datetime.strptime(string, FORMAT_FULL)
      elif REGEX_HALF.match(string):
         self.start = datetime.strptime(string, FORMAT_HALF)
      else:
         #invalid string
         pass
         #print("'%s' is not a valid datetime." % (string))

   def setEndStr(self, string):
      if REGEX_FULL.match(string):
         self.end = datetime.strptime(string, FORMAT_FULL)
      elif REGEX_HALF.match(string):
         self.end = datetime.strptime(string, FORMAT_HALF)
      else:
         #invalid string
         pass
         #print("'%s' is not a valid datetime." % (string))

   def getImportance(self):
      if (self.start and self.end):
         self.importance = (datetime.today()-self.start)/(self.end-self.start)
      else:
         self.importance = 0.0
      return self.importance