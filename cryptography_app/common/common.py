import json
import os
import time
import tkinter as tk

from LeleEasyTkinter.easy_mobile_animation import move_window_to


def log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"调用函数 {func.__name__} 前的普通参数={args}, 字典参数={kwargs}")
        ret = func(*args, **kwargs)
        cost = time.time() - start
        print(f"调用函数 {func.__name__} 后的普通参数={args}, 字典参数={kwargs}, 耗时: {cost:.2f}s")
        return ret

    return wrapper


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
    # print(f"config_write: before config_map={config_map}\njson_file={json_file}")

    with open(json_file, "w") as file:
        json.dump(config_map, file, indent=indent)

    # print(f"config_write: after config_map={config_map}\njson_file={json_file}")


@log
def config_read(json_file, default_config_map=None, indent=2):
    # print(f"config_read: before json_file={json_file}\ndefault_config_map={default_config_map}")

    if default_config_map is None:
        default_config_map = {}

    if not os.path.exists(json_file):
        with open(json_file, 'w') as file:
            json.dump(default_config_map, file, indent=indent)

    with open(json_file, "r") as file:
        result = json.load(file)
    # print(f"config_read: after json_file={json_file}\ndefault_config_map={default_config_map}")
    return result


if __name__ == '__main__':
    print(config_read("test.json", {"a": "b"}))
