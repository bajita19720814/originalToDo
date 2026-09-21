import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from ui.listview import ListView
from color import colors

class TaskForm(tk.Tk):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.title("タスク入力")
        
        self.task_var = tk.StringVar()
        self.before_var = tk.IntVar(value=0)
        self.repeat_var = tk.StringVar(value="なし")
        self.color_var = tk.IntVar(value=0)
        screen_w = self.winfo_screenwidth() 
        screen_h = self.winfo_screenheight() 
        self.x = screen_w - 330 
        self.y = screen_h - 300
        self.geometry(f"300x212+{self.x}+{self.y}")
        ttk.Label(self, text="タスク名", font=("Arial", 10)).grid(row=0, column=0, pady=5)
        ttk.Entry(self, textvariable=self.task_var, width=20, font=("Arial", 12)).grid(row=0, column=1, pady=5)
        
        ttk.Label(self, text="日付", font=("Arial", 10)).grid(row=1, column=0, pady=5)
        self.date_entry = DateEntry(self, width=27, date_pattern="yyyy-mm-dd")
        self.date_entry.grid(row=1, column=1, pady=5)

        ttk.Label(self, text="事前表示", font=("Arial", 10)).grid(row=2, column=0, pady=5)
        befor_frame = ttk.Frame(self)
        befor_frame.grid(row=2, column=1, pady=5)
        ttk.Spinbox(befor_frame, from_=0, to=10, textvariable=self.before_var).pack(side="left")
        ttk.Label(befor_frame, text="日前", font=("Arial", 8)).pack(side="left")

        ttk.Label(self, text="繰り返し", font=("Arial", 10)).grid(row=3, column=0, pady=5)
        repeat_frame = ttk.Frame(self)
        repeat_frame.grid(row=3, column=1, pady=5)
        choices = ["なし", "あり"]
        for choice in choices:
            ttk.Radiobutton(repeat_frame, text=choice, variable=self.repeat_var, value=choice).pack(side=tk.LEFT, padx=20) 

        def chose_color():
            selectcolor = tk.Toplevel(self)
            selectcolor.geometry(f"80x160+{self.x - 80}+{self.y}")
            selectcolor.title("カラー選択")
            def setcolor(i):
                def x():
                    self.color_var.set(i)
                    self.btn.config(bg=colors[i][0])
                    selectcolor.destroy()
                return x
            for i in range(6):
                button = tk.Button(selectcolor, bg=colors[i][0], width=15, command=setcolor(i))
                button.pack()
        ttk.Label(self, text="テーマカラー", font=("Arial", 10)).grid(row=4, column=0, pady=5)
        self.btn = tk.Button(self, text="色を選んでください", font=("Arial", 10), command=chose_color)
        self.btn.grid(row=4, column=1, pady=5)

        tk.Button(self, text="　登　録　", font=("Arial", 10), command=self.save).grid(row=6, column=0, pady=5)
        tk.Button(self, text="登録タスクの表示", font=("Arial", 10), command=self.showlist).grid(row=6, column=1, pady=5)        

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_rowconfigure(2, weight=1)
        # self.grid_rowconfigure(3, weight=1)
        # self.grid_rowconfigure(4, weight=1)
        # self.grid_rowconfigure(5, weight=3)
        # self.grid_rowconfigure(6, weight=1)

        self.configure(padx=12)
        self.after(200, self.iconify)  # 0.2秒後に最小化


    def reset_form(self):
        self.task_var.set("")
        self.before_var.set(0)
        self.repeat_var.set("なし")
        self.color_var.set(0)
        self.btn.config(bg="white")

    def save(self):
        data = (
            self.task_var.get(),
            self.date_entry.get_date(),
            self.before_var.get(),
            self.repeat_var.get(),
            self.color_var.get()
        )
        self.db.add_task(data)
        self.reset_form()
        
    def showlist(self):
       ListView(self, self.db, self.x, self.y)
