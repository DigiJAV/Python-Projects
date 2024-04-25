from dataclasses import dataclass
from tkinter import ttk
import tkinter as tk


@dataclass
class Inbox:
    text_input: str
	#file_input: ?

@dataclass
class Date:
	year: int
	month: int
	day:	int
	time: 	int

@dataclass
class Actionable:
	date_of_creation: Date 
	deadline: Date
	completed: bool
	inbox_data: Inbox
	next_action: str
	waiting_for: str
	context: str 

@dataclass
class Not_Actionable:
	date_of_creation: Date
	inbox_data: Inbox
	review: Date 
	
@dataclass
class Project: 
	name: str
	vision: str
	outcome: str
	next_actions_list: list[Actionable]
	review: Date
	date_of_creation: Date
	completed: bool

#Data functions
def add_input():
	"""Receives input from UI. Creates instance of Inbox. Appends istance to inbox_list."""

def process_inbox():
	"""Receives input from UI. Creates instance of Actionable or Non_Actionable. Appends instance to a list. Calls the following functions:
        create_actionable
        create_non_actionable
		create_project  """

def create_actionable():
	"""Recieves input from UI. Creates instance of Actionable. Appends instance to a list."""

def create_non_actionable():
	"""Recevies input from UI. Creates instance of Non_Actionable. Appends instance to a list."""

def create_project():
	"""Receives input from UI. Creates instance of Project. Appends instance to project_list."""

def list_sort():
	"""Recevies input from UI and list. UI interaction determines list and filter option."""

def list_filter():
	"""Receives input from UI and list. UI interaction determines list and filter option."""

def ui_manager():
    """Tkinter mainloop located here."""
    screen0 = tk.Tk()
	screen0.geometry('500x500')
	screen0.title("GTD")
    screen0.mainloop()
    
#UI Functions



#Lists 
inbox_list = []
next_actions_list = []
projects_list = []
calendar_list = []
waiting_for_list = []
reference_list = []
someday_list =[]
tickler_list =[]
trash_list = []

completed_actions_list = []
completed_projects_list = []
achieved_outcomes_list = []

topics_list = []

filter_options = []
sort_options = []

