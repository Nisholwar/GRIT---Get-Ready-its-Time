import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime
import time
import random

quotes = [
    "Keep going, you’re doing great!",
    "Discipline beats motivation!",
    "Small steps every day lead to success.",
    "Don’t give up, your future self will thank you.",
    "Stay consistent, even on tough days!"
]

tasks = []  # list of dicts: {'name': str, 'dt': datetime.datetime, 'display': str}

# Prompt for user's name at startup
user_name = None

def add_task():
    task_name = task_entry.get()
    time_str = time_entry.get()
    if not task_name or not time_str:
        messagebox.showerror("Error", "Please enter both task and time!")
        return
    def parse_time(s):
        s = s.strip().lower()
        try:
            return datetime.datetime.strptime(s, "%H:%M").strftime("%H:%M")
        except Exception:
            pass
        try:
            return datetime.datetime.strptime(s, "%H:%M").strftime("%H:%M")
        except Exception:
            pass
        digits = ''.join(ch for ch in s if ch.isdigit())
        if len(digits) in (3,4):
            if len(digits) == 3:
                h = digits[0]
                m = digits[1:]
            else:
                h = digits[:2]
                m = digits[2:]
            try:
                return datetime.time(int(h), int(m)).strftime("%H:%M")
            except Exception:
                pass
        try:
            return datetime.datetime.strptime(s.replace(' ', ''), "%I%p").strftime("%H:%M")
        except Exception:
            pass
        try:
            return datetime.datetime.strptime(s, "%I:%M%p").strftime("%H:%M")
        except Exception:
            pass

    t_norm = parse_time(time_str)
    if not t_norm:
        messagebox.showerror("Error", "Time must be in HH:MM (24-hour) format or common variants (e.g., 09:05, 9:05, 930, 9am)")
        return

    hour, minute = map(int, t_norm.split(":"))
    now = datetime.datetime.now()
    scheduled = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if scheduled < now:
        scheduled = scheduled + datetime.timedelta(days=1)

    display_str = f"{task_name.strip()} at {scheduled.strftime('%Y-%m-%d %H:%M')}"
    tasks.append({"name": task_name.strip(), "dt": scheduled, "display": display_str})
    listbox.insert(tk.END, display_str)
    task_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

def check_tasks():
    """
    Check tasks using the Tkinter main loop (root.after). This keeps GUI calls (messagebox)
    on the main thread and avoids issues that arise when invoking GUI from a background thread.
    """
    now_dt = datetime.datetime.now()
    for entry in list(tasks):
        if now_dt >= entry["dt"]:
            quote = random.choice(quotes)
            current_time = now_dt.strftime('%Y-%m-%d %H:%M:%S')
            messagebox.showinfo(
                "Reminder",
                f"Hello {user_name}!\n\nTime for: {entry['name']}\nTime: {current_time}\n\nMotivation: {quote}"
            )
            try:
                tasks.remove(entry)
            except ValueError:
                pass
            for i in range(listbox.size()):
                if listbox.get(i) == entry["display"]:
                    listbox.delete(i)
                    break
    root.after(1 * 1000, check_tasks)

# GUI setup
root = tk.Tk()
root.title("GRIT - Reminder & Motivation App")
root.geometry("400x400")

# Prompt for user's name
user_name = simpledialog.askstring("Welcome!", "Please enter your name:", parent=root)
if not user_name:
    user_name = "User"

title_label = tk.Label(root, text="💪 GRIT - Stay Consistent", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Task:").grid(row=0, column=0)
task_entry = tk.Entry(frame)
task_entry.grid(row=0, column=1)

tk.Label(frame, text="Time (HH:MM):").grid(row=1, column=0)
time_entry = tk.Entry(frame)
time_entry.grid(row=1, column=1)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white")
add_button.pack(pady=10)

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

# Start periodic check on the main thread
root.after(1000, check_tasks)

root.mainloop()
