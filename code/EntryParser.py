from TodoEntry import *

# a class with some functions for extracting information from 
#   entry files
class EntryParser:
   # accepts a filename to parse
   # returns a TodoEntry
   def parse(filename):
      f = open(filename, 'r')
      text = f.read()
      dictionary = EntryParser.extractBrackets(text)
      entry = TodoEntry()
      if 'title' in dictionary:
         entry.title = dictionary['title']
      if 'description' in dictionary:
         entry.desc = dictionary['description']
      if 'start' in dictionary:
         entry.setStartStr(dictionary['start'])
      if 'end' in dictionary:
         entry.setEndStr(dictionary['end'])

      print(entry)
      return entry



   # returns a dictionary of all [key:value]s in the text with whitespace
   # stripped
   def extractBrackets(text):
      recording = False
      strings = []
      inside = ''
      for c in text:
         #ignore any whitespace
         if recording:
            if c == ']':
               recording = False
               strings.append(inside)
               inside = ''
            else :
               # do whatever with valid characters here
               inside += c
         else:
            if c == '[':
               recording = True

      if recording:
         # no closing bracket
         print("No closing bracket.")
      return {}

      dictionary = {}
      for s in strings:
         sp = s.split(':')
         if len(sp) == 2:
            # valid key:value
            dictionary[sp[0].strip()] = sp[1].strip()
         else:
            #invalid
            pass

      return dictionary


EntryParser.parse('sample.do')