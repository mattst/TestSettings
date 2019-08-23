
import sublime
import sublime_plugin

# The global scope ensures that the settings can
# be easily accessed from within all the classes.
# global settings
# settings = Settings()
# settings.load_all()

# def plugin_loaded():
#     global settings
#     settings = Settings()
#     settings.load_all()

# def plugin_unloaded():
#     settings.remove_callbacks()

# def init():
#     global settings
#     settings = Settings()
#     settings.load_all()


class Settings:
    """
    Handles all the settings. A callback method is added for each setting, it
    gets called by ST if that setting is changed in the settings file.
    """

    def __init__(self):

        FILENAME = "TestSettings.sublime-settings"
        self.st_settings = sublime.load_settings(FILENAME)

        # User configurable settings.
        self.items = {}
        self.items["caption"] = None
        self.items["init_text"] = None
        self.items["done_text"] = None

    def load_all(self):
        self.init_setting("caption", self.set_caption)
        self.init_setting("init_text", self.set_init_text)
        self.init_setting("done_text", self.set_done_text)

    def init_setting(self, setting_name, setting_method):
        """
        Calls the setting_method to set the setting's value and registers the
        setting_method as a callback so that it will be called by ST if the
        setting's value is changed by the user.
        """

        setting_method()
        self.st_settings.add_on_change(setting_name, setting_method)

    def remove_callbacks(self):
        self.st_settings.clear_on_change("caption")
        self.st_settings.clear_on_change("init_text")
        self.st_settings.clear_on_change("done_text")

    # Methods for the user configurable settings.

    def set_caption(self):
        DEFAULT = "default_caption"
        self.items["caption"] = self.string_setting("caption", DEFAULT)

    def set_init_text(self):
        DEFAULT = "default_init_text"
        self.items["init_text"] = self.string_setting("init_text", DEFAULT)

    def set_done_text(self):
        DEFAULT = "default_done_text"
        self.items["done_text"] = self.string_setting("done_text", DEFAULT)

    # Methods for settings retrieval; all will return a
    # setting of the required type or the default value.

    def string_setting(self, setting, default):
        return self.setting_of_type(setting, default, str)

    def list_setting(self, setting, default):
        return self.setting_of_type(setting, default, list)

    def boolean_setting(self, setting, default):
        return self.setting_of_type(setting, default, bool)

    def list_or_string_setting(self, setting, default):
        return self.setting_of_type(setting, default, (str, list))

    def setting_of_type(self, setting, default, required_type):
        value = self.st_settings.get(setting, None)
        return value if isinstance(value, required_type) else default

    # Special case.

    def integer_setting(self, setting, default, min_value):
        value = self.st_settings.get(setting, None)
        return value if self.is_integer(value) and value >= min_value else default

    def is_integer(self, value):
        # Bool is a subclass of int; isinstance(False, int) == True.
        return isinstance(value, int) and not isinstance(value, bool)
