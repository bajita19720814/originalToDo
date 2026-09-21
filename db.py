import os
import sys
import sqlite3
from datetime import datetime, timedelta

def get_db_path():
    if getattr(sys, "frozen", False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.dirname(__file__)
    return os.path.join(base, "tasks.db")

class TaskDB:
    def __init__(self, path=get_db_path()):
        self.conn = sqlite3.connect(path)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            due_date TEXT,
            visible_from INT,
            repeat_rule TEXT,
            theme_color INTEGER,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """)
        self.conn.commit()

    def add_task(self, data):
        self.conn.execute("""
            INSERT INTO tasks (title, due_date, visible_from, repeat_rule, theme_color)
            VALUES (?, ?, ?, ?, ?)
        """, data)
        self.conn.commit()

    def pull_data(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, title, due_date, visible_from, repeat_rule FROM tasks")
        return cur.fetchall()
    
    def pull_tasks(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, title, due_date, visible_from, repeat_rule, theme_color FROM tasks")
        rows = cur.fetchall()
        tasks = []
        for row in rows:
            notice = datetime.strptime(row[2], "%Y-%m-%d")
            run_date = notice - timedelta(days=(row[3]))

            if run_date > datetime.now():
                continue

            tasks.append(row)
        return tasks


    def delete_item(self, item):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM tasks WHERE id = ?", (item,))
        self.conn.commit()

    def repeat_task(self, item, date):
        cur = self.conn.cursor()
        cur.execute("UPDATE tasks SET due_date = ? WHERE id = ?", (date, item))
        self.conn.commit()