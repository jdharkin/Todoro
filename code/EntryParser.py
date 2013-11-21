# a class with some functions for extracting information from 
#   entry files
class EntryParser:
   # accepts a filename to parse
   # returns a TodoEntry
   def parse(filename):
      f = open(filename, 'r')
      text = f.read()
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
         pass

      print(text)
      print(strings)


EntryParser.parse('sample.do')