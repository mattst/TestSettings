
# Launch keys:
# { "keys": ["ctrl+k", "ctrl+shift+z"], "command": "test_settings" }

import sublime
import sublime_plugin

from .TestSettingsSubClass import TestSettingsSubClass
from .SettingsModule import Settings

# Both of the imports below result in the same problem, see on_panel_done()
# placing the import line above the Settings import line makes no difference.
#
# from .MiscModule import *
from .MiscModule import misc_module_done_text

def plugin_loaded():
    Settings.load_settings()

def plugin_unloaded():
    Settings.remove_callbacks()

class TestSettingsCommand(sublime_plugin.WindowCommand):

    def run(self):

        test_sub_class = TestSettingsSubClass()
        init_text = test_sub_class.init_text

        self.window.show_input_panel(Settings.caption_text, init_text,
            self.on_panel_done, self.on_panel_change, self.on_panel_cancel)

    def on_panel_done(self, text):
        done_text = misc_module_done_text()
        print("In: on_panel_done() - done_text: " + done_text)
        # This fails the output is:
        # In: on_panel_done() - done_text: Not set

    def on_panel_change(self, text):
        print("In: on_panel_change() - change_text: " + Settings.change_text)

    def on_panel_cancel(self):
        print("In: on_panel_cancel() - cancel_text: " + Settings.cancel_text)
