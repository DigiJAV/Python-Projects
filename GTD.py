from dataclasses import dataclass
from tkinter import ttk
import PIL.Image
from tkcalendar import Calendar
from PIL import Image, ImageTk
import PIL
import tkinter as tk
import math


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


class List_Options:
    def __init__(self, menubar: tk.Frame):
        self.sort_menubutton = tk.Menubutton(
            master=menubar, text='Sort Options', borderwidth=2, bg='grey', relief="raised")
        self.filter_menubutton = tk.Menubutton(
            master=menubar, text='Filter Options', borderwidth=2, bg='grey', relief="raised")
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
        # Populate sort & filter menus
        for option in self.sort_options:
            self.sort_menu.add_command(
                label=option, command=lambda option=option: print(option))
        for option in self.filter_options:
            self.filter_menu.add_command(
                label=option, command=lambda option=option: print(option))

        def generate_menu():
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


class Sub_Window_Content:
    def __init__(self):
        self.item_list: list[str]  # List of strings for now
        self.listbox_widget: tk.Listbox
        self.list_options: List_Options
        self.calendar: tk.Widget
        self.pil_image: PIL.Image
        self.photoimage: tk.PhotoImage
        self.label: tk.Label

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
        self.window_width = 350     #Default width: 350 pixels
        self.window_height = 300    #Default height: 300 pixels
        self.sub_window_frame = tk.Frame(
            master=canvas0,
            width=self.window_width,
            height=self.window_height,
            background='blue')
        self.top_frame = tk.Frame(
            master=self.sub_window_frame,
            width=self.window_width - 4,
            height=30,
            bg='black',
            relief='raised',
            bd=2)
        self.title_label = tk.Label(
            master=self.top_frame,
            text=self.title,
            fg='white',
            bg='black')
        self.window_options_frame = tk.Frame(master=self.top_frame, bg='black')
        self.minimize_button = tk.Button(
            master=self.window_options_frame,
            fg='white',
            bg='black',
            text='\u2013')
        self.full_screen_button = tk.Button(
            master=self.window_options_frame,
            fg='white',
            bg='black',
            text='\u29E0')
        self.close_button = tk.Button(
            master=self.window_options_frame,
            fg='white',
            bg='black',
            text='X')
        self.border_frame_S = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            height=2,
            width=self.window_width - 4,
            cursor='bottom_side',
            relief='raised')
        self.border_frame_N = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            height=2,
            width=self.window_width - 4,
            relief='raised')
        self.border_frame_W = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            height=self.window_height - 4,
            width=2,
            relief='raised')
        self.border_frame_E = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            height=self.window_height - 4,
            width=2,
            cursor='right_side',
            relief='raised')
        self.corner_frame_NW = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            bd=1,
            borderwidth=2,
            height=2,
            width=2,
            relief='raised')
        self.corner_frame_SW = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            bd=1,
            borderwidth=2,
            height=2,
            width=2,
            relief='raised')
        self.corner_frame_NE = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            bd=1,
            borderwidth=2,
            height=2,
            width=2,
            relief='raised')
        self.corner_frame_SE = tk.Frame(
            master=self.sub_window_frame,
            bg='grey',
            bd=1,
            borderwidth=2,
            height=2,
            width=2,
            cursor='bottom_right_corner',
            relief='raised')
        self.menubar = tk.Frame(
            master=self.sub_window_frame,
            bg="navy",
            width=self.window_width - 4,
            height=25,
            relief='raised')
        # This attribute will contain most of the content of the sub-window, be
        # it a list, an image, or a calendar.
        self.content = Sub_Window_Content
        # The content will be determined after the Sub_Window object initialization.
    # Configure default widgets
        self.sub_window_frame.grid_propagate(0)
        self.top_frame.grid_propagate(0)
        self.menubar.grid_propagate(0)
        self.sub_window_frame.columnconfigure([0, 1, 2], weight=1)
        self.sub_window_frame.rowconfigure(0, weight=1)
        self.sub_window_frame.rowconfigure(1, weight=1)
        self.sub_window_frame.rowconfigure(2, weight=1)
        self.sub_window_frame.rowconfigure(3, weight=300)
        self.sub_window_frame.rowconfigure(4, weight=1)
        self.top_frame.columnconfigure([0, 1], weight=1)
        self.menubar.columnconfigure(0, weight=1)
        self.menubar.columnconfigure(1, weight=1)
    # Place default widgets
        # Places the sub-window in the canvas.
        self.sub_window_frame.grid()
        self.canvas_window0_ID = canvas0.create_window(
            50, 50, anchor=tk.NW, window=self.sub_window_frame)
        self.top_frame.grid(column=1, row=1, sticky='n')
        self.window_options_frame.grid(column=1, row=0, sticky='e')
        self.minimize_button.grid(column=1, row=0)
        self.full_screen_button.grid(column=2, row=0)
        self.close_button.grid(column=3, row=0)
        self.title_label.grid(column=0, row=0, sticky='w')
        self.border_frame_S.grid(column=1, row=4)
        self.border_frame_W.grid(column=0, row=1, rowspan=3)
        self.border_frame_E.grid(column=2, row=1, rowspan=3)
        self.border_frame_N.grid(column=1, row=0)
        self.corner_frame_NE.grid(column=2, row=0)
        self.corner_frame_NW.grid(column=0, row=0)
        self.corner_frame_SW.grid(column=0, row=4)
        self.corner_frame_SE.grid(column=2, row=4)
        self.menubar.grid(column=1, row=2, sticky='new')
    #Sub-window methods    
    def update_size(self):
        """Update internal widget sizes"""
        def update_image_size():
            """Updates size of the image in an image sub-window"""
            #Resize the pil image
            self.content.pil_image = self.content.pil_image.resize((self.window_width - 20, self.window_height - 20))
            #Update tk photoimage with resized pil image
            self.content.photoimage = ImageTk.PhotoImage(image=self.content.pil_image)
            #Update label with updated photoiamge
            self.content.label.configure(image=self.content.photoimage)
        
        self.sub_window_frame.config(
            width=self.window_width, 
            height=self.window_height)
        self.top_frame.config(width=self.window_width - 4)
        self.border_frame_N.config(width=self.window_width - 4)
        self.border_frame_S.config(width=self.window_width - 4)
        self.border_frame_E.config(height=self.window_height - 4)
        self.border_frame_W.config(height=self.window_height - 4)
        self.menubar.config(width=self.window_width - 4)
        update_image_size()
        
    def add_list(self):
        """Adds list that corresponds to the sub_window."""
        self.content.listbox_widget = tk.Listbox(
            master=self.sub_window_frame,  
            bg='blue', relief="raised", 
            highlightbackground="blue", 
            activestyle='dotbox')
        for number in range(1,100,1):   #Add sample list
            self.content.listbox_widget.insert(number, f"Item {number}")
        self.content.listbox_widget.grid(column=1, row=3, sticky='nwes')

    def add_list_options(self):
        "Adds list control options to the sub-window containing a list."
        self.content.list_options = List_Options(self.menubar)

    def add_calendar(self):
        """Adds a calendar to the sub-window."""
        calendar = Calendar(master=self.sub_window_frame)
        calendar.grid(column=1, row=3, sticky='nwes')

    def add_image(self):
        """Adds an image to the sub-window. Will have a file parameter that will be user provided, either directly or accessed dynamically."""
        sample_image = Image.open("C:/Users/User/Documents/Programming/Git repository 1/Sample image futuristic.png")
        resized_sample_image = sample_image.resize((self.window_width - 20, self.window_height - 20))
        sample_photoimage = ImageTk.PhotoImage(
            image=resized_sample_image, 
            )
        label = tk.Label(
            master=self.sub_window_frame, 
            image=sample_photoimage)
        label.grid(column=1, row=3)
        self.content.pil_image = sample_image
        self.content.photoimage = sample_photoimage
        self.content.label = label
        

        
    def add_scrollbars(self):
        """Adds vertical and horizontal scrollbars. Scrollbars will be present in all sub windows when necessary. Scrollbars will automatically
        appear when the content of the sub window exceeds the size of the sub window, such that part of it is obscured. Because scrollbars are
        a property of all sub_windows, it should be placed as an attribute of the Sub_Window class. The function will be called whenever
        scrollbars are necessary. Another function, remove_scrollbars, will remove them when unecessary."""
        
    def remove_scrollbars(self):
        """"""
        
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
        window0,
        width=screen_width,
        height=screen_height,
        bg='black')
    canvas.grid(column=0, row=0)
    return canvas


def create_sub_windows(window0: tk.Tk, canvas0: tk.Canvas) -> list[tk.Frame]:
    """Creates an empty sub_window."""
    def create_basic_widgets(title: str, type: str, canvas0: tk.Canvas):
        """Generates the basic widgets that make up a sub-window. These are widgets that will be present in all sub-windows."""
        window = Sub_Window(
            type,
            title,
            canvas0,
            window0)  # The basic widgets of a sub window are already attributes of a sub-window object.
        # Therefore, they are automatically generated, configured, and placed,
        # upon creation of the sub-window object.
        return window

    # There will be multiple functions that create window content. There will be code that uses the title of the sub-window to determine which function to use.
    # create_window_content is the function that will house the sub functions and the code that will determine which of these sub-functions is used.
    # Since all the sub-window types to be used in the program are known, the
    # sub-functions and their triggers will be hardcoded.

    def create_window_content(window: Sub_Window, list: list):
        """Fills subwindow with list items, list options, sort and filter options, scroll bars, calendar, image, etc. Content depends on the sub-windows title.  """
        # Code to determine whether sub_Window will contain lists, calendar, or image. For this. the Sub_Window class can have an attribute
        # will tell which of these options is the case. The attribute will be called type. Three possible definitions for the attribute are
        # strings, corresponding to List, Calendar, or Image, respectively.
        # list_control_options = List_Control_Options(window.menubar)
        # content = Sub_Window_Content(list, listbox, window.menubar, list_control_options)
        # window.content = content
        if window.type == "List":
            window.add_list()
            window.add_list_options()
            window.add_scrollbars()
        elif window.type == "Calendar":
            """Add calendar"""
            window.add_calendar()
        elif window.type == "Image":
            """Add Image"""
            window.add_image()
    def configure_layout(window: Sub_Window):
        """Configures layout of widgets within a sub window."""
        # Default widgets layout done upon creation of object. Additional
        # widgets depending of type of sub-window to be configured separately.

    def place_widgets(window: Sub_Window):
        """"""
        # Default widgets placed upone creation of the sub-window. Additional
        # widgets placed depending on type of sub-window.

        window.content.list_options.sort_menubutton.grid(
            column=0, row=0, sticky='w')
        window.content.list_options.filter_menubutton.grid(column=0, row=0)

    def create_window(
            window0: tk.Tk,
            canvas0: tk.Canvas,
            title: str,
            type: str) -> tk.Frame:
        """Creates a sub-window. Runs other sub-functions depending on the type of subwindow."""
        window = create_basic_widgets(title, type, canvas0)
        create_window_content(window, next_actions_list)
        configure_layout(window)
        place_widgets(window)
        return window

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
    windows = [
        next_actions_window,
        upcoming_events_window,
        ticklers_window,
        outcomes_window,
        waiting_for_window,
        calendar_window,
        image_window]
    return windows


def event_handling(window: Sub_Window):
    """"""
    # Widget-event-handler binds
 # Will using lambda functions to call all event handlers, in order to use window as an argument in each of them. This will enable easy access
 # of the window object attributes.
    window.sub_window_frame.bind(
        "<Button-1>",
        lambda event: lift_window(
            event,
            window))
    window.top_frame.bind(
        "<Button-1>",
        lambda event: enable_drag(
            event,
            window))
    window.top_frame.bind(
        "<Button-1>",
        lambda event: lift_window(
            event,
            window),
        add='+')
    window.top_frame.bind(
        "<ButtonRelease>",
        lambda event: disable_drag(
            event,
            window))
    window.top_frame.bind(
        "<Motion>",
        lambda event: execute_drag(
            event,
            window))
    window.title_label.bind(
        "<Button-1>",
        lambda event: enable_drag(
            event,
            window))
    window.title_label.bind(
        "<Button-1>",
        lambda event: lift_window(
            event,
            window),
        add='+')
    window.title_label.bind(
        "<ButtonRelease>",
        lambda event: disable_drag(
            event,
            window))
    window.title_label.bind(
        "<Motion>",
        lambda event: execute_drag(
            event,
            window))
    if window.type != "Calendar":
        window.border_frame_E.bind(
            "<Button-1>",
            lambda event: enable_drag(
                event,
                window))
        window.border_frame_E.bind(
            "<Button-1>",
            lambda event: lift_window(
                event,
                window),
            add='+')
        window.border_frame_E.bind(
            "<ButtonRelease>",
            lambda event: disable_drag(
                event,
                window))
        window.border_frame_E.bind(
            "<Motion>", lambda event: resize_right(
                event, window))
        window.border_frame_S.bind(
            "<Button-1>",
            lambda event: enable_drag(
                event,
                window))
        window.border_frame_S.bind(
            "<Button-1>",
            lambda event: lift_window(
                event,
                window),
            add='+')
        window.border_frame_S.bind(
            "<ButtonRelease>",
            lambda event: disable_drag(
                event,
                window))
        window.border_frame_S.bind(
            "<Motion>", lambda event: resize_bottom(
                event, window))
        window.corner_frame_SE.bind(
            "<Button-1>",
            lambda event: enable_drag(
                event,
                window))
        window.corner_frame_SE.bind(
            "<Button-1>",
            lambda event: lift_window(
                event,
                window),
            add='+')
        window.corner_frame_SE.bind(
            "<ButtonRelease>",
            lambda event: disable_drag(
                event,
                window))
        window.corner_frame_SE.bind(
            "<Motion>", lambda event: resize_corner(
                event, window))


def ui_manager():
    "Manages UI."
    window0 = create_root_window()
    canvas0 = create_root_canvas(window0)
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

### Event Handlers ##################################


def lift_window(button1_press: tk.Event, window: Sub_Window):
    """Upon a sub-window being clicked with left mouse button at any point within it, the event handler lifts the clicked sub-window to top of stack."""
    ID = window.canvas_window0_ID
    canvas = window.canvas
    window.sub_window_frame.lift(aboveThis=None)
    canvas.tag_raise(ID)


def enable_drag(button1_press: tk.Event, window: Sub_Window):
    """"Returns True when mouse button 1 is pressed in binded widget. """
    window.drag_enabled = True
    window.button1_press_coords = button1_press.x, button1_press.y


def disable_drag(button1_release: tk.Event, window: Sub_Window):
    """Returns False when mouse button 1 is released over the binded widget. """
    window.drag_enabled = False


def execute_drag(mouse_motion: tk.Event, window: Sub_Window):
    """Called when motion detected in binded frame, and drag_status == True."""
    # Initial position values of mouse pointer (relative widget (upper left
    # coner of the widget))
    x1, y1 = window.button1_press_coords[0], window.button1_press_coords[1]
    if window.drag_enabled:
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
        window.canvas.move(window.canvas_window0_ID, delta_x, delta_y)


def resize_right(motion: tk.Event, window: Sub_Window):
    """Changes the width of the sub_window based on the change in position of the mouse cursor. Assuming the width will increase both to
            the left and to the right, the sub-window position will change in response to the change in
            position of the mouse cursor, so as to make it seem that only the right side of the window is being resized."""
    if window.drag_enabled:
        x1 = window.button1_press_coords[0]
        x2 = motion.x
        delta_cursor = x2 - x1  # Horizontal change in position of mouse cursor
        x1 = x2
        delta_window = window.window_width + delta_cursor
        #delta_top_frame = window.top_frame.winfo_width() + delta_cursor
        #delta_border_frame_N = window.border_frame_N.winfo_width() + delta_cursor
        #delta_border_frame_S = window.border_frame_S.winfo_width() + delta_cursor
        #############
        # Add code to verify whether the sort and menu buttons are present in
        # the sub-window
        #delta_menubar = window.menubar.winfo_width() + delta_cursor
        ##############
        # Imposes minimum width to sub-window (measured in pixels)
        if delta_window > 130:
            window.window_width = delta_window
            window.update_size()
            #window.top_frame.configure(width=delta_top_frame)
            #window.border_frame_N.configure(width=delta_border_frame_N)
            #window.border_frame_S.configure(width=delta_border_frame_S)
        if delta_window < 205:
            window.menubar.grid_remove()
        elif delta_window > 205:
            if window.menubar.winfo_manager() == "" and window.window_height > 56:
                window.menubar.grid()
            #window.menubar.configure(width=delta_menubar-4)

    #print("BFE width: ", window.border_frame_E.winfo_width())
    #print("CFSW width: ", window.corner_frame_SW.winfo_width())
    print("Window width: ", window.window_width)
    print("Subw window frame width: ", window.sub_window_frame.winfo_height())
    #print("Menubar width: ", window.menubar.winfo_width())

def resize_bottom(motion: tk.Event, window: Sub_Window):
    """Changes the height of the sub-window based on the change in position of the mouse cursor. Assuming both the top and the
    bottom of the sub-window will adjust for the change in height, the position of the sub-window will adjust also, in order to
    make it seem that only the buttom of the sub-screen is changing to adjust for the change in height."""
    if window.drag_enabled:
        y1 = window.button1_press_coords[1]
        y2 = motion.y
        # Vertical change in position of mouse cursor in the subwindow frame
        delta_cursor = y2 - y1
        y1 = y2
        delta_window = window.window_height + delta_cursor
        #delta_border_frame_W = window.border_frame_W.winfo_height() + delta_cursor
        #delta_border_frame_E = window.border_frame_E.winfo_height() + delta_cursor

        # Add code to verify whether the sort and menu buttons are present in
        # the sub-window

        #############

        if delta_window > 31:   #Imposes minimum width to the sub_window, so that the top frame remains visible. 
            window.window_height = delta_window
            window.update_size()
            #window.border_frame_W.configure(height=window.window_height - 4)
            #window.border_frame_E.configure(height=window.window_height - 4)
        if window.window_height < 56: #Removes menubar once a minimum window height is reached, to enable uninterrupted resizing. 
            #window.menubar.configure(height=0)
            window.menubar.grid_remove()
        elif window.window_height > 56:
            if window.menubar.winfo_manager() == "" and window.window_width > 205:
                window.menubar.grid()
            #window.menubar.configure(height=25)
            
    print("Window height: ", window.window_height)
    #print("Menubar height: ", window.menubar.winfo_height())
    #print("Border frame east height: ", window.border_frame_E.winfo_height())
    #print("Border frame west height: ", window.border_frame_W.winfo_height())
        #################

def resize_corner(motion: tk.Event, window: Sub_Window):
    """Uses functions resize bottom and resize right at the same time when user clicks and drags from SW corner of window"""
    if window.drag_enabled:
        resize_right(motion, window)
        resize_bottom(motion, window)


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
