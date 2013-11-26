from TodoEntry import *

TEMPLATE = '''[title: ]
[start: ]
[end: ]
[description: ]
'''

ENTRY_REGEX = re.compile('.+\.do')

def makeTemplate(filename):
   #check for a valid .do filename
   if (ENTRY_REGEX.match(filename)):
      #open, write, close
      f = open(filename, 'w')
      f.write(TEMPLATE)
      f.close
   else:
      # not a valid .do file
      pass

# accepts a filename to parse
# returns a TodoEntry
def parseEntryFile(filename):
   f = open(filename, 'r')
   text = f.read()
   dictionary = extractBrackets(text)
   entry = TodoEntry()
   if 'title' in dictionary:
      if dictionary['title']:
         entry.title = dictionary['title']
      else:
         entry.title = 'no title'
   if 'description' in dictionary:
      entry.desc = dictionary['description']
   if 'start' in dictionary:
      entry.setStartStr(dictionary['start'])
   if 'end' in dictionary:
      entry.setEndStr(dictionary['end'])
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