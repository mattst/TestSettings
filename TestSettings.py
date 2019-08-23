
import sublime
import sublime_plugin

from .SettingsModule import Settings
from .MiscModule import misc_module_done_text
from .TestSettingsSubClass import TestSettingsSubClass


global settings

def plugin_loaded():
    global settings
    settings = Settings()
    settings.load_all()

def plugin_unloaded():
    settings.remove_callbacks()


class TestSettingsCommand(sublime_plugin.WindowCommand):

    def run(self):

        caption = settings.items["caption"]
        sub_class = TestSettingsSubClass()
        init_text = sub_class.init_text

        self.window.show_input_panel(caption, init_text,
                            self.on_panel_done, None, None)

    def on_panel_done(self, text):
        done_text = misc_module_done_text()
        print(done_text + ": " + text)
