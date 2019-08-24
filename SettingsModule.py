
import sublime

class Settings:

    settings = None
    filename = "TestSettings.sublime-settings"

    # User configurable settings.
    caption_text = "Not set"
    init_text = "Not set"
    done_text = "Not set"
    change_text = "Not set"
    cancel_text = "Not set"

    @classmethod
    def load_settings(cls):

        cls.settings = sublime.load_settings(cls.filename)
        cls.init_setting("caption_text", cls.set_caption_text)
        cls.init_setting("init_text", cls.set_init_text)
        cls.init_setting("done_text", cls.set_done_text)
        cls.init_setting("change_text", cls.set_change_text)
        cls.init_setting("cancel_text", cls.set_cancel_text)

    @classmethod
    def init_setting(cls, setting_name, setting_method):
        setting_method()
        cls.settings.add_on_change(setting_name, setting_method)

    @classmethod
    def remove_callbacks(cls):
        cls.settings.clear_on_change("caption_text")
        cls.settings.clear_on_change("init_text")
        cls.settings.clear_on_change("done_text")
        cls.settings.clear_on_change("change_text")
        cls.settings.clear_on_change("cancel_text")

    @classmethod
    def set_caption_text(cls):
        DEFAULT = "default_caption_text"
        cls.caption_text = cls.get_string_setting("caption_text", DEFAULT)

    @classmethod
    def set_init_text(cls):
        DEFAULT = "default_init_text"
        cls.init_text = cls.get_string_setting("init_text", DEFAULT)

    @classmethod
    def set_done_text(cls):
        DEFAULT = "default_done_text"
        cls.done_text = cls.get_string_setting("done_text", DEFAULT)

    @classmethod
    def set_change_text(cls):
        DEFAULT = "default_change_text"
        cls.change_text = cls.get_string_setting("change_text", DEFAULT)

    @classmethod
    def set_cancel_text(cls):
        DEFAULT = "default_cancel_text"
        cls.cancel_text = cls.get_string_setting("cancel_text", DEFAULT)

    @classmethod
    def get_string_setting(cls, setting, default):
        value = cls.settings.get(setting, None)
        return value if isinstance(value, str) else default
