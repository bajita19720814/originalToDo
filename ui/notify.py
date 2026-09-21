import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import DateEntry
from color import colors

class Popup():
    def __init__(self, app, db, index, id, title, due_date, repeat_rule, theme_color):
        super().__init__()
        self.toplebel = tk.Toplevel(app, bg="white")
        self.toplebel.overrideredirect(True)
        self.toplebel.attributes("-topmost", True)
        self.toplebel.attributes("-alpha", 0.9)
        self.toplebel.wm_attributes("-transparentcolor", "white")
        self.id = id
        self.repeat = False if repeat_rule == "なし" else True
        self.bg = colors[int(theme_color)][0]
        self.btn_color = colors[int(theme_color)][1]
        self.fg = colors[int(theme_color)][2]
        self.db = db
       
        screen_w = self.toplebel.winfo_screenwidth() 
        
        width, height = 200, 74 
        x = screen_w - width - 8 
        y = height * index + 8 * (index +1)
        self.toplebel.geometry(f"{width}x{height}+{x}+{y}") 

        frame = ctk.CTkFrame(self.toplebel, corner_radius=30, fg_color=self.bg, border_color=self.btn_color, border_width=3) 
        frame.pack(fill="both", expand=True)


        self.task_frame = tk.Frame(frame, bg=self.bg)
        self.task_frame.pack(side="left", padx=8)
        title_label = tk.Label(self.task_frame, bg=self.bg, text=title, font=("Meiryo", 10, "bold"), fg=self.fg)
        title_label.pack()
        self.date_label = tk.Label(self.task_frame, bg=self.bg, text=due_date, font=("Meiryo", 10, "bold"), fg=self.fg)
        self.date_label.pack(pady=0)
        self.btn_frame = tk.Frame(frame, bg=self.bg)
        self.btn_frame.pack(side="right", padx=10)
        def done():
            if messagebox.askokcancel(title="確認", message="本当に削除しますか"):
                self.db.delete_item(self.id)
                self.toplebel.destroy()
        done_button = ctk.CTkButton(self.btn_frame, fg_color=self.btn_color, text="完了", width=35, font=("Meiryo", 8, "bold"), corner_radius=5, text_color=self.fg, command=done)
        done_button.pack(side="top", padx=0, pady=2)
            
        def repeat():
            repeat_date = tk.Toplevel(app)
            repeat_date.attributes("-topmost", True)
            repeat_date.geometry(f"100x74+{screen_w - 330}+20")
            tk.Label(repeat_date, text="日にちを選ぶ", font=("Arial", 10)).pack()
            def comform(d):
                def x():
                    self.db.repeat_task(self.id, d.get_date())
                    repeat_date.destroy()
                    self.toplebel.destroy()
                return x
            date_entry = DateEntry(repeat_date, width=27, date_pattern="yyy-mm-dd")
            date_entry.pack()
            comform_button = tk.Button(repeat_date, text="決定する", font=("Arial", 10), command=comform(date_entry))
            comform_button.pack()
        if self.repeat == True:
            repeat_button = ctk.CTkButton(self.btn_frame, fg_color=self.btn_color, text="繰り返し", width=35, font=("Meiryo", 8, "bold"), corner_radius=5, text_color=self.fg, command=repeat)
            repeat_button.pack(side="bottom", padx=0, pady=2)