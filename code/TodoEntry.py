# TodoItem 
# the internal representation of a todo list 
class TodoItem:
   # title - string - title of the entry
   # desc - string - desctiption of the entry
   # start - datetime - start datetime
   # end - datetime - end datetime
   def __init__(self, title, desc, start, end):
      self.title = title
      self.desc = desc
      self.start = start
      self.end = end

