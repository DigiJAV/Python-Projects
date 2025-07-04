from dataclasses import dataclass
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
import PIL
import tkinter as tk
import math
import time

DEFAULT_WINDOW_WIDTH = 350
DEFAULT_WINDOW_HEIGHT = 300
BORDER_WIDTH = 2
TOP_FRAME_HEIGHT = 30
TOP_FRAME_BORDER_WIDTH = 2
MENUBAR_HEIGHT = 25

@dataclass
class Inbox:
    text_input: str
    # file_input: ?

@dataclass
class Date:
    year: int
    month: int
    day: int
    time: int

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

class Sub_Window:
    def __init__(
            self,
            window_type: str,
            window_title: str,
            canvas0: tk.Canvas,
            root: tk.Tk):
        # Generate widgets
        self.type = window_type
        self.drag_enabled = False
        self.button1_press_coords = (0, 0)
        self.type: int
        self.title = window_title
        self.canvas = canvas0
        self.window_width = DEFAULT_WINDOW_WIDTH     #Default width: 350 pixels
        self.window_height = DEFAULT_WINDOW_HEIGHT    #Default height: 300 pixels
        self.sub_window_frame = tk.Frame(
            master=canvas0,
            width=self.window_width,
            height=self.window_height,
            background='blue'
            )
        self.top_frame = tk.Frame(
            master=self.sub_window_frame,
            width=self.window_width - (2 * BORDER_WIDTH),
            height=TOP_FRAME_HEIGHT,
            bg='black',
            relief='raised',
            bd=TOP_FRAME_BORDER_WIDTH
            )
        self.title_label = tk.Label(
            master=self.top_frame,
            text=self.title,
            fg='white',
            bg='black'
            )
        self.window_options_frame = tk.Frame(master=self.top_frame, bg='black')
        self.minimize_button = tk.Button(
            master=self.window_options_frame,
            fg='white',
            bg='black',
            text='\u2013'
            )
        self.full_screen_button = tk.Button(
            master=self.window_options_frame,
            fg='white',
            bg='black',
            text='\u29E0'
            )
        self.close_button = tk.Button(
            master=self.window_options_frame,
            fg='white',
            bg='black',
            text='X'
            )
        self.border_frame_S = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            height=BORDER_WIDTH,
            width=self.window_width - (2 * BORDER_WIDTH),
            cursor='bottom_side',
            bd=0
            )
        self.border_frame_N = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            height=BORDER_WIDTH,
            width=self.window_width - (2 * BORDER_WIDTH),
            bd=0
            )
        self.border_frame_W_1 = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            width=BORDER_WIDTH,
            height=TOP_FRAME_HEIGHT,
            bd=0
            )
        self.border_frame_W2 = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            width=BORDER_WIDTH,
            height=self.window_height - TOP_FRAME_HEIGHT - MENUBAR_HEIGHT - (2 * BORDER_WIDTH),
            bd=0
            )
        self.border_frame_E_1 = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            width=BORDER_WIDTH,
            height=TOP_FRAME_HEIGHT,
            cursor='right_side',
            bd=0
            )
        self.border_frame_E2 = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            width=BORDER_WIDTH,
            height=self.window_height - TOP_FRAME_HEIGHT - MENUBAR_HEIGHT - (2 * BORDER_WIDTH),
            cursor='right_side',
            bd=0
            )
        self.corner_frame_NW = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            bd=0,
            height=BORDER_WIDTH,
            width=BORDER_WIDTH
            )
        self.corner_frame_SW = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            bd=0,
            height=BORDER_WIDTH,
            width=BORDER_WIDTH
            )
        self.corner_frame_NE = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            bd=0,
            height=BORDER_WIDTH,
            width=BORDER_WIDTH
            )
        self.corner_frame_SE = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            bd=0,
            height=BORDER_WIDTH,
            width=BORDER_WIDTH,
            cursor='bottom_right_corner'
            )     
        #This attribute will contain most of the content of the sub-window, beit a list, an image, or a calendar.
        self.content: Sub_Window_Content
    # Configure default widgets
        self.sub_window_frame.grid_propagate(0)
        self.top_frame.grid_propagate(0)
        #self.border_frame_S.grid_propagate(0)
        #self.sub_window_frame.columnconfigure([0, 1, 2], weight=1)
        #self.sub_window_frame.rowconfigure(0, weight=1)
        #self.sub_window_frame.rowconfigure(1, weight=1)
        #self.sub_window_frame.rowconfigure(2, weight=1)
        #self.sub_window_frame.rowconfigure(3, weight=300)
        #self.sub_window_frame.rowconfigure(4, weight=1)
        self.top_frame.columnconfigure([0, 1], weight=1)
    # Place default widgets
        self.sub_window_frame.grid()    # Places the sub-window in the canvas.
        self.canvas_window0_ID = canvas0.create_window(
            50, 50, anchor=tk.NW, window=self.sub_window_frame)
        self.top_frame.grid(column=1, row=1, sticky='n')
        self.window_options_frame.grid(column=1, row=0, sticky='e')
        self.minimize_button.grid(column=1, row=0)
        self.full_screen_button.grid(column=2, row=0)
        self.close_button.grid(column=3, row=0)
        self.title_label.grid(column=0, row=0, sticky='w')
        self.border_frame_S.grid(column=1, row=4)
        self.border_frame_W_1.grid(column=0, row=1)   
        self.border_frame_W2.grid(column=0, row=3)
        self.border_frame_E_1.grid(column=2, row=1)   
        self.border_frame_E2.grid(column=2, row=3)
        self.border_frame_N.grid(column=1, row=0)
        self.corner_frame_NE.grid(column=2, row=0)
        self.corner_frame_NW.grid(column=0, row=0)
        self.corner_frame_SW.grid(column=0, row=4)
        self.corner_frame_SE.grid(column=2, row=4)
    #Sub-window methods 
    def update_size(self):
        """Update internal widget sizes"""
        self.update_sub_window_size()
        if self.type == "List":
            self.content.update_menubar_width(self)
        elif self.type == "Image":
            self.content.update_image_size(self)
            self.content.update_menubar_width(self)
            
    def update_sub_window_size(self):
        """Updates the size of the widgets attributes within the Sub-Window class."""
        self.sub_window_frame.config(
            width=self.window_width, 
            height=self.window_height)
        self.top_frame.config(width=self.window_width - (2 * BORDER_WIDTH))
        self.border_frame_N.config(width=self.window_width - (2 * BORDER_WIDTH))
        self.border_frame_S.config(width=self.window_width - (2 * BORDER_WIDTH))
        
        if self.content.menubar.winfo_manager():
            #Border_frame_2 height values if menubar present
            self.border_frame_E2.config(height=self.window_height - TOP_FRAME_HEIGHT - MENUBAR_HEIGHT - (2 * BORDER_WIDTH))
            self.border_frame_W2.config(height=self.window_height - TOP_FRAME_HEIGHT - MENUBAR_HEIGHT - (2 * BORDER_WIDTH))
        else:
            #Border_frame_2 height values if menubar absent
            self.border_frame_E2.config(height=self.window_height - TOP_FRAME_HEIGHT - (2 * BORDER_WIDTH))
            self.border_frame_W2.config(height=self.window_height - TOP_FRAME_HEIGHT - (2 * BORDER_WIDTH))
        
    def add_sub_window_content(self):
        """Creates instance of class Sub_Window_Content, saves it in the content attribute."""
        self.content = Sub_Window_Content()
        
class Sub_Window_Content:
    def __init__(self):
        self.list: list[str]  # List of strings for now
        self.listbox: tk.Listbox
        self.list_options: List_Options
        self.calendar: Calendar
        self.original_pil_image: PIL.Image
        self.resized_pil_image: PIL.Image
        self.photoimage: tk.PhotoImage
        self.label: tk.Label 
        self.menubar: tk.Frame
        self.menubar_border_E: tk.Frame
        self.menubar_border_W: tk.Frame
    
    def add_image(self, sub_window: Sub_Window):
        """Adds image to Sub_Window_Content, with label widget as parent. Creates the label widget also."""       
        self.original_pil_image = Image.open("C:/Users/User/Documents/Programming/Git repository 1/Sample images/Screenshot 2025-06-08 143629.png") 
        self.resized_pil_image = self.original_pil_image.resize(
            (sub_window.window_width - (4 * BORDER_WIDTH), 
             sub_window.window_height - TOP_FRAME_HEIGHT - MENUBAR_HEIGHT - (4 * BORDER_WIDTH)), 
            Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(image=self.resized_pil_image)
        self.label = tk.Label(master=sub_window.sub_window_frame, image=self.photoimage)
        
    def place_image(self):
        """Creates the label widget on which the image will be displayed. Grids the label widget on the sub_window_frame."""
        self.label.grid(column=1, row=3)
        
    def update_image_size(self, sub_window: Sub_Window):
        """Updates size of the image in an image sub-window"""
        #Resize the pil image
        self.resized_pil_image = sub_window.content.original_pil_image.resize(
            (sub_window.window_width - (4 * BORDER_WIDTH), 
             sub_window.window_height - TOP_FRAME_HEIGHT - MENUBAR_HEIGHT - (4 * BORDER_WIDTH)), 
            Image.LANCZOS)
        #Update tk photoimage with resized pil image
        self.photoimage = ImageTk.PhotoImage(image=self.resized_pil_image)
        #Update label with updated photoiamge
        self.label.configure(image=self.photoimage)
        
    def remove_image(self):
        """Removes image by ungridding the label widget."""
        self.label.grid_remove()
        
    def add_list(self, sub_window: Sub_Window):
        """Adds list that corresponds to the parent Sub_Window of the Sub_Window_Content instance."""
        self.listbox = tk.Listbox(
            master=sub_window.sub_window_frame,
            bg='blue', 
            relief="raised", 
            height=1,
            width=1,
            highlightbackground="blue", 
            activestyle='dotbox')
        for number in range(1,100,1):   #Add sample list
            self.listbox.insert(number, f"Item {number}")
            
    def place_list(self):
        """Places list in the sub_window."""
        self.listbox.grid(column=1, row=3, sticky='nswe')
        
    def add_list_options(self, sub_window: Sub_Window):
        "Adds list control options to the sub-window containing a list."
        self.list_options = List_Options(sub_window)
        
    def add_menubar(self, sub_window: Sub_Window):
        "Adds a menubar; frame in column 1 row 2 used for placing sub-window content ui options."
        self.menubar = tk.Frame(
            master=sub_window.sub_window_frame,
            bg="navy",
            width=sub_window.window_width - 4,
            height=25)
        self.menubar_border_W = tk.Frame(
            master=sub_window.sub_window_frame,
            bg='grey',
            width=BORDER_WIDTH,
            height=MENUBAR_HEIGHT,
            bd=0
            )
        self.menubar_border_E = tk.Frame(
            master=sub_window.sub_window_frame,
            bg='grey',
            width=BORDER_WIDTH,
            height=MENUBAR_HEIGHT,
            cursor='right_side',
            bd=0
            )
        self.menubar.grid_propagate(0)
    
    def place_menubar(self, sub_window: Sub_Window):  
        """Grids menubar in the sub_window_frame. If the border frames associated with the menubar are not gridded, grids them as well."""  
        self.menubar.grid(column=1, row=2, sticky='N')
        self.menubar_border_E.grid(column=2, row=2)
        self.menubar_border_W.grid(column=0, row=2)
        sub_window.update_sub_window_size()
            
    def update_menubar_width(self, sub_window: Sub_Window):
        """Updates the menubar width based on the window_width attribute of the parent Sub_Window instance."""
        sub_window.content.menubar.config(width=sub_window.window_width - (2 * BORDER_WIDTH))
    
    def remove_menubar(self, sub_window: Sub_Window):
        """Ungrids the menubar along with the borderframes associated with it."""  
        self.menubar.grid_remove()
        self.menubar_border_E.grid_remove()
        self.menubar_border_W.grid_remove()
        sub_window.update_sub_window_size()
        
    def place_list_options(self):
        """Grids widgets of the List_Options class."""
        self.list_options.sort_menubutton.grid(column=0, row=0, sticky='W')
        self.list_options.filter_menubutton.grid(column=1, row=0)

    def add_calendar(self, sub_window: Sub_Window):
        """Adds a calendar to Sub_Window_Content class."""
        self.calendar = Calendar(master=sub_window.sub_window_frame)
        
    def place_calendar(self):
        """Places calendar in the sub_window."""
        self.calendar.grid(column=1, row=3, sticky='nwes')
        
    def add_scrollbars(self):
        """Adds vertical and horizontal scrollbars. Scrollbars will be present in all sub windows when necessary. Scrollbars will automatically
        appear when the content of the sub window exceeds the size of the sub window, such that part of it is obscured. Because scrollbars are
        a property of all sub_windows, it should be placed as an attribute of the Sub_Window class. The function will be called whenever
        scrollbars are necessary. Another function, remove_scrollbars, will remove them when unecessary."""
        
    def remove_scrollbars(self):
        """"""       
        
class List_Options:
    def __init__(self, sub_window: Sub_Window):
        self.sort_menubutton = tk.Menubutton(
            master=sub_window.content.menubar, 
            text='Sort Options', 
            borderwidth=2, 
            bg='grey', 
            relief="raised")
        self.filter_menubutton = tk.Menubutton(
            master=sub_window.content.menubar, 
            text='Filter Options', 
            borderwidth=2, 
            bg='grey', 
            relief="raised")
        self.sort_menu = tk.Menu(master=self.sort_menubutton, tearoff=False)
        self.filter_menu = tk.Menu(
            master=self.filter_menubutton, tearoff=False)
        self.sort_menubutton['menu'] = self.sort_menu
        self.filter_menubutton['menu'] = self.filter_menu
        self.sort_options = ["Alphabetical order", "Attribute", "Deadline"]
        self.filter_options = ["Key-word", "Attribute", "Deadline"]
        # List_options available after selecting and right clicking on selected list items. May select multiple at a time.
        # Right clicking generates at drop down menu at location of right click
        self.other_options = ["Delete", "Mark as completed"]
        
        #self.menubar.columnconfigure(0, weight=1)
        #self.menubar.columnconfigure(1, weight=1)
        
        # Populate sort & filter menus
        for option in self.sort_options:
            self.sort_menu.add_command(
                label=option, command=lambda option=option: print(option))
        for option in self.filter_options:
            self.filter_menu.add_command(
                label=option, command=lambda option=option: print(option))  
        
    def remove_widgets(self):
        """Removes List_Options class widgets."""

    def generate_menu(self):
        """Event handler. Generates dropdown menu of list options upon mouse right button click. Either the right click must occur directly on a list item, or one or more list items must be
        selected, in order for right click to generate a menu. Mouse left button click outside the bounds of the menu will close the menu. Mouse left button click on a menu
        option will execute the command associated with that option, and it will also close the menu."""
        # Need to get location of right mouse button click within the sub-window frame.
        # Need to generate a menu without it being associated with a menu button. Perhaps the parent of the menu will be the frame.
        # Perhaps a separate function should be used to remove the menu.
        # Checks if any menu items selected
        # Checks if right mouse button click occurred on a menu item list. Or right mouse button click selects and opens list menu for selection.
        # List menu commands applied only to list items selected.
        # Right mouse button click may occur on list widget or on the
        # sub-window frame widget.
 
# Data functions
def add_input():
    """Receives input from UI. Creates instance of Inbox. Appends istance to inbox_list."""

def process_inbox():
    """Receives input from UI. Creates instance of Actionable or Non_Actionable. 
    Appends instance to a list. Calls the following functions:
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

# UI Functions
def create_root_window():
    window0 = tk.Tk()
    screen_width = window0.winfo_screenwidth()
    screen_height = window0.winfo_screenheight()
    window0.geometry(f"{screen_width}x{screen_height}")  # f-strings
    window0.title("Getting Things Done")
    return window0

def create_root_canvas(window0):
    screen_width = window0.winfo_screenwidth()
    screen_height = window0.winfo_screenheight()
    canvas = tk.Canvas(
        master=window0,
        width=screen_width,
        height=screen_height,
        bg='black')
    canvas.grid(column=0, row=0)
    return canvas

def create_sub_windows(window0: tk.Tk, canvas0: tk.Canvas) -> list[tk.Frame]:
    """Creates an empty sub_window."""
    def create_basic_widgets(title: str, type: str, canvas0: tk.Canvas):
        """Generates the basic widgets that make up a sub-window. These are widgets that will be present in all sub-windows."""
        sub_window = Sub_Window(
            type,
            title,
            canvas0,
            window0)  # The basic widgets of a sub window are already attributes of a sub-window object.
        # Therefore, they are automatically generated, configured, and placed,
        # upon creation of the sub-window object.
        return sub_window

    # There will be multiple functions that create window content. There will be code that uses the title of the sub-window to determine which function to use.
    # create_window_content is the function that will house the sub functions and the code that will determine which of these sub-functions is used.
    # Since all the sub-window types to be used in the program are known, the
    # sub-functions and their triggers will be hardcoded.

    def create_window_content(sub_window: Sub_Window, list: list):
        """Fills subwindow with list items, list options, sort and filter options, scroll bars, calendar, image, etc. Content depends on the sub-windows title.  """
        # Code to determine whether sub_Window will contain lists, calendar, or image. For this. the Sub_Window class can have an attribute
        # will tell which of these options is the case. The attribute will be called type. Three possible definitions for the attribute are
        # strings, corresponding to List, Calendar, or Image, respectively.
        # list_control_options = List_Control_Options(window.menubar)
        # content = Sub_Window_Content(list, listbox, window.menubar, list_control_options)
        # window.content = content
        sub_window.add_sub_window_content()
        if sub_window.type == "List":
            sub_window.content.add_menubar(sub_window)
            sub_window.content.add_list_options(sub_window)
            sub_window.content.add_list(sub_window)
            sub_window.content.place_menubar(sub_window)
            sub_window.content.place_list()
            sub_window.content.place_list_options()
        elif sub_window.type == "Calendar":
            """Add calendar"""
            sub_window.content.add_menubar(sub_window)
            sub_window.content.place_menubar(sub_window)
            sub_window.content.add_calendar(sub_window)
            sub_window.content.place_calendar()
        elif sub_window.type == "Image":
            """Add Image"""
            sub_window.content.add_image(sub_window)
            sub_window.content.place_image()
            sub_window.content.add_menubar(sub_window)
            sub_window.content.place_menubar(sub_window)
            
    #def configure_layout(sub_window: Sub_Window):
        #"""Configures layout of widgets within a sub window."""
        # Default widgets layout done upon creation of object. Additional
        # widgets depending of type of sub-window to be configured separately.

    #def place_window_content(sub_window: Sub_Window):
      #""""""
        # Default widgets placed upone creation of the sub-window. Additional
        # widgets placed depending on type of sub-window.
    
    def create_window(
            window0: tk.Tk,
            canvas0: tk.Canvas,
            title: str,
            type: str) -> tk.Frame:
        """Creates a sub-window. Runs other sub-functions depending on the type of subwindow."""
        sub_window = create_basic_widgets(title, type, canvas0)
        create_window_content(sub_window, next_actions_list)
        return sub_window

    next_actions_window = create_window(
        window0, canvas0, "Next Actions", "List")
    upcoming_events_window = create_window(
        window0, canvas0, "Upcoming Events Window", "List")
    ticklers_window = create_window(window0, canvas0, "Ticklers", "List")
    outcomes_window = create_window(window0, canvas0, "Outcomes", "List")
    waiting_for_window = create_window(window0, canvas0, "Waiting For", "List")
    calendar_window = create_window(window0, canvas0, "Calendar", "Calendar")
    image_window = create_window(window0, canvas0, "Image", "Image")
    # Initial x and y positions of the canvas window objects is modified to
    # avoid overlap. (Modified from the inital position upon creation, which is (50,50))
    upcoming_events_window.canvas.coords(
        upcoming_events_window.canvas_window0_ID, 400, 50)
    ticklers_window.canvas.coords(ticklers_window.canvas_window0_ID, 750, 50)
    outcomes_window.canvas.coords(outcomes_window.canvas_window0_ID, 1100, 50)
    waiting_for_window.canvas.coords(waiting_for_window.canvas_window0_ID, 50, 400)
    calendar_window.canvas.coords(calendar_window.canvas_window0_ID, 400, 400)
    image_window.canvas.coords(image_window.canvas_window0_ID, 750, 400)
    sub_windows = [
        next_actions_window,
        upcoming_events_window,
        ticklers_window,
        outcomes_window,
        waiting_for_window,
        calendar_window,
        image_window]
    return sub_windows

def event_handling(sub_window: Sub_Window):
    """"""
    # Widget-event-handler binds
 # Will using lambda functions to call all event handlers, in order to use window as an argument in each of them. This will enable easy access
 # of the window object attributes.
    sub_window.sub_window_frame.bind(
        "<Button-1>",
        lambda event: lift_window(
            event,
            sub_window))
    sub_window.top_frame.bind(
        "<Button-1>",
        lambda event: (
            enable_drag(
                event, 
                sub_window), 
            lift_window(
                event, 
                sub_window)))
    sub_window.top_frame.bind(
        "<ButtonRelease>",
        lambda event: disable_drag(
            event,
            sub_window))
    sub_window.top_frame.bind(
        "<Motion>",
        lambda event: execute_drag(
            event,
            sub_window))
    sub_window.title_label.bind(
        "<Button-1>",
        lambda event: (enable_drag(
            event,
            sub_window), 
                       lift_window(
            event, 
            sub_window)))
    sub_window.title_label.bind(
        "<ButtonRelease>",
        lambda event: disable_drag(
            event,
            sub_window))
    sub_window.title_label.bind(
        "<Motion>",
        lambda event: execute_drag(
            event,
            sub_window))
    if sub_window.type != "Calendar":
        east_border_frames = [
            sub_window.border_frame_E_1, 
            sub_window.content.menubar_border_E, 
            sub_window.border_frame_E2]
        for frame in east_border_frames:
            frame.bind(
                "<Button-1>",
                lambda event: (
                    enable_drag(
                        event, 
                        sub_window), 
                    lift_window(
                        event, 
                        sub_window)))
            frame.bind(
                "<Motion>", 
                lambda event: resize_right(
                    event, sub_window))
            frame.bind(
                "<ButtonRelease>",
                lambda event: disable_drag(
                    event,
                    sub_window))
        sub_window.border_frame_S.bind(
            "<Button-1>",
            lambda event: (
                enable_drag(
                    event, 
                    sub_window), 
                lift_window(
                    event, 
                    sub_window)))
        sub_window.border_frame_S.bind(
            "<ButtonRelease>",
            lambda event: disable_drag(
                event,
                sub_window))
        sub_window.border_frame_S.bind(
            "<Motion>", lambda event: resize_bottom(
                event, sub_window))
        sub_window.corner_frame_SE.bind(
            "<Button-1>",
            lambda event: (
                enable_drag(
                    event,
                    sub_window), 
                lift_window(
                    event, 
                    sub_window)))
        sub_window.corner_frame_SE.bind(
            "<ButtonRelease>",
            lambda event: disable_drag(
                event,
                sub_window))
        sub_window.corner_frame_SE.bind(
            "<Motion>", lambda event: resize_corner(
                event, sub_window))
        
    if sub_window.type == "List":  
        sub_window_content_widgets = [
            sub_window.content.listbox,
            sub_window.content.menubar,
            sub_window.content.list_options.filter_menubutton,
            sub_window.content.list_options.sort_menubutton
            ]
        for widget in sub_window_content_widgets:
            widget.bind("<Button-1>", lambda event: lift_window(event, sub_window))
    
    elif sub_window.type == "Image": 
        sub_window.content.label.bind("<Button-1>", lambda event: lift_window(event, sub_window))
    
    elif sub_window.type == "Calendar":
        sub_window.content.calendar.bind("<<CalendarSelected>>", lambda event: lift_window(event, sub_window))
        sub_window.content.calendar.bind("<<CalendarMonthChanged>>", lambda event: lift_window(event, sub_window))
        
def ui_manager():
    "Manages UI."
    window0 = create_root_window()
    canvas0 = create_root_canvas(window0)
    sub_windows = create_sub_windows(window0, canvas0)
    for sub_window in sub_windows:
        event_handling(sub_window)
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

### Event Handlers ##################################
def lift_window(button1_press: tk.Event, sub_window: Sub_Window):
    """Upon a sub-window being clicked with left mouse button at any point within it, the event handler lifts the clicked sub-window to top of stack."""
    sub_window.sub_window_frame.lift(aboveThis=None)

def enable_drag(button1_press: tk.Event, sub_window: Sub_Window):
    """"Returns True when mouse button 1 is pressed in binded widget. """
    sub_window.drag_enabled = True
    sub_window.button1_press_coords = button1_press.x, button1_press.y

def disable_drag(button1_release: tk.Event, sub_window: Sub_Window):
    """Returns False when mouse button 1 is released over the binded widget. """
    sub_window.drag_enabled = False

def execute_drag(mouse_motion: tk.Event, sub_window: Sub_Window):
    """Called when motion detected in binded frame, and drag_status == True."""
    start = time.time()
    # Initial position values of mouse pointer (relative widget (upper left
    # coner of the widget))
    x1, y1 = sub_window.button1_press_coords[0], sub_window.button1_press_coords[1]
    if sub_window.drag_enabled:
        # Final position values of the mouse pointer (relative widget (upper
        # left corner of the widget))
        x2 = mouse_motion.x
        y2 = mouse_motion.y
        # Calculates change in x and change in y from difference between
        # initial and final position of mouse pointer. Initial position:
        # (x1,y1), final position (x2, y2).
        delta_x = x2 - x1
        delta_y = y2 - y1
        x1 = x2
        y1 = y2
        # Update the position of the canvas window object using change in x and change in y of mouse pointer.
        # canvas, canvas_window_object_ID = get_canvas_window_obj_ID()
        sub_window.canvas.move(sub_window.canvas_window0_ID, delta_x, delta_y)
        end = time.time()
        execute_time = end - start
        if execute_time > 0.004:
            print(f"execute_drag took {execute_time} seconds.")
        
def resize_right(motion: tk.Event, sub_window: Sub_Window):
    """Changes the width of the sub_window based on the change in position of the mouse cursor. Assuming the width will increase both to
            the left and to the right, the sub-window position will change in response to the change in
            position of the mouse cursor, so as to make it seem that only the right side of the window is being resized."""
    start = time.time()
    if sub_window.drag_enabled:
        # Get initial and current mouse x-coordinates
        x1 = sub_window.button1_press_coords[0]
        x2 = motion.x
        
        # Calculate horizontal movement
        delta_cursor = x2 - x1  
        x1 = x2     # Update starting point for next movement
        
        # Compute new window width
        delta_window = sub_window.window_width + delta_cursor
        
        # Enforce minimum width constraint
        if delta_window > 130:  
            sub_window.window_width = delta_window
            sub_window.update_size()
    end = time.time()
    execute_time = end - start
    if execute_time > 0.004:   
        print(f"resize_right took {execute_time} seconds.")
    
def resize_bottom(motion: tk.Event, sub_window: Sub_Window):
    """Changes the height of the sub-window based on the change in position of the mouse cursor. Assuming both the top and the
    bottom of the sub-window will adjust for the change in height, the position of the sub-window will adjust also, in order to
    make it seem that only the buttom of the sub-screen is changing to adjust for the change in height."""
    start = time.time()
    if sub_window.drag_enabled:
        y1 = sub_window.button1_press_coords[1]
        y2 = motion.y
        # Vertical change in position of mouse cursor in the subwindow frame
        delta_cursor = y2 - y1
        y1 = y2
        delta_window = sub_window.window_height + delta_cursor

        #Imposes minimum width to the sub_window, so that the top frame remains visible.
        if delta_window > 34:    
            sub_window.window_height = delta_window
            sub_window.update_size()
        #Removes menubar once a minimum window height is reached, to enable uninterrupted resizing.
        if sub_window.type == "List" or sub_window.type == "Image":
            if sub_window.window_height < 60 and sub_window.content.menubar.winfo_manager() != "":  
                sub_window.content.remove_menubar(sub_window)

            elif sub_window.window_height > 60 and sub_window.content.menubar.winfo_manager() == "":
                sub_window.content.place_menubar(sub_window)
    
        if sub_window.type == 'List':
            if sub_window.content.listbox.winfo_manager() != "" and sub_window.window_height < 80:
                sub_window.content.listbox.grid_remove()
            elif sub_window.type == 'List' and sub_window.content.listbox.winfo_manager() == "" and sub_window.window_height > 80:
                sub_window.content.listbox.grid()
                
        if sub_window.type == "Image":
            if sub_window.content.label.winfo_manager() != "" and sub_window.window_height < 65:
                sub_window.content.remove_image()
            elif sub_window.content.label.winfo_manager() == "" and sub_window.window_height > 65:
                sub_window.content.place_image()
    end = time.time()
    execute_time = end - start
    if execute_time > 0.004:
        print(f"resize_bottom took {execute_time} seconds.")           
    #print("Window height: ", sub_window.window_height)
    #print("Border frame S height: ", sub_window.border_frame_S.winfo_height())
    #print("Border frame S height: ", sub_window.border_frame_S.winfo_height())

def resize_corner(motion: tk.Event, sub_window: Sub_Window):
    """Uses functions resize bottom and resize right at the same time when user clicks and drags on SW corner frame."""
    start = time.time()
    if sub_window.drag_enabled:
        resize_right(motion, sub_window)
        resize_bottom(motion, sub_window)
    end = time.time()
    print(f"resize_corner took {end - start} seconds.")
# Lists
inbox_list = []
next_actions_list = []
projects_list = []
calendar_list = []
waiting_for_list = []
reference_list = []
someday_list = []
tickler_list = []
trash_list = []

completed_actions_list = []
completed_projects_list = []
achieved_outcomes_list = []

topics_list = []

filter_options = []
sort_options = []

ui_manager()
