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

@dataclass
class Sub_Window:
	list: list
	title: str

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
	screen_width = window0.winfo_screenwidth()
	screen_height = window0.winfo_screenheight()
	window0.geometry(f"{screen_width}x{screen_height}")
	window0.title("Getting Things Done")
	return window0

def create_sub_window(window0: tk.Tk):
	"""Creates an empty sub_screen."""
	create_next_actions_window(window0, next_actions_list)

def ui_manager():
	"Manages UI. "
	window0= create_main_window()
	window1 = create_sub_window(window0)
	window0.mainloop()

def create_next_actions_window(window0: tk.Tk, next_actions_list: list[Actionable])->tk.Frame:
	"""Creates Next acions window"""
	screen_width = window0.winfo_screenwidth()
	screen_height = window0.winfo_screenheight()
	#Generate widgets and objects
	canvas0= tk.Canvas(window0, width=screen_width, height=screen_height, bg='black')
	sub_window= tk.Frame(master=canvas0, width = SUB_WINDOW_WIDTH, height = SUB_WINDOW_HEIGHT, background='blue' )
	top_frame = tk.Frame(sub_window, width=SUB_WINDOW_WIDTH, height=20, bg='black')
	title = tk.Label(top_frame, text="Next Actions", fg='white', bg='black')
	window_options_frame = tk.Frame(top_frame, bg='black')
	minimize_button = tk.Button(window_options_frame, fg='white', bg='black', text ='\u2013')
	maximize_button = tk.Button(window_options_frame, fg='white', bg='black', text='\u29E0')
	close_button = tk.Button(window_options_frame, fg='white', bg='black', text='X')
	canvas_window0_ID = canvas0.create_window(100,100, anchor=tk.NW, width=SUB_WINDOW_WIDTH, height=SUB_WINDOW_HEIGHT, window=sub_window)
	##Generate border frames
	border_frame_S = tk.Frame(master=sub_window, bg='grey', bd=2, borderwidth=2, class_="Border", height=3, width=SUB_WINDOW_WIDTH-6)
	border_frame_N = tk.Frame(master=sub_window, bg='grey', bd=2, borderwidth=2, class_="Border", height=3, width=SUB_WINDOW_WIDTH-6)
	border_frame_W = tk.Frame(master=sub_window, bg='grey', bd=2, borderwidth=2, class_="Border", height=SUB_WINDOW_HEIGHT-6, width=3)
	border_frame_E = tk.Frame(master=sub_window, bg='grey', bd=2, borderwidth=2, class_="Border", height=SUB_WINDOW_HEIGHT-6, width=3)
	corner_frame_NW = tk.Frame(master=sub_window, bg='green', bd=1, borderwidth=2, class_="Border", height=3, width=3)
	corner_frame_SW = tk.Frame(master=sub_window, bg='green', bd=1, borderwidth=2, class_="Border", height=3, width=3)
	corner_frame_NE = tk.Frame(master=sub_window, bg='green', bd=1, borderwidth=2, class_="Border", height=3, width=3)
	corner_frame_SE = tk.Frame(master=sub_window, bg='green', bd=1, borderwidth=2, class_="Border", height=3, width=3)
	#Force sub_window and top_frame to be of desired size, and not the size of the component widgets. 
	sub_window.grid_propagate(0)
	top_frame.grid_propagate(0)
	border_frame_S.grid_propagate(0)
	border_frame_W.grid_propagate(0)
	border_frame_E.grid_propagate(0)
	border_frame_N.grid_propagate(0)
	#Configure columns and rows
	sub_window.columnconfigure(0, weight=1)
	sub_window.columnconfigure(1, weight=1)
	sub_window.columnconfigure(2, weight=1)
	sub_window.rowconfigure(0, weight=1)
	sub_window.rowconfigure(1, weight=1)
	sub_window.rowconfigure(2, weight=1)
	sub_window.rowconfigure(3, weight=1)
	top_frame.columnconfigure(0, weight=1)
	top_frame.columnconfigure(1, weight=1)
	#Place widgets 
	canvas0.grid(column=0, row=0)
	top_frame.grid(column=1, row=1, sticky=tk.E + tk.W + tk.N )
	window_options_frame.grid(column=1, row=0, sticky='e')
	minimize_button.grid(column=1, row=0)
	maximize_button.grid(column=2, row=0)
	close_button.grid(column=3, row=0)
	title.grid(column=0, row=0, sticky='w')

	border_frame_S.grid(column=1, row=3)
	border_frame_W.grid(column=0, row=1, rowspan=2)
	border_frame_E.grid(column=2, row=1, rowspan=2)
	border_frame_N.grid(column=1, row=0)
#Event handling
	drag_activated = False
	button1_press_coords = (0, 0)
	#Widget-event-handler binds  
	top_frame.bind("<Button-1>", drag_activate)
	top_frame.bind("<ButtonRelease>", drag_deactivate)
	top_frame.bind("<Motion>", execute_drag)
	title.bind("<Button-1>", drag_activate)
	title.bind("<ButtonRelease>", drag_deactivate)
	title.bind("<Motion>", execute_drag)

def resize_sub_window():
	""""""
	def sub_window_resize_event_handling():
		"""Binds relevant widgets to relevant functions"""
	def horizontal_resize():
		"""Used in event handler"""
	def vertical_resize():
		"""Used in event handler"""
	def corner_resize ():
		"""Used in event handler"""

def update_mouse_pointer_graphic(event: tk.Event):
		"""Updates the mouse pointer graphic when the pointer hovers over certain widgets."""
		def resize_cursor(enter_event: tk.Event):
			"""Changes mouse pointer graphic to resize graphic. The specific resize graphic depends on the possible direction of resize. """
			W_frame_start: int
			W_frame_end: int
			E_frame_start: int
			E_frame_end: int
			N_frame_start: int
			N_frame_end: int
			S_frame_start: int
			S_frame_end: int
			if enter_event.x > W_frame_start and enter_event.x < W_frame_end:
				if enter_event.y > N_frame_start and enter_event.y < N_frame_end:
					"""Change cursor to 'top_left_corner'."""
				elif enter_event.y > S_frame_start and enter_event.y < S_frame_end:
					"""Change cursor to 'bottom_left_corner'."""
				"""Change cursor to 'left_side'."""
			elif enter_event.x > E_frame_start and enter_event.x < E_frame_end:
				if enter_event.y > N_frame_start and enter_event.y < N_frame_end:
					"""Change cursor to 'top_right_corner'."""
				elif enter_event.y > S_frame_start and enter_event.y < S_frame_end:
					"""Change cursor to 'bottom_right_corner'."""
				"""Change cursor to 'right_side'."""
			elif enter_event.y > N_frame_start and enter_event.y < N_frame_end:
				"""Change cursor to 'top_side'."""
			elif enter_event.y > S_frame_start and enter_event.y < S_frame_end:
				"""Change cursor to 'bottom_side."""
			enter_event.widget.bind('<Leave>', default_cursor)
			

		def default_cursor (leave_event: tk.Event):
			"""Change cursor graphic to the default graphic."""
			

			
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
def drag_activate(button1_press: tk.Event):
	""""Returns True when mouse button 1 is pressed in binded widget. """
	print("Button1 Pressed")
	global drag_activated
	global button1_press_coords
	drag_activated = True
	button1_press_coords = button1_press.x, button1_press.y

def drag_deactivate(button1_release: tk.Event):
	"""Returns False when mouse button 1 is released over the binded widget. """
	print("Button1 Released")
	global drag_activated
	drag_activated = False

def execute_drag(mouse_motion: tk.Event):
	"""Called when motion detected in binded frame, and drag_status == True."""
	def get_canvas_window_obj_ID():
		"""Gets the canvas window obj ID by using event.widget attribute, and the widget.master attribute, to refer to the canvas. 
		Determines whether the widget is the label widget (containing the title) or the top frame widget. If the former, the .master
		attribute is called one more time than for the latter. Returns the canvas widget and the canvas window object ID."""
		x_root = mouse_motion.x_root
		y_root = mouse_motion.y_root
		event_frame = mouse_motion.widget
		if event_frame.winfo_class() == 'Frame':
			sub_window = event_frame.master
			canvas = sub_window.master
			return canvas, canvas.find_closest(x_root,y_root)[0]
		elif event_frame.winfo_class() == 'Label':
			top_frame = event_frame.master
			sub_window = top_frame.master
			canvas = sub_window.master
			return canvas, canvas.find_closest(x_root,y_root)[0]

	global drag_activated
	global button1_press_coords
	#Initial position values of mouse pointer (relative widget (upper left coner of the widget))
	x1, y1 = button1_press_coords[0], button1_press_coords[1]
	if drag_activated:
		# Final position values of the mouse pointer (relative widget (upper left corner of the widget))
		x2 = mouse_motion.x
		y2 = mouse_motion.y
		# Calculates change in x and change in y from difference between initial and final position of mouse pointer. Initial position: (x1,y1), final position (x2, y2).
		delta_x = x2 - x1
		delta_y = y2 - y1
		x1 = x2
		y1 = y2
		#Update the position of the canvas window object using change in x and change in y of mouse pointer. 
		canvas, canvas_window_object_ID = get_canvas_window_obj_ID()
		canvas.move(canvas_window_object_ID, delta_x, delta_y)

		

#Global Constants:
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