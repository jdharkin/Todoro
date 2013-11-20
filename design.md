# todoro #

Each todo list entry is represented as in individual file.
Top level of the todoro folder has unfinished entries and folders for finished and finished repeating items.

todo/
	(active todo items)
	repeat/
		(repeating todo items)
	done/
		(finished todo items)
	


Commands:

add [filename]
	creates a new file with the given name and adds an entry template to the file

what
	tells you what to do

finish [filename]
	moves an entry file to the completed or completed repeating folder

help
	prints a description of todoro commands

setup
	sets up a new todo list folder in the current directory



entry format:

    [title: title text]
    [description: description text]
    [start: datetime]
    [end: datetime]
    
repeating entry format:

    [title: title text]
    [description: description text]
    [repeat: frequency] // can be ‘daily’ ‘weekly’ ‘monthly’ ‘yearly’ or ‘x days’ ‘x weeks’ ‘x months’ ‘x years’
    // one of:
    [start: datetime] // necessary for ‘x somethings’ frequencies
    [start: weekday] // useful for ‘weekly’ frequency
    [start: month day] // useful for ‘monthly’ frequency
    
    [end: timedelta] // not a date, but an increment of time
