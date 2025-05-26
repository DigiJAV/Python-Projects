import tkinter as tk
from tkinter import ttk

class GTDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Getting Things Done")
        self.root.geometry("1200x800")

        self.create_address_bar()
        self.create_main_controls()
        self.create_main_layout()

    def create_address_bar(self):
        address_bar = tk.Frame(self.root, bg="lightgray", height=30)
        address_bar.pack(fill=tk.X, side=tk.TOP)

        tk.Button(address_bar, text="⬅").pack(side=tk.LEFT)
        tk.Button(address_bar, text="➡").pack(side=tk.LEFT)
        tk.Label(address_bar, text="🏠 Home", bg="lightgray").pack(side=tk.LEFT)

    def create_main_controls(self):
        controls_frame = tk.Frame(self.root)
        controls_frame.pack(fill=tk.X)

        tk.Button(controls_frame, text="Add Input", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(controls_frame, text="Files", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(controls_frame, text="Process Inbox", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(controls_frame, text="History", width=15).pack(side=tk.LEFT, padx=5)

    def create_main_layout(self):
        content_frame = tk.Frame(self.root)
        content_frame.pack(expand=True, fill=tk.BOTH)

        # Left column
        left_col = tk.Frame(content_frame)
        left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.create_list_box(left_col, "Upcoming Events", ["Event 1 | Date", "Event 2 | Date"])
        self.create_calendar_overview(left_col)
        self.create_image_box(left_col)

        # Center and right columns
        center_col = tk.Frame(content_frame)
        center_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.create_action_list(center_col, "Next Actions", ["Next Action 1", "Next Action 2", "Next Action 3"])
        self.create_action_list(center_col, "Outcomes", ["Outcome 1", "Outcome 2", "Outcome 3"])
        self.create_action_list(center_col, "Ticklers", ["Tickler 1", "Tickler 2"])

    def create_list_box(self, parent, title, items):
        frame = tk.LabelFrame(parent, text=title)
        frame.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)
        listbox = tk.Listbox(frame)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        for item in items:
            listbox.insert(tk.END, item)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)

    def create_action_list(self, parent, title, items):
        frame = tk.LabelFrame(parent, text=title)
        frame.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)

        top_row = tk.Frame(frame)
        top_row.pack(fill=tk.X)
        tk.Label(top_row, text="Options").pack(side=tk.LEFT, padx=5)
        tk.Label(top_row, text="Sort:").pack(side=tk.LEFT)
        ttk.Combobox(top_row, values=["Option 1", "Option 2"]).pack(side=tk.LEFT)
        tk.Label(top_row, text="Filter:").pack(side=tk.LEFT)
        ttk.Combobox(top_row, values=["Option 1", "Option 2"]).pack(side=tk.LEFT)

        listbox = tk.Listbox(frame)
        listbox.pack(fill=tk.BOTH, expand=True)
        for item in items:
            listbox.insert(tk.END, item)

    def create_calendar_overview(self, parent):
        frame = tk.LabelFrame(parent, text="Calendar Overview")
        frame.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)

        for row in range(6):
            for col in range(7):
                day = row * 7 + col + 1
                if day <= 31:
                    lbl = tk.Label(frame, text=str(day), borderwidth=1, relief="solid", width=3)
                    lbl.grid(row=row, column=col, padx=1, pady=1)

    def create_image_box(self, parent):
        frame = tk.LabelFrame(parent, text="Image")
        frame.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)
        tk.Label(frame, text="[Image Placeholder]").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = GTDApp(root)
    root.mainloop()
