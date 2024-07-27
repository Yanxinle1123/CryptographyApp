import tkinter as tk

from LeleEasyTkinter.easy_auto_window import EasyAutoWindow
from LeleEasyTkinter.easy_fade_animation import fade_in, fade_out
from LeleEasyTkinter.easy_multi_text import EasyMultiText
from LeleEasyTkinter.easy_popup_animation import animate_resize_window
from LeleEasyTkinter.easy_warning_windows import EasyWarningWindows

from cryptography_app.common.common import replace, center_window


class InstructionsWindow:
    def __init__(self, window, parent_window):
        self._parent_window = parent_window
        self._window = tk.Toplevel(window)

    def center(self):
        center_window(self._window)

    def on_instructions_window_close(self):
        result = EasyWarningWindows(self._window, "是/否",
                                    "下次打开程序时是否需要自动打开此窗口？").show_warning()
        if result:
            self._parent_window.write_one_config("auto_open_instructions_window", True)
        else:
            self._parent_window.write_one_config("auto_open_instructions_window", False)
        fade_out(self._window)
        self._parent_window.instructions_num_sub()

    def run(self):
        instructions_text = ("加密方法: 将需要加密的文本输入到指定的文本框内, 然后点击加密按钮, 加密后的文本和密钥就会显示在指定的文本"
                             "框内。您可以在设置窗口里面调整加密的算法, 默认为自动\n\n\n解密方法: 将密文和密钥输入到指定的文本框内, 然"
                             "后点击解密按钮, 解密后的文本就会显示在指定的文本框内, 程序会根据密钥自动匹配解密算法。(注: 如果解密出错,"
                             " 程序会弹出错误提示, 如果没有看见弹窗, 可能是被设置或者其他窗口挡住了)\n\n\n设置说明: 在设置中, 你可以"
                             "设置加密的算法和其他的功能。(注: 由于程序会根据密钥自动检测加密的算法来匹配解密的算法, 所以无需设置解密的"
                             "算法)如果您想要恢复默认设置, 请点击重置按钮。如果您想要保存您的更改, 请点击保存按钮。如果您想要退出设置, "
                             "请点击退出按钮。\n\n\n关于设置: 点击加密解密窗口下方的设置按钮, 程序就会弹出设置窗口。在设置里, 您可以选"
                             "择加密解密的算法。\n\n\n注意事项: 请不要全屏显示窗口, 全屏模式下, 显示会有一些问题。\n\n\n快捷键: 您可"
                             "以通过按q键来关闭程序, 您也可以通过按command键加逗号来打开设置窗口, 您还可以按F1键来打开使用方法窗口。")

        EasyAutoWindow(self._window, window_title="使用方法", window_width_value=230, window_height_value=170,
                       minimum_value_x=230, minimum_value_y=170)

        instructions_box = EasyMultiText(self._window, expand=tk.YES, fill=tk.BOTH)
        replace(instructions_box, instructions_text)

        fade_in(self._window, ms=2)
        animate_resize_window(self._window, 600, 400, 200, "ordinary", False)

        self._window.protocol("WM_DELETE_WINDOW", self.on_instructions_window_close)

        # with open(shortcut_keys_settings, 'r', encoding='utf-8') as file:
        #     shortcut_keys_settings_value = file.read()
        #
        # if shortcut_keys_settings_value == "开":
        #     self._window.bind('<F1>', lambda event: instructions())
        #     self._window.bind('<Command-comma>', lambda event: settings())
        #     self._window.bind('<q>', lambda event: quit_window())
        #     self._window.bind('<Q>', lambda event: quit_window())
