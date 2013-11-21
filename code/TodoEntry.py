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

   def __str__(self):
      return 'todo: ' + self.title + ': ' + self.desc

