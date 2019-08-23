
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

def misc_module_done_text():
    return settings.items["done_text"]
