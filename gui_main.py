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
7) AAAAAHHHH FUCK
"""

import tkinter as tk
from tkinter import ttk

"""Class that allows for editing treeview stuff, need to fix it from bugging out in fullscreen or just remove fullscreen entirely"""
class TreeEdit(ttk.Treeview):

    HORIZONAL_OFFSET = 305
    VERTICAL_OFFSET = 10

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.bind("<Double-1>", self.double_click)
        self.bind("<<TreeviewSelect>>", self.selected_row)

    def selected_row(self, event):
        self.bind("<Delete>", self.delete_row)
        self.bind("<Up>", self.up_select)
        self.bind("<Down>", self.down_select)
        self.bind("<Escape>", self.deselect)

    def delete_row(self, event):
        row = self.selection()[0]
        self.delete(row)

    def up_select(self, event):
        rows = self.selection()
        for row in rows:
            self.move(row, self.parent(row), self.index(row))

    def down_select(self, event):
        rows = self.selection()
        for row in rows:
            self.move(row, self.parent(row), self.index(row))

    def deselect(self, event):
        if len(self.selection()) > 0:
            self.selection_remove(self.selection()[0])



    def double_click(self, event):
        try:
            region = self.identify_region(event.x, event.y)
            
            if region not in ("tree", "cell"):
                return

            column = self.identify_column(event.x)
            self.column_index = int(column[1:]) - 1

            value = self.item(self.focus())
            self.id = self.focus()
            if column == '#0':
                selected_values = value.get("text") 
            else:
                selected_values = value.get("values")[self.column_index]
            
            cell = self.bbox(self.id,column)
            self.entry = ttk.Entry(root, width=cell[2])
        
            self.entry.insert(0, selected_values)
            self.entry.select_range(0, tk.END)
            self.entry.focus()

            self.entry.bind("<FocusOut>", self.focus_out)
            self.entry.bind("<Return>", self.enter)
            self.entry.bind("<Escape>", self.escape)
            
            self.entry.place(
                x=cell[0]+ self.HORIZONAL_OFFSET,
                y=cell[1]+ self.VERTICAL_OFFSET,
                w=cell[2],
                h=cell[3]
            )
        
        except IndexError:
            return 0

    def focus_out(self, event):
        event.widget.destroy()

    def enter(self, event):
        text = event.widget.get()
        values_current = self.item(self.id).get("values")
        values_current[self.column_index] = text
        self.item(self.id, values=values_current)
        event.widget.destroy()
    
    def escape(self, event):
        text = event.widget.get()
        values_current = self.item(self.id).get("values")[self.column_index]=text
        event.widget.destroy()


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

        # Initialize table frame
        self.table_frame = ttk.Frame(self.frame)
        self.table_frame.grid(row=0, column=1, padx=20, pady=10)

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
        self.has_saves = tk.BooleanVar()
        self.death_saves = ttk.Checkbutton(self.entry_frame, text="Death Saves", variable=self.has_saves)
        self.death_saves.grid(row=7, column=0, sticky="ew")

        # Insert Button
        self.insert_button = ttk.Button(self.entry_frame, text="Insert", command=self.insert_button)
        self.insert_button.grid(row=9, columnspan=2, column=0, sticky="ew")

        # Roll Button
        self.roll_button = ttk.Button(self.entry_frame, text="ROLL")
        self.roll_button.grid(row=10, columnspan=2, column=0, sticky="ew")

        #Tree Table
        table_scroll = ttk.Scrollbar(self.table_frame)
        table_scroll.pack(side="right", fill="y")

        cols = ("turn", "name", "initiative", "ac", "hp", "thp", "damage", "healing", "death_saves")
        self.table_view = TreeEdit(self.table_frame, show="headings", yscrollcommand=table_scroll.set, columns=cols, height=13)


        self.table_view.column("turn", width=50)
        self.table_view.column("name", width=150)
        self.table_view.column("initiative", width=100)
        self.table_view.column("ac", width=70)
        self.table_view.column("hp", width=70)
        self.table_view.column("thp", width=70)
        self.table_view.column("damage", width=70)
        self.table_view.column("healing", width=70)
        self.table_view.column("death_saves", width=70) 

        self.table_view.pack()
        table_scroll.config(command=self.table_view.yview)

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


    def insert_button(self):
        
        if self.has_saves.get():
            death_saves = "3/3"
        else:
            death_saves = "N/A"

        creature_values = (
        "",
        self.name_entry.get(),
        "0",
        self.ac_entry.get(),
        self.hp_entry.get(),
        self.thp_entry.get(),
        "0",
        "0",
        death_saves
        )

        self.insert_row(creature_values)


    def insert_row(self, creature_values):
        self.table_view.insert(
            "",
            tk.END,
            text="",
            values = creature_values
        )



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