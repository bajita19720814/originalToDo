from ui.form import TaskForm
from db import TaskDB
from ui.notify import Popup
from concurrent.futures import ProcessPoolExecutor
import os

def load_tasks(app, db):
    tasks = db.pull_tasks()

    with ProcessPoolExecutor(max_workers=os.cpu_count()):
        for i, task in enumerate(tasks):
            Popup(app, db, i, task[0], task[1], task[2], task[4], task[5])        


def main():
    db = TaskDB()
    app = TaskForm(db)
    load_tasks(app, db)
    app.mainloop()

if __name__ == "__main__":
    main()