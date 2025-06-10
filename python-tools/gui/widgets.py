import tkinter as tk

def labeled_entry(parent, label_text):
    frame = tk.Frame(parent)
    label = tk.Label(frame, text=label_text)
    entry = tk.Entry(frame)
    label.pack(side="left")
    entry.pack(side="right", fill="x", expand=True)
    frame.pack(fill="x", padx=10, pady=5)
    return entry
