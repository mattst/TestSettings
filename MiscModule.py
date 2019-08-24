
from .SettingsModule import Settings

def misc_module_done_text():
    print("In: misc_module_done_text() - done_text: " + Settings.done_text)
    return Settings.done_text
    # This fails the output is:
    # In: misc_module_done_text() - done_text: Not set
