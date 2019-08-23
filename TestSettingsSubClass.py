
# from .SettingsModule import Settings
# import .SettingsModule
from .SettingsModule import Settings

global settings

# def plugin_loaded():
#     global settings
#     settings = Settings()
#     settings.load_all()

# def plugin_unloaded():
#     settings.remove_callbacks()


class TestSettingsSubClass():

    def __init__(self):
        self.init_text = settings.items["init_text"]
