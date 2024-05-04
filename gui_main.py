#Main gui for the tracker
#Main gui for the tracker
"""
TO-DO: 
1) Get styles working
2) Get NPC and PC widgets working
3) Add padding
4) Add some input limitations
5) Add seperators  
6) CSV support
7) Get Treeview frame working "I can do this one"
8) AAAAAHHHH FUCK
"""

import tkinter as tk
from tkinter import ttk

class Gui_Main:
    def __init__(self, root):
        self.root = root
        self.root.title("")

        # Create main frame
        self.frame = ttk.Frame(root)
        self.frame.pack()

        # Initialize entry frame
        self.entry_frame = ttk.LabelFrame(self.frame, text="Enter Creature")
        self.entry_frame.grid(row=0, column=0, padx=20, pady=10)

        self.setup_widgets()

    def setup_widgets(self):
        # Create and place all widgets
        self.name_entry = self.create_entry(self.entry_frame, "Name", "---", 1)
        self.ac_entry = self.create_entry(self.entry_frame, "AC", "0", 2)
        self.hp_entry = self.create_entry(self.entry_frame, "HP", "0", 3)
        self.mod_entry = self.create_entry(self.entry_frame, "Initiative Modifier", "0", 4)

        # Temporary HP entry and label
        self.thp_entry = ttk.Entry(self.entry_frame)
        self.thp_label = ttk.Label(self.entry_frame, text="Temporary HP")
        self.thp_space = ttk.Label(self.entry_frame, text="")
        self.thp_space.grid(row=5, column=0, pady=1, sticky="ew")

        # Checkbox for Temporary HP
        self.has_thp = tk.BooleanVar()
        self.thp_checkbutton = ttk.Checkbutton(self.entry_frame, text="Temporary HP", variable=self.has_thp, command=self.add_thp_entry)
        self.thp_checkbutton.grid(row=6, column=0, sticky="ew")

        # Dropdown for status
        self.status_type = ttk.Combobox(self.entry_frame, values=["NPC", "PC"])
        self.status_type.current(0)
        self.status_type.grid(row=6, column=1, sticky="ew")
        self.status_type.bind("<<ComboboxSelected>>", self.status_widgets)

        # Death Saves Checkbutton
        self.death_saves = ttk.Checkbutton(self.entry_frame, text="Death Saves")
        self.death_saves.grid(row=7, column=0, sticky="ew")

        # Buttons
        self.insert_button = ttk.Button(self.entry_frame, text="Insert")
        self.insert_button.grid(row=9, columnspan=2, column=0, sticky="ew")

        self.roll_button = ttk.Button(self.entry_frame, text="ROLL")
        self.roll_button.grid(row=10, columnspan=2, column=0, sticky="ew")

    def create_entry(self, frame, label_text, initial_text, row):
        label = ttk.Label(frame, text=label_text)
        label.grid(row=row, column=0, sticky="ew")
        entry = ttk.Entry(frame)
        entry.insert(0, initial_text)
        entry.bind("<FocusIn>", lambda e, entry=entry: entry.delete(0, 'end'))
        entry.grid(row=row, column=1, sticky="ew")
        return entry

    def add_thp_entry(self):
        if self.has_thp.get():
            self.thp_label.grid(row=5, column=0, sticky="ew")
            self.thp_entry.grid(row=5, column=1, sticky="ew")
            self.thp_space.grid_remove()
        else:
            self.thp_space.grid(row=5, column=0, sticky="ew")
            self.thp_entry.grid_remove()
            self.thp_label.grid_remove()

    def status_widgets(self, event=None):
        status = self.status_type.get()
        if status == "NPC":
            self.death_saves.grid()
        elif status == "PC":
            self.death_saves.grid_remove()

    """
    callback to ensure certain entries are integers only.
    not in use right now 
    """
    def callback(input):
        if str.isdigit(input) or input =="":
            return True
        else:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = Gui_Main(root)
    root.mainloop()