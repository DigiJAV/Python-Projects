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
class List_Control_Options:
	def __init__(self, sub_window_frame: tk.Frame):
		self.sort_menubutton = tk.Menubutton(master=sub_window_frame, text='Sort Options')
		self.filter_menubutton = tk.Menubutton(master=sub_window_frame, text='Filter Options')
		self.sort_menu = tk.Menu(master=self.sort_menubutton)
		self.filter_menu = tk.Menu(master=self.filter_menubutton)
		self.sort_menubutton['menu'] = self.sort_menu
		self.filter_menubutton['menu'] = self.filter_menu
		self.sort_options = ["Alphabetical order", "Attribute", "Deadline"]
		self.filter_options = ["Key-word", "Attribute", "Deadline" ]
		#List_options available after selecting and right clicking on selected list items. May select multiple at a time. Right clicking generates at drop down menu at location of right click 
		self.list_options = ["Delete", "Mark as completed"]
		#Populate sort & filter menus
		for option in sort_options:
			self.sort_menu.add_command(label = option, command = lambda: print(option))
		for option in filter_options:
			self.filter_menu.add_command(label = option, command = lambda: print(option))

		def generate_menu():
			"""Event handler. Generates dropdown menu of list options upon mouse right button click. Either the right click must occur directly on a list item, or one or more list items must be
			selected, in order for right click to generate a menu. Mouse left button click outside the bounds of the menu will close the menu. Mouse left button click on a menu
			option will execute the command associated with that option, and it will also close or remove the menu."""
			#Need to get location of right mouse button click within the sub-window frame. 
			#Need to generate a menu without it being associated with a menu button. Perhaps the parent of the menu will be the frame. 
			#Perhaps a separate function should be used to remove the menu. 
			#Checks if any menu items selected
			#Checks if right mouse button click occurred on a menu item list. Or right mouse button click selects and opens list menu for selection. 
			#List menu commands applied only to list items selected. 
			#Right mouse button click may occur on list widget or on the sub-window frame widget. 
	
@dataclass
class Sub_Window_Content:
	item_list: list[str]
	listbox_widget: tk.Listbox
	menubar: tk.Frame
	list_control_options: List_Control_Options
class Sub_Window:
	def __init__(self, window_title: str, canvas0: tk.Canvas):
		self.title = window_title
		self.canvas = canvas0
		self.window_dimensions = [300, 300] 	# Default width & height of sub-windows
		self.sub_window_frame = tk.Frame(master=canvas0, width = self.window_dimensions[0], height = self.window_dimensions[1], background='blue')
		self.top_frame = tk.Frame(master=self.sub_window_frame, width=self.window_dimensions[0]-4, height=30, bg='black', relief='raised', bd=2)
		self.title_label = tk.Label(master=self.top_frame, text=self.title, fg='white', bg='black')
		self.window_options_frame = tk.Frame(master=self.top_frame, bg='black')
		self.minimize_button = tk.Button(master=self.window_options_frame, fg='white', bg='black', text ='\u2013')
		self.full_screen_button = tk.Button(master=self.window_options_frame, fg='white', bg='black', text='\u29E0')
		self.close_button = tk.Button(master=self.window_options_frame, fg='white', bg='black', text='X')
		self.border_frame_S = tk.Frame(master=self.sub_window_frame, bg='grey', height=2, width=self.window_dimensions[0]-4, cursor='bottom_side', relief='raised')
		self.border_frame_N = tk.Frame(master=self.sub_window_frame, bg='grey', height=2, width=self.window_dimensions[0]-4, relief='raised')
		self.border_frame_W = tk.Frame(master=self.sub_window_frame, bg='grey', height=self.window_dimensions[1]-4, width=2, relief='raised')
		self.border_frame_E = tk.Frame(master=self.sub_window_frame, bg='grey', height=self.window_dimensions[1]-4, width=2, cursor='right_side', relief='raised')
		self.corner_frame_NW = tk.Frame(master=self.sub_window_frame, bg='grey', bd=1, borderwidth=2, height=2, width=2, relief='raised')
		self.corner_frame_SW = tk.Frame(master=self.sub_window_frame, bg='grey', bd=1, borderwidth=2, height=2, width=2, relief='raised')
		self.corner_frame_NE = tk.Frame(master=self.sub_window_frame, bg='grey', bd=1, borderwidth=2, height=2, width=2, relief='raised')
		self.corner_frame_SE = tk.Frame(master=self.sub_window_frame, bg='grey', bd=1, borderwidth=2, height=2, width=2, cursor='bottom_right_corner', relief='raised')
		self.content = None
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
def create_root_window():
	window0 = tk.Tk()
	screen_width = window0.winfo_screenwidth()
	screen_height = window0.winfo_screenheight()
	window0.geometry(f"{screen_width}x{screen_height}")
	window0.title("Getting Things Done")
	return window0

def create_root_canvas(window0):
	screen_width = window0.winfo_screenwidth()
	screen_height = window0.winfo_screenheight()
	canvas = tk.Canvas(window0, width=screen_width, height=screen_height, bg='black')
	canvas.grid(column=0, row=0)
	return canvas

def create_sub_windows(window0: tk.Tk, canvas0: tk.Canvas)->list[tk.Frame]:
	"""Creates an empty sub_screen."""
	def create_basic_widgets(title: str, canvas0: tk.Canvas):
		"""Generates the basic widgets that make up a sub-window."""
		window = Sub_Window(title, canvas0)	
		canvas_window0_ID = canvas0.create_window(100,100, anchor=tk.NW, window=window.sub_window_frame)
		return window
	def create_window_content(window: Sub_Window, list: list):
		"""Fills subwindow with list items, list options, sort and filter options, scroll bars, calendar, image, etc. Content depends on the sub-windows title.  """
		listbox = tk.Listbox(master=window.sub_window_frame)
		menubar = tk.Frame(master=window.sub_window_frame, bg='red', width=window.window_dimensions[0]-4, height=20, relief='raised')
		list_control_options = List_Control_Options(menubar)
		content = Sub_Window_Content(list, listbox, menubar, list_control_options)
		window.content = content
		def add_list(title:str):
			"""Adds list that corresponds to the sub_window."""
			#The list already exists.
			#The list will be dynamically updated. 
			#This function takes the already existing list, to an element in 
		def add_options(title: str):
			"""Adds sub-window content manipulation options that correspond to the sub-window. Determined via if statements, using the title. These may be:
			 sort options, filter options, list item options, etc. """
			
		def add_scrollbars():
			"""Adds vertical and horizontal scrollbars"""
		def add_calendar():
			""""""
		def add_image():
			""""""
	def configure_layout(window: Sub_Window):
		window.sub_window_frame.grid_propagate(0)
		window.top_frame.grid_propagate(0)
		window.content.menubar.grid_propagate(0)
		#Configure columns and rows
		window.sub_window_frame.columnconfigure([0,1,2], weight=1)
		window.sub_window_frame.rowconfigure(0, weight=1)
		window.sub_window_frame.rowconfigure(1, weight=1)
		window.sub_window_frame.rowconfigure(2, weight=1)
		window.sub_window_frame.rowconfigure(3, weight=1)
		window.sub_window_frame.rowconfigure(4, weight=1)
		window.top_frame.columnconfigure([0,1], weight=1)
		window.content.menubar.columnconfigure([0,1], weight=1)
	def place_widgets(window: Sub_Window):
		""""""
		window.top_frame.grid(column=1, row=1, sticky='n')
		window.window_options_frame.grid(column=1, row=0, sticky='e')
		window.minimize_button.grid(column=1, row=0)
		window.full_screen_button.grid(column=2, row=0)
		window.close_button.grid(column=3, row=0)
		window.title_label.grid(column=0, row=0, sticky='w')
		window.border_frame_S.grid(column=1, row=4)
		window.border_frame_W.grid(column=0, row=1, rowspan=3)
		window.border_frame_E.grid(column=2, row=1, rowspan=3)
		window.border_frame_N.grid(column=1, row=0)
		window.corner_frame_NE.grid(column=2, row=0)
		window.corner_frame_NW.grid(column=0, row=0)
		window.corner_frame_SW.grid(column=0, row=4)
		window.corner_frame_SE.grid(column=2, row=4)
		window.content.menubar.grid(column=1, row=2, sticky='n')
		window.content.list_control_options.sort_menubutton.grid(column=0, row=0)
		window.content.list_control_options.filter_menubutton.grid(column=1, row=0)
	def create_window(window0: tk.Tk, canvas0: tk.Canvas, title: str)->tk.Frame:
		"""Creates a sub-window"""
		window = create_basic_widgets(title, canvas0)
		create_window_content(window, next_actions_list)
		configure_layout(window)
		place_widgets(window)
		return window
	
	next_actions_window = create_window(window0, canvas0, "Next Actions")
	windows = [next_actions_window]
	return windows

def event_handling(window: Sub_Window):
		""""""
		drag_enabled = False 
		button1_press_coords = (0, 0)
		#Widget-event-handler binds  
		window.top_frame.bind("<Button-1>", enable_drag)
		window.top_frame.bind("<ButtonRelease>", disable_drag)
		window.top_frame.bind("<Motion>", execute_drag)
		window.title_label.bind("<Button-1>", enable_drag)
		window.title_label.bind("<ButtonRelease>", disable_drag)
		window.title_label.bind("<Motion>", execute_drag)
		window.border_frame_E.bind("<Button-1>", enable_drag)
		window.border_frame_E.bind("<ButtonRelease>", disable_drag)
		window.border_frame_E.bind("<Motion>", resize_right)
		window.border_frame_S.bind("<Button-1>", enable_drag)
		window.border_frame_S.bind("<ButtonRelease>", disable_drag)
		window.border_frame_S.bind("<Motion>", resize_bottom)
		window.corner_frame_SE.bind("<Button-1>", enable_drag)
		window.corner_frame_SE.bind("<ButtonRelease>", disable_drag)
		window.corner_frame_SE.bind("<Motion>", resize_corner)
def ui_manager():
	"Manages UI."
	window0= create_root_window()
	canvas0= create_root_canvas(window0)
	sub_windows = create_sub_windows(window0, canvas0)
	for window in sub_windows:
		event_handling(window)
	window0.mainloop()
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
	print("Button Press location: ", button1_press_coords)

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


def resize_right(motion: tk.Event):
	"""Changes the width of the sub_window based on the change in position of the mouse cursor. Assuming the width will increase both to 
		the left and to the right, the sub-window position will change in response to the change in
	position of the mouse cursor, so as to make it seem that only the right side of the window is being resized."""
	global button1_press_coords
	global drag_enabled
	frame = motion.widget
	sub_window = frame.master
	children = sub_window.winfo_children()
	top_frame = children[0]
	border_frame_S = children[1]
	border_frame_N = children[2]
	if drag_enabled:
		x1 = button1_press_coords[0]
		x2 = motion.x
		delta_cursor = x2 - x1 	#Horizontal change in position of mouse cursor
		x1 = x2
		delta_sub_window = sub_window.winfo_width() + delta_cursor
		delta_top_frame = top_frame.winfo_width() + delta_cursor
		delta_border_frame_N = border_frame_N.winfo_width() + delta_cursor
		delta_border_frame_S = border_frame_S.winfo_width() + delta_cursor
		if delta_sub_window > 130:	
			sub_window.configure(width = delta_sub_window)
			top_frame.configure(width = delta_top_frame)
			border_frame_N.configure(width = delta_border_frame_N)
			border_frame_S.configure(width = delta_border_frame_S)

def resize_bottom(motion: tk.Event):
	"""Changes the height of the sub-window based on the change in position of the mouse cursor. Assuming both the top and the 
	bottom of the sub-window will adjust for the change in height, the position of the sub-window will adjust also, in order to 
	make it seem that only the buttom of the sub-screen is changing to adjust for the change in height."""
	global button1_press_coords
	global drag_enabled
	frame = motion.widget
	sub_window = frame.master
	children = sub_window.winfo_children()
	border_frame_W = children[3]
	border_frame_E = children[4]
	if drag_enabled:
		y1 = button1_press_coords[1]
		y2 = motion.y
		delta_cursor = y2 - y1 	#Horizontal change in position of mouse cursor
		y1 = y2
		delta_sub_window = sub_window.winfo_height() + delta_cursor
		delta_border_frame_W = border_frame_W.winfo_height() + delta_cursor
		delta_border_frame_E = border_frame_E.winfo_height() + delta_cursor
		if delta_sub_window > 31:
			sub_window.configure(height = delta_sub_window)
			border_frame_W.configure(height = delta_border_frame_W)
			border_frame_E.configure(height = delta_border_frame_E)

def resize_corner(motion: tk.Event):
	"""Uses functions resize bottom and resize right at the same time when user clicks and drags from SW corner of window"""
	if drag_enabled:
		resize_right(motion)
		resize_bottom(motion)

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