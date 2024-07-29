import os
import sys
import tkinter as tk

from LeleEasyTkinter.easy_auto_window import EasyAutoWindow
from LeleEasyTkinter.easy_button import EasyButton
from LeleEasyTkinter.easy_check_button import EasyCheckButton
from LeleEasyTkinter.easy_drop_list import EasyDropList
from LeleEasyTkinter.easy_fade_animation import fade_in, fade_out
from LeleEasyTkinter.easy_frame import EasyFrame
from LeleEasyTkinter.easy_label import EasyLabel
from LeleEasyTkinter.easy_popup_animation import animate_resize_window
from LeleEasyTkinter.easy_warning_windows import EasyWarningWindows

from cryptography_app.common.common import center_window


def resource_path(relative_path):
    home_dir = os.path.expanduser('~')
    file_path = os.path.join(home_dir, relative_path)
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, file_path)
    return file_path


class SettingsWindow:
    def __init__(self, window, parent_window):
        # print("SettingsWindow初始化！")
        self._parent_window = parent_window
        self._window = tk.Toplevel(window)
        self._other_settings = None
        self._command = None
        self._algorithm_settings = self._parent_window.read_one_config("algorithm_settings")
        self._algorithm = None
        self._auto_save_settings_value = self._parent_window.read_one_config("auto_save_settings")
        self._auto_save_settings_value2 = self._parent_window.read_one_config("auto_save_settings2")

    def _about_keys(self):

        EasyWarningWindows(self._window, "信息", "按下q键退出\n按下F1显示使用说明").show_warning()

    def center(self):
        center_window(self._window)

    def _save_settings(self, *args):
        other_settings_set = self._other_settings.get_set()

        self._parent_window.write_one_config("algorithm_settings", self._algorithm.get_combo_value())

        if "退出设置未保存时提醒" in other_settings_set:
            self._parent_window.write_one_config("unsaved_reminder_settings", True)
        else:
            self._parent_window.write_one_config("unsaved_reminder_settings", False)

        if "加密解密出错时弹出错误提示" in other_settings_set:
            self._parent_window.write_one_config("error_prompt_settings", True)
        else:
            self._parent_window.write_one_config("error_prompt_settings", False)

        if "重置设置后自动保存" in other_settings_set:
            self._parent_window.write_one_config("auto_save_settings", True)
        else:
            self._parent_window.write_one_config("auto_save_settings", False)

        # with open(shortcut_keys_settings, 'w', encoding='utf-8') as file:
        #     if "启用快捷键" in other_settings_set:
        #         file.write("开")
        #         window.bind('<Command-comma>', lambda event: settings())
        #         window.bind('<F1>', lambda event: instructions())
        #         window.bind('<q>', lambda event: quit_window())
        #         window.bind('<Q>', lambda event: quit_window())
        #         self._window.bind('<Command-comma>', lambda event: settings())
        #         self._window.bind('<F1>', lambda event: instructions())
        #         self._window.bind('<q>', lambda event: quit_window())
        #         self._window.bind('<Q>', lambda event: quit_window())
        #         if instructions_num == 1:
        #             instructions_window.bind('<Command-comma>', lambda event: settings())
        #             instructions_window.bind('<F1>', lambda event: instructions())
        #             instructions_window.bind('<q>', lambda event: quit_window())
        #             instructions_window.bind('<Q>', lambda event: quit_window())
        #     else:
        #         file.write("关")
        #         window.unbind('<Command-comma>')
        #         window.unbind('<F1>')
        #         window.unbind('<q>')
        #         window.unbind('<Q>')
        #         self._window.unbind('<Command-comma>')
        #         self._window.unbind('<F1>')
        #         self._window.unbind('<q>')
        #         self._window.unbind('<Q>')
        #         if instructions_num == 1:
        #             instructions_window.unbind('<Command-comma>')
        #             instructions_window.unbind('<F1>')
        #             instructions_window.unbind('<q>')
        #             instructions_window.unbind('<Q>')

        if "自动保存设置" in other_settings_set:
            self._parent_window.write_one_config("auto_save_settings2", True)
        else:
            self._parent_window.write_one_config("auto_save_settings2", False)

    def on_settings_window_close(self):
        file_list = []
        obtain_list = self._other_settings.get_set()

        if self._parent_window.read_one_config("unsaved_reminder_settings"):
            file_list.append("退出设置未保存时提醒")

        if self._parent_window.read_one_config("error_prompt_settings"):
            file_list.append("加密解密出错时弹出错误提示")

        if self._parent_window.read_one_config("auto_save_settings"):
            file_list.append("重置设置后自动保存")

        # if self._parent_window.read_one_config("shortcut_keys_settings_value"):
        #     file_list.append("启用快捷键")

        if self._parent_window.read_one_config("auto_save_settings2"):
            file_list.append("自动保存设置")

        if self._parent_window.read_one_config("unsaved_reminder_settings") and obtain_list != file_list:
            result = EasyWarningWindows(self._window, "是/否", "是否保存更改？").show_warning()
            if result:
                self._save_settings()
        fade_out(self._window)
        self._parent_window.settings_num_sub()

    def _reset_settings(self):
        # global auto_save_settings_value

        # self._auto_save_settings_value = self._parent_window.read_one_config("auto_save_settings")

        result = EasyWarningWindows(self._window, "是/否", "您确定要重置设置吗？").show_warning()
        if result:
            self._algorithm.set_combo_value('自动')
            self._other_settings.set(
                ["退出设置未保存时提醒", "加密解密出错时弹出错误提示", "重置设置后自动保存", "启用快捷键",
                 "自动保存设置"])
            print(self._auto_save_settings_value2)
            if self._auto_save_settings_value2:
                print("正在保存")
                self._save_settings()
                print("保存成功")

    def _layout_pack(self):
        if self._algorithm_settings == '自动':
            self._algorithm_settings = 1
        elif self._algorithm_settings == 'AEAD':
            self._algorithm_settings = 2
        elif self._algorithm_settings == 'AES':
            self._algorithm_settings = 3
        elif self._algorithm_settings == 'Camellia':
            self._algorithm_settings = 4
        elif self._algorithm_settings == 'Fernet':
            self._algorithm_settings = 5
        elif self._algorithm_settings == 'RSA':
            self._algorithm_settings = 6
        elif self._algorithm_settings == 'Blowfish':
            self._algorithm_settings = 7
        elif self._algorithm_settings == 'CAST5':
            self._algorithm_settings = 8
        elif self._algorithm_settings == 'RC4':
            self._algorithm_settings = 9

        other_settings_set = []
        if self._parent_window.read_one_config("unsaved_reminder_settings"):
            other_settings_set.append("退出设置未保存时提醒")
        if self._parent_window.read_one_config("error_prompt_settings"):
            other_settings_set.append("加密解密出错时弹出错误提示")
        if self._parent_window.read_one_config("auto_save_settings"):
            other_settings_set.append("重置设置后自动保存")
        # if shortcut_keys_settings_value == "开":
        #     other_settings_set.append("启用快捷键")
        if self._parent_window.read_one_config("auto_save_settings2"):
            other_settings_set.append("自动保存设置")
            self._command = self._save_settings

        f1 = EasyFrame(self._window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
        f11 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
        f12 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
        f13 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
        f14 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
        f2 = EasyFrame(self._window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()

        EasyLabel(f11, text="加密算法:", side=tk.LEFT)
        self._algorithm = EasyDropList(f11,
                                       options=['自动', 'AEAD', 'AES', 'Camellia', 'Fernet', 'RSA', 'Blowfish', 'CAST5',
                                                'RC4'], default=self._algorithm_settings, side=tk.LEFT,
                                       cmd=self._command)
        EasyLabel(f11, text="*越靠上的算法越安全", side=tk.LEFT, font_size=12, text_color="gray")

        EasyLabel(f12, text="由于程序会根据密钥自动检测加密的算法来匹配解密的算法, 所以无需设置解密的算法",
                  side=tk.LEFT, font_size=12)

        self._other_settings = EasyCheckButton(f13, text=["退出设置未保存时提醒", "加密解密出错时弹出错误提示",
                                                          "重置设置后自动保存", "启用快捷键", "自动保存设置"],
                                               set_text_list=other_settings_set, master_win=self._window,
                                               expand=True,
                                               fill=tk.Y,
                                               cmd=self._command)

        EasyButton(f14, text="关于快捷键", cmd=self._about_keys, side=tk.LEFT, width=10, height=1,
                   font_size=12)

        EasyButton(f2, text="保存", expand=tk.YES, height=2, cmd=self._save_settings, side=tk.LEFT,
                   fill=tk.X)

        EasyButton(f2, text="退出", expand=tk.YES, height=2, cmd=self.on_settings_window_close, side=tk.LEFT,
                   fill=tk.X)

        EasyButton(f2, text="重置", expand=tk.YES, height=2, cmd=self._reset_settings, side=tk.LEFT,
                   fill=tk.X)

    def run(self):
        # global unsaved_reminder_settings_value, error_prompt_settings_value, auto_save_settings_value, \
        #     shortcut_keys_settings_value, auto_save_settings_value2, command, window
        EasyAutoWindow(self._window, window_title="设置", window_width_value=280, window_height_value=140,
                       adjust_x=False, adjust_y=False)

        # command = None
        # algorithm_settings = self._parent_window.read_one_config("algorithm_settings")
        #
        # if algorithm_settings == '自动':
        #     algorithm_settings = 1
        # elif algorithm_settings == 'AEAD':
        #     algorithm_settings = 2
        # elif algorithm_settings == 'AES':
        #     algorithm_settings = 3
        # elif algorithm_settings == 'Camellia':
        #     algorithm_settings = 4
        # elif algorithm_settings == 'Fernet':
        #     algorithm_settings = 5
        # elif algorithm_settings == 'RSA':
        #     algorithm_settings = 6
        # elif algorithm_settings == 'Blowfish':
        #     algorithm_settings = 7
        # elif algorithm_settings == 'CAST5':
        #     algorithm_settings = 8
        # elif algorithm_settings == 'RC4':
        #     algorithm_settings = 9

        # unsaved_reminder_settings_value = self._parent_window.read_one_config("unsaved_reminder_settings")
        # error_prompt_settings_value = self._parent_window.read_one_config("error_prompt_settings")

        # with open(shortcut_keys_settings, 'r', encoding='utf-8') as file:
        #     shortcut_keys_settings_value = file.read()

        # other_settings_set = []
        # if self._parent_window.read_one_config("unsaved_reminder_settings"):
        #     other_settings_set.append("退出设置未保存时提醒")
        # if self._parent_window.read_one_config("error_prompt_settings"):
        #     other_settings_set.append("加密解密出错时弹出错误提示")
        # if self._parent_window.read_one_config("auto_save_settings"):
        #     other_settings_set.append("重置设置后自动保存")
        # # if shortcut_keys_settings_value == "开":
        # #     other_settings_set.append("启用快捷键")
        # if self._parent_window.read_one_config("auto_save_settings2"):
        #     other_settings_set.append("自动保存设置")
        #     command = self._save_settings
        #
        # EasyAutoWindow(self._window, window_title="设置", window_width_value=280, window_height_value=140,
        #                adjust_x=False, adjust_y=False)
        #
        # f1 = EasyFrame(self._window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
        # f11 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
        # f12 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
        # f13 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
        # f14 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
        # f2 = EasyFrame(self._window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
        #
        # EasyLabel(f11, text="加密算法:", side=tk.LEFT)
        # algorithm = EasyDropList(f11,
        #                          options=['自动', 'AEAD', 'AES', 'Camellia', 'Fernet', 'RSA', 'Blowfish', 'CAST5',
        #                                   'RC4'], default=algorithm_settings, side=tk.LEFT, cmd=self._save_settings)
        # EasyLabel(f11, text="*越靠上的算法越安全", side=tk.LEFT, font_size=12, text_color="gray")
        #
        # EasyLabel(f12, text="由于程序会根据密钥自动检测加密的算法来匹配解密的算法, 所以无需设置解密的算法",
        #           side=tk.LEFT, font_size=12)
        #
        # self._other_settings = EasyCheckButton(f13, text=["退出设置未保存时提醒", "加密解密出错时弹出错误提示",
        #                                                   "重置设置后自动保存", "启用快捷键", "自动保存设置"],
        #                                        set_text_list=other_settings_set, master_win=self._window, expand=True,
        #                                        fill=tk.Y,
        #                                        cmd=command)
        #
        # EasyButton(f14, text="关于快捷键", cmd=self._about_keys, side=tk.LEFT, width=10, height=1,
        #            font_size=12)
        #
        # EasyButton(f2, text="保存", expand=tk.YES, height=2, cmd=self._save_settings, side=tk.LEFT,
        #            fill=tk.X)
        #
        # EasyButton(f2, text="退出", expand=tk.YES, height=2, cmd=self.on_settings_window_close, side=tk.LEFT,
        #            fill=tk.X)
        #
        # EasyButton(f2, text="重置", expand=tk.YES, height=2, cmd=self._reset_settings, side=tk.LEFT,
        #            fill=tk.X)

        fade_in(self._window, ms=2)
        animate_resize_window(self._window, 780, 340, 250, "ordinary", False)

        self._layout_pack()

        self._window.protocol("WM_DELETE_WINDOW", self.on_settings_window_close)

        # with open(shortcut_keys_settings, 'r', encoding='utf-8') as file:
        #     shortcut_keys_settings_value = file.read()
        #
        # if shortcut_keys_settings_value == "开":
        #     self._window.bind('<Command-comma>', lambda event: settings())
        #     self._window.bind('<F1>', lambda event: instructions())
        #     self._window.bind('<q>', lambda event: quit_window())
        #     self._window.bind('<Q>', lambda event: quit_window())
