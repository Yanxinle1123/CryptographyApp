import json
import os
import tkinter as tk

from LeleEasyTkinter.easy_mobile_animation import move_window_to


def replace(text_box, text):
    text_box.get_text().config(state="normal")
    text_box.get_text().delete("1.0", tk.END)
    text_box.get_text().insert(tk.END, text)
    text_box.get_text().config(state="disabled")


def center_window(root):
    width = root.winfo_width()
    height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2 - 20

    root.focus_set()
    root.lift()
    move_window_to(root, x, y, 100, 0.05)


def config_write(config_map, json_file, indent=2):
    with open(json_file, "w") as file:
        json.dump(config_map, file, indent=indent)


def config_read(json_file, default_config_map=None):
    if default_config_map is None:
        default_config_map = {}

    if not os.path.exists(json_file):
        with open(json_file, 'w') as file:
            file.write(default_config_map)

    with open(json_file, "r") as file:
        return json.load(file)
