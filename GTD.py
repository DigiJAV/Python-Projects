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
0

def save_data():
	"""Saves data in files."""

def load_data():
	"""Loads data in files."""

#UI Functions
def create_main_window():
	window0 = tk.Tk()
	window0.geometry(f"{SCREEN_WIDTH}x{SCREEN_LENGTH}")
	window0.title("Getting Things Done")
	window0.grid()
	return window0

def create_sub_window(window0: tk.Tk):
	"""Creates an empty sub_screen."""
	window1 = tk.Toplevel(window0,borderwidth=2, background='blue')

	sub_window_border = tk.Frame(window0, width = SUB_WINDOW_WIDTH, height = SUB_WINDOW_HEIGT, background='black', borderwidth=3)
	sub_window = tk.Frame(sub_window_border, width = SUB_WINDOW_WIDTH-6, height = SUB_WINDOW_HEIGT-6, background='blue')
	title_frame = tk.Frame(sub_window)
	title = tk.Label(title_frame, text="Next Actions", fg='white', bg='black', font=16)

	sub_window_border.grid_propagate(0)
	sub_window.grid_propagate(0)
	sub_window_border.grid(row=0, column=0)
	sub_window.grid(column=0, row=0)
	title_frame.grid(column=0, row=0)
	title.grid(column=0,row=0)

	title_frame.bind("<Button-1><Motion>", drag_window)
	

def ui_manager():
	"Manages UI. "
	window0 = create_main_window()
	window1 = create_sub_window(window0)
	window0.mainloop()



def create_next_actions_window(window0: tk.Tk, next_actions_list: list[Actionable])->tk.Frame:
	"""Creates Next acions window"""
	window = create_sub_window(window0)						#Create Next Actions parent window
	widget = tk.Listbox(master = window, cnf={} )			#Create the list widget in parent window
	for next_action in next_actions_list:					#Populate the list widget with next actions 
		widget.insert(0, next_action.next_action)
	return window

def add_address_bar():
	"""Creates address bar."""

def update_address_bar():
	"""Updates address bar."""

def add_back_forward_buttons():
	"""Creates backward and forward buttons. Used with address bar, and with calendar."""

def add_sort_button():
	""""""
def add_filter_button():
	""""""
def add_checkboxes():
	""""""

#Event Handlers
def drag_window(event):
	"""Event_handler for click and drag on title frame of a sub-window, leading to repositioning of sub-window according to position of mouse pointer."""



#Global Constants:
SCREEN_WIDTH = 1800
SCREEN_LENGTH = 800
SUB_WINDOW_WIDTH = 300
SUB_WINDOW_HEIGT = 300
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

ui_manager()