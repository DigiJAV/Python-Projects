from dataclasses import dataclass
from tkinter import ttk
import tkinter as tk
import math

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

def save_data():
	"""Saves data in files."""

def load_data():
	"""Loads data in files."""

#UI Functions
def create_main_window():
	window0 = tk.Tk()
	window0.geometry(f"{SCREEN_WIDTH}x{SCREEN_LENGTH}")
	window0.title("Getting Things Done")

	return window0

def create_sub_window(window0: tk.Tk):
	"""Creates an empty sub_screen."""
	#Generate sub-window and  component widgets
	canvas0= tk.Canvas(window0, width=SCREEN_WIDTH, height=SCREEN_LENGTH, bg='black')
	
	sub_window= tk.Frame(master=canvas0, width = SUB_WINDOW_WIDTH, height = SUB_WINDOW_HEIGHT, background='blue', borderwidth=5, relief='groove')
	top_frame = tk.Frame(sub_window, width=SUB_WINDOW_WIDTH-10, height=20, bg='black')
	title = tk.Label(top_frame, text="Next Actions", fg='white', bg='black')
	window_options_frame = tk.Frame(top_frame, bg='black')
	minimize_button = tk.Button(window_options_frame, fg='white', bg='black', text ='\u2013')
	maximize_button = tk.Button(window_options_frame, fg='white', bg='black', text='\u29E0')
	close_button = tk.Button(window_options_frame, fg='white', bg='black', text='X')
	
	canvas_window0_ID = canvas0.create_window(100,100, anchor=tk.NW, width=SUB_WINDOW_WIDTH, height=SUB_WINDOW_HEIGHT, window=sub_window)
	
	
	
	#Force sub_window and top_frame to be of determined size, and not the size of the component widgets. 
	top_frame.grid_propagate(0)
	
	#Configure columns of top_frame widget
	top_frame.columnconfigure(0, weight=1)
	top_frame.columnconfigure(1, weight=1)

	#Place widgets 
	canvas0.grid(column=0, row=0)
	top_frame.grid(column=0, row=0)
	window_options_frame.grid(column=1, row=0, sticky='e')
	close_button.grid(column=3, row=0)
	minimize_button.grid(column=1, row=0)
	maximize_button.grid(column=2, row=0)
	title.grid(column=0, row=0, sticky='w')

	#Event handling
	drag_status = False

	#Widget event binds  
	top_frame.bind("<Button-1>", drag_activate)
	top_frame.bind("<ButtonRelease>", drag_deactivate)
	top_frame.bind("<Motion>", execute_drag)
	print(drag_status)
	
	return canvas0

def ui_manager():
	"Manages UI. "
	window0= create_main_window()
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
def drag_activate(mouse_button1_press: tk.Event)->bool:
	""""Returns True when mouse button 1 is pressed in binded widget. """
	print("Button1 Pressed")
	global drag_status 
	drag_status = True

def drag_deactivate(mouse_butto1_release: tk.Event)->bool:
	"""Returns False when mouse button 1 is released over the binded widget. """
	print("Button1 Released")
	global drag_status
	drag_status = False

def execute_drag(mouse_motion: tk.Event):
	"""Called when motion detected in binded frame, and drag_status == True.
	"""
	global drag_status
	if drag_status:
		print("Dragging")
		top_frame = mouse_motion.widget
		# X and Y coords of the mouse motion event relative to the frame widget 
		x_frame = mouse_motion.x
		y_frame = mouse_motion.y
		# X and Y coords of the mouse motin event relative the canvas root window
		x_root = mouse_motion.x_root 
		y_root = mouse_motion.y_root
		
		# Update position of the window object in the canvas using x and y position of mouse pointer relative to root screen. 
		sub_window_frame = top_frame.master
		canvas = sub_window_frame.master
		canvas_window_object_ID = canvas.find_closest(x_root,y_root)[0]
		x, y = canvas.coords(canvas_window_object_ID)
		print("Mouse (x_root,y_root): (",x_root,y_root,")")
		print("Canvas window old coords: ",x,",",y)
		canvas.move(canvas_window_object_ID, x_frame-x_frame*(8/10) , y_frame-y_frame*(8/10))
		print("Canvas window new coords: ",x,",",y)

#Global Constants:
SCREEN_WIDTH = 1800
SCREEN_LENGTH = 800
SUB_WINDOW_WIDTH = 300
SUB_WINDOW_HEIGHT = 300
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