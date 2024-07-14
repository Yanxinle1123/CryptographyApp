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
from LeleEasyTkinter.easy_warning_windows import EasyWarningWindows

from cryptography_app.common.common import center_window

settings_num = 0


def resource_path(relative_path):
    home_dir = os.path.expanduser('~')
    file_path = os.path.join(home_dir, relative_path)
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, file_path)
    return file_path


def check_and_create_file(filename, home_dir, write):
    home_dir = os.path.expanduser(home_dir)
    file_path = os.path.join(home_dir, filename)

    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(write)


check_and_create_file("algorithm_settings.txt", "~", "自动")
check_and_create_file("instructions_settings.txt", "~", "开")
check_and_create_file("unsaved_reminder_settings.txt", "~", "开")
check_and_create_file("error_prompt_settings.txt", "~", "开")
check_and_create_file("auto_save_settings.txt", "~", "开")
check_and_create_file("auto_save_settings2.txt", "~", "开")
check_and_create_file("enable_shortcut_keys.txt", "~", "开")

cryptography_settings = resource_path('algorithm_settings.txt')
instructions_settings = resource_path('instructions_settings.txt')
unsaved_reminder_settings = resource_path('unsaved_reminder_settings.txt')
error_prompt_settings = resource_path('error_prompt_settings.txt')
auto_save_settings = resource_path('auto_save_settings.txt')
auto_save_settings2 = resource_path('auto_save_settings2.txt')
shortcut_keys_settings = resource_path('enable_shortcut_keys.txt')


class SettingsWindow:
    def __init__(self, window):
        self._window = tk.Toplevel(window)

    def _about_keys(self):

        EasyWarningWindows(self._window, "信息", "按下q键退出\n按下F1显示使用说明").show_warning()

    def _save_settings(self, *args):
        pass
        # global algorithm, other_settings, instructions_num
        #
        # other_settings_set = other_settings.get_set()
        #
        # with open(cryptography_settings, 'w', encoding='utf-8') as file_local:
        #     file_local.write(algorithm.get_combo_value())
        #
        # with open(unsaved_reminder_settings, 'w', encoding='utf-8') as file:
        #     if "退出设置未保存时提醒" in other_settings_set:
        #         file.write("开")
        #     else:
        #         file.write("关")
        #
        # with open(error_prompt_settings, 'w', encoding='utf-8') as file:
        #     if "加密解密出错时弹出错误提示" in other_settings_set:
        #         file.write("开")
        #     else:
        #         file.write("关")
        #
        # with open(auto_save_settings, 'w', encoding='utf-8') as file:
        #     if "重置设置后自动保存" in other_settings_set:
        #         file.write("开")
        #     else:
        #         file.write("关")
        #
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
        #
        # with open(auto_save_settings2, 'w', encoding='utf-8') as file:
        #     if "自动保存设置" in other_settings_set:
        #         file.write("开")
        #     else:
        #         file.write("关")

    def _on_settings_window_close(self):
        global settings_window, settings_num, unsaved_reminder_settings_value, error_prompt_settings_value, \
            auto_save_settings_value, shortcut_keys_settings_value, other_settings

        # file_list = []
        # obtain_list = other_settings.get_set()
        #
        # with open(unsaved_reminder_settings, 'r', encoding='utf-8') as file:
        #     unsaved_reminder_settings_value = file.read()
        # if unsaved_reminder_settings_value == "开":
        #     file_list.append("退出设置未保存时提醒")
        #
        # with open(error_prompt_settings, 'r', encoding='utf-8') as file:
        #     error_prompt_settings_value = file.read()
        # if error_prompt_settings_value == "开":
        #     file_list.append("加密解密出错时弹出错误提示")
        #
        # with open(auto_save_settings, 'r', encoding='utf-8') as file:
        #     auto_save_settings_value = file.read()
        # if auto_save_settings_value == "开":
        #     file_list.append("重置设置后自动保存")
        #
        # with open(shortcut_keys_settings, 'r', encoding='utf-8') as file:
        #     shortcut_keys_settings_value = file.read()
        # if shortcut_keys_settings_value == "开":
        #     file_list.append("启用快捷键")
        #
        # with open(auto_save_settings2, 'r', encoding='utf-8') as file:
        #     auto_save_settings2_value = file.read()
        # if auto_save_settings2_value == "开":
        #     file_list.append("自动保存设置")
        #
        # if unsaved_reminder_settings_value == "开" and obtain_list != file_list:
        #     result = EasyWarningWindows(self._window, "是/否", "是否保存更改？").show_warning()
        #     if result:
        #         self._save_settings()
        fade_out(self._window)
        settings_num -= 1

    def _reset_settings(self):
        global algorithm, other_settings, auto_save_settings_value

        with open(auto_save_settings, 'r', encoding='utf-8') as file:
            auto_save_settings_value = file.read()

        result = EasyWarningWindows(self._window, "是/否", "您确定要重置设置吗？").show_warning()
        if result:
            algorithm.set_combo_value('自动')
            other_settings.set(
                ["退出设置未保存时提醒", "加密解密出错时弹出错误提示", "重置设置后自动保存", "启用快捷键",
                 "自动保存设置"])
            if auto_save_settings_value == "开":
                self._save_settings()

    def run(self):
        global settings_window, settings_num, algorithm, algorithm_settings, other_settings, \
            unsaved_reminder_settings_value, error_prompt_settings_value, auto_save_settings_value, \
            shortcut_keys_settings_value, auto_save_settings_value2, command, window

        if settings_num != 1:
            settings_num += 1

            command = None

            with open(cryptography_settings, 'r', encoding='utf-8') as file:
                algorithm_settings = file.read()
            if algorithm_settings == '自动':
                algorithm_settings = 1
            elif algorithm_settings == 'AEAD':
                algorithm_settings = 2
            elif algorithm_settings == 'AES':
                algorithm_settings = 3
            elif algorithm_settings == 'Camellia':
                algorithm_settings = 4
            elif algorithm_settings == 'Fernet':
                algorithm_settings = 5
            elif algorithm_settings == 'RSA':
                algorithm_settings = 6
            elif algorithm_settings == 'Blowfish':
                algorithm_settings = 7
            elif algorithm_settings == 'CAST5':
                algorithm_settings = 8
            elif algorithm_settings == 'RC4':
                algorithm_settings = 9

            with open(unsaved_reminder_settings, 'r', encoding='utf-8') as file:
                unsaved_reminder_settings_value = file.read()

            with open(error_prompt_settings, 'r', encoding='utf-8') as file:
                error_prompt_settings_value = file.read()

            with open(auto_save_settings, 'r', encoding='utf-8') as file:
                auto_save_settings_value = file.read()

            with open(auto_save_settings2, 'r', encoding='utf-8') as file:
                auto_save_settings_value2 = file.read()

            with open(shortcut_keys_settings, 'r', encoding='utf-8') as file:
                shortcut_keys_settings_value = file.read()

            other_settings_set = []
            if unsaved_reminder_settings_value == "开":
                other_settings_set.append("退出设置未保存时提醒")
            if error_prompt_settings_value == "开":
                other_settings_set.append("加密解密出错时弹出错误提示")
            if auto_save_settings_value == "开":
                other_settings_set.append("重置设置后自动保存")
            if shortcut_keys_settings_value == "开":
                other_settings_set.append("启用快捷键")
            if auto_save_settings_value2 == "开":
                other_settings_set.append("自动保存设置")
                command = self._save_settings

            EasyAutoWindow(self._window, window_title="设置", window_width_value=780, window_height_value=340,
                           adjust_x=False, adjust_y=False)

            f1 = EasyFrame(self._window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
            f11 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
            f12 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
            f13 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
            f14 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()
            f2 = EasyFrame(self._window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES, is_debug=False).get()

            EasyLabel(f11, text="加密算法:", side=tk.LEFT)
            algorithm = EasyDropList(f11,
                                     options=['自动', 'AEAD', 'AES', 'Camellia', 'Fernet', 'RSA', 'Blowfish', 'CAST5',
                                              'RC4'], default=algorithm_settings, side=tk.LEFT, cmd=self._save_settings)
            EasyLabel(f11, text="*越靠上的算法越安全", side=tk.LEFT, font_size=12, text_color="gray")

            EasyLabel(f12, text="由于程序会根据密钥自动检测加密的算法来匹配解密的算法, 所以无需设置解密的算法",
                      side=tk.LEFT, font_size=12)

            other_settings = EasyCheckButton(f13, text=["退出设置未保存时提醒", "加密解密出错时弹出错误提示",
                                                        "重置设置后自动保存", "启用快捷键", "自动保存设置"],
                                             set_text_list=other_settings_set, master_win=self._window, expand=True,
                                             fill=tk.Y,
                                             cmd=command)

            EasyButton(f14, text="关于快捷键", cmd=self._about_keys, side=tk.LEFT, width=10, height=1,
                       font_size=12)

            EasyButton(f2, text="保存", expand=tk.YES, height=2, cmd=self._save_settings, side=tk.LEFT,
                       fill=tk.X)

            EasyButton(f2, text="退出", expand=tk.YES, height=2, cmd=self._on_settings_window_close, side=tk.LEFT,
                       fill=tk.X)

            EasyButton(f2, text="重置", expand=tk.YES, height=2, cmd=self._reset_settings, side=tk.LEFT,
                       fill=tk.X)

            fade_in(self._window)
            self._window.protocol("WM_DELETE_WINDOW", self._on_settings_window_close)

            # with open(shortcut_keys_settings, 'r', encoding='utf-8') as file:
            #     shortcut_keys_settings_value = file.read()
            #
            # if shortcut_keys_settings_value == "开":
            #     self._window.bind('<Command-comma>', lambda event: settings())
            #     self._window.bind('<F1>', lambda event: instructions())
            #     self._window.bind('<q>', lambda event: quit_window())
            #     self._window.bind('<Q>', lambda event: quit_window())

        else:
            center_window(self._window)
