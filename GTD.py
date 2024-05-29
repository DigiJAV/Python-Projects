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
	top_frame = tk.Frame(sub_window, width=SUB_WINDOW_WIDTH, height=20, bg='black', relief='raised', bd=2)
	title = tk.Label(top_frame, text="Next Actions", fg='white', bg='black')
	window_options_frame = tk.Frame(top_frame, bg='black')
	minimize_button = tk.Button(window_options_frame, fg='white', bg='black', text ='\u2013')
	maximize_button = tk.Button(window_options_frame, fg='white', bg='black', text='\u29E0')
	close_button = tk.Button(window_options_frame, fg='white', bg='black', text='X')
	canvas_window0_ID = canvas0.create_window(100,100, anchor=tk.NW, window=sub_window)
	##Generate border frames
	border_frame_S = tk.Frame(master=sub_window, bg='grey', height=2, width=SUB_WINDOW_WIDTH-4, cursor='bottom_side', relief='raised')
	border_frame_N = tk.Frame(master=sub_window, bg='grey', height=2, width=SUB_WINDOW_WIDTH-4, cursor='top_side', relief='raised')
	border_frame_W = tk.Frame(master=sub_window, bg='grey', height=SUB_WINDOW_HEIGHT-4, width=2, cursor='left_side', relief='raised')
	border_frame_E = tk.Frame(master=sub_window, bg='grey', height=SUB_WINDOW_HEIGHT-4, width=2, cursor='right_side', relief='raised')
	corner_frame_NW = tk.Frame(master=sub_window, bg='grey', bd=1, borderwidth=2, height=2, width=2, cursor='top_left_corner', relief='raised')
	corner_frame_SW = tk.Frame(master=sub_window, bg='grey', bd=1, borderwidth=2, height=2, width=2, cursor='bottom_left_corner', relief='raised')
	corner_frame_NE = tk.Frame(master=sub_window, bg='grey', bd=1, borderwidth=2, height=2, width=2, cursor='top_right_corner', relief='raised')
	corner_frame_SE = tk.Frame(master=sub_window, bg='grey', bd=1, borderwidth=2, height=2, width=2, cursor='bottom_right_corner', relief='raised')
	#Force sub_window to be of desired size, and not the size of the component widgets. 
	sub_window.grid_propagate(0)
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
	top_frame.grid(column=1, row=1, sticky='new')
	window_options_frame.grid(column=1, row=0, sticky='e')
	minimize_button.grid(column=1, row=0)
	maximize_button.grid(column=2, row=0)
	close_button.grid(column=3, row=0)
	title.grid(column=0, row=0, sticky='w')
	#Place border frames
	border_frame_S.grid(column=1, row=3, sticky='wes')
	border_frame_W.grid(column=0, row=1, rowspan=2, sticky='ns')
	border_frame_E.grid(column=2, row=1, rowspan=2, sticky='nse')
	border_frame_N.grid(column=1, row=0, sticky='we')
	corner_frame_NE.grid(column=2, row=0)
	corner_frame_NW.grid(column=0, row=0)
	corner_frame_SW.grid(column=0, row=3)
	corner_frame_SE.grid(column=2, row=3)
#Event handling state variables
	drag_enabled = False 
	button1_press_coords = (0, 0)
	#Widget-event-handler binds  
	top_frame.bind("<Button-1>", enable_drag)
	top_frame.bind("<ButtonRelease>", disable_drag)
	top_frame.bind("<Motion>", execute_drag)
	title.bind("<Button-1>", enable_drag)
	title.bind("<ButtonRelease>", disable_drag)
	title.bind("<Motion>", execute_drag)
	border_frame_E.bind("<Button-1>", enable_drag)
	border_frame_E.bind("<Motion>", execute_resize)
	border_frame_E.bind("<ButtonRelease>", disable_drag)
	
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
def enable_drag(button1_press: tk.Event):
	""""Returns True when mouse button 1 is pressed in binded widget. """
	print("Button1 Pressed")
	global drag_enabled
	global button1_press_coords
	drag_enabled = True
	button1_press_coords = button1_press.x, button1_press.y

def disable_drag(button1_release: tk.Event):
	"""Returns False when mouse button 1 is released over the binded widget. """
	print("Button1 Released")
	global drag_enabled
	drag_enabled = False

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

	global drag_enabled
	global button1_press_coords
	#Initial position values of mouse pointer (relative widget (upper left coner of the widget))
	x1, y1 = button1_press_coords[0], button1_press_coords[1]
	if drag_enabled:
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

def execute_resize(motion: tk.Event):
	"""If resize_enabled is True, the function will resize the sub_window widget based on the motion of the mouse and the border frame
	in which motion event is occurring. How to know in which border frame the event is occurring? I could assign the frame a class_
	which identifies it. """
	def resize_right():
		"""Changes the width of the sub_window based on the change in position of the mouse cursor. Assuming the width will increase both to 
		the left and to the right, the sub-window position will change in response to the change in
		position of the mouse cursor, so as to make it seem that only the right side of the window is being resized."""

	def resize_left():
		"""Changes the width of the sub_window based on the change in position of the mouse cursor. Assuming the width will increase 
		both to the left and to the right, the sub-window position will change in response to the change in
		position of the mouse cursor, so as to make it seem that only the left side of the window is being resized.
		"""
		global button1_press_coords
		x1 = button1_press_coords[0]
		if drag_enabled:
			x2 = motion.x
			delta = x2 - x1
			x1 = x2
			border_frame.configure(height = border_frame.winfo_width() + delta)

	def resize_bottom():
		"""Changes the height of the sub-window based on the change in position of the mouse cursor. Assuming both the top and the 
		bottom of the sub-window will adjust for the change in height, the position of the sub-window will adjust also, in order to 
		make it seem that only the buttom of the sub-screen is changing to adjust for the change in height."""
	def resize_top():
		"""Changes the height of the sub-window based on the change in position of the mouse cursor. Assuming both the top and the 
		bottom of the sub-window will adjust for the change in height, the position of the sub-window will adjust also, in order to 
		make it seem that only the top of the sub-screen is changing to adjust for the change in height."""	
	def resize_corner():
		"""Changes both the height and the width of the subwindow at the same time. Uses two side resize functions for each corner. 
		If event widget is corner_frame_NW, resize_top & resize_left
		If NE, resize_top & resize_right
		If SE, resize_bottom & resize_right
		If SW, resize_bottom & resize_left
		"""
	global drag_enabled
	border_frame = motion.widget
	cursor = border_frame.cget('cursor')
	if drag_enabled:
		if cursor == 'right_side':
			resize_right()
		elif cursor == 'left_side':
			resize_left()
		elif cursor == 'top_side':
			resize_top()
		elif cursor == 'bottom_side':
			resize_bottom()
		elif any(cursor_type in cursor for cursor_type in ('top_left_corner', 'bottom_left_corner', 'top_right_corner', 'bottom_right_corner')):
			resize_corner()
	



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