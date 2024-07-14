import tkinter as tk

from LeleEasyTkinter.easy_auto_window import EasyAutoWindow
from LeleEasyTkinter.easy_button import EasyButton
from LeleEasyTkinter.easy_fade_animation import fade_in, fade_out
from LeleEasyTkinter.easy_frame import EasyFrame
from LeleEasyTkinter.easy_label import EasyLabel
from LeleEasyTkinter.easy_multi_text import EasyMultiText

from cryptography_app.app_window.instructions_window import InstructionsWindow
from cryptography_app.app_window.settings_window.settings_window import SettingsWindow, check_and_create_file, \
    resource_path

check_and_create_file("instructions_settings.txt", "~", "开")
instructions_settings = resource_path('instructions_settings.txt')


class CryptographyWindow:
    def __init__(self):
        self._window = tk.Tk()
        self._settings_num = 0
        self._instructions_num = 0
        self._settings_win = None
        self._instructions_win = None

    def _encryption(self):
        pass

    def _decryption(self):
        pass

    def _quit_window(self):
        if self._settings_num == 1:
            self._settings_win.on_settings_window_close()
        if self._instructions_num == 1:
            self._instructions_win.on_instructions_window_close()
        fade_out(self._window)

    def settings_num_sub(self):
        self._settings_num -= 1

    def instructions_num_sub(self):
        self._instructions_num -= 1

    def _settings(self):
        if self._settings_num != 1:
            self._settings_num += 1
            # print(f"before settings_num = {self._settings_num}")
            self._settings_win = SettingsWindow(self._window, self)
            self._settings_win.run()
            # print(f"after settings_num = {self._settings_num}")
        else:
            self._settings_win.center()

    def _instructions(self):
        if self._instructions_num != 1:
            self._instructions_num += 1
            self._instructions_win = InstructionsWindow(self._window, self)
            self._instructions_win.run()
        else:
            self._instructions_win.center()

    def _layout_pack(self):
        EasyAutoWindow(self._window, window_title="cryptography", minimum_value_x=640, minimum_value_y=870)

        f1 = EasyFrame(self._window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
        f11 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
        f12 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
        f13 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
        f14 = EasyFrame(f1, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES).get()

        f2 = EasyFrame(self._window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
        f21 = EasyFrame(f2, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
        f22 = EasyFrame(f2, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
        f23 = EasyFrame(f2, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
        f24 = EasyFrame(f2, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES).get()

        EasyLabel(f11, text="要加密的文本:", side=tk.LEFT)
        encryption_text_need = EasyMultiText(f11, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)

        EasyLabel(f12, text="加密时的密钥:", side=tk.LEFT)
        key_text = EasyMultiText(f12, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
        key_text.get_text().config(state="disabled")

        EasyLabel(f13, text="加密后的文本:", side=tk.LEFT)
        encryption_text_after = EasyMultiText(f13, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
        encryption_text_after.get_text().config(state="disabled")

        EasyButton(f14, text="加密", fill=tk.BOTH, side=tk.TOP, expand=tk.YES, height=2, cmd=self._encryption)

        EasyLabel(f21, text="要解密的文本:", side=tk.LEFT)
        decryption_text_need = EasyMultiText(f21, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)

        EasyLabel(f22, text="解密时的密钥:", side=tk.LEFT)
        key_text_need = EasyMultiText(f22, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)

        EasyLabel(f23, text="解密后的文本:", side=tk.LEFT)
        decryption_text_after = EasyMultiText(f23, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
        decryption_text_after.get_text().config(state="disabled")

        EasyButton(f24, text="解密", fill=tk.BOTH, side=tk.TOP, expand=tk.YES, height=2, cmd=self._decryption)

        EasyButton(self._window, text="退出", fill=tk.BOTH, expand=tk.YES, side=tk.LEFT, height=2,
                   cmd=self._quit_window)

        EasyButton(self._window, text="设置", fill=tk.BOTH, expand=tk.YES, side=tk.LEFT, height=2, cmd=self._settings)

        EasyButton(self._window, text="使用方法", fill=tk.BOTH, expand=tk.YES, side=tk.LEFT, height=2,
                   cmd=self._instructions)

    def run(self):
        self._layout_pack()
        fade_in(self._window)
        with open(instructions_settings, 'r', encoding='utf-8') as file:
            auto_open_instructions_window = file.read()
        if auto_open_instructions_window == "开":
            self._instructions()

        self._window.protocol("WM_DELETE_WINDOW", self._quit_window)
        self._window.mainloop()
