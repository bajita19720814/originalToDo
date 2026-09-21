import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

def adjust_treeview_column_width(tree):
    font = tkFont.Font()

    for col in tree["columns"]:
        # ヘッダーの幅
        header_width = font.measure(tree.heading(col)["text"])

        # データの最大幅
        max_data_width = 0
        for item in tree.get_children():
            text = tree.set(item, col)
            max_data_width = max(max_data_width, font.measure(text))

        # 余白 + 10px
        optimal_width = max(header_width, max_data_width) + 20

        tree.column(col, width=optimal_width)

class ListView():
    def __init__(self, app, db, x, y):
        super().__init__()
        self.db = db
        toplebel = tk.Toplevel(app)
        toplebel.geometry(f"800x300+{x-800}+{y-120}")
        toplebel.title("タスク一覧")
        rows = self.db.pull_data()
                
        tree = ttk.Treeview(toplebel, columns=("id", "title", "due_date", "visible_from", "repeat_rule"), show="headings")
        tree.heading("id", text="ID")
        tree.heading("title", text="タスク")
        tree.heading("due_date", text="日付")
        tree.heading("visible_from", text="表示期間")
        tree.heading("repeat_rule", text="繰り返し")


        for row in rows:
            tree.insert("", tk.END, values=row)

        tree.grid(row=0, column=0, sticky="nsew")  
        adjust_treeview_column_width(tree)      

        delete_btn = tk.Button(toplebel, text="選択行を削除", command=lambda: self.delete_selected(tree))
        delete_btn.grid(row=1, column=0, sticky="ew")

        toplebel.grid_rowconfigure(0, weight=1)
        toplebel.grid_columnconfigure(0, weight=1)

    def delete_selected(self, tree):
            selected_items = tree.selection()
            for item_iid in selected_items:
                item_id = tree.item(item_iid, "values")[0]
                tree.delete(item_iid)
                self.db.delete_item(item_id)