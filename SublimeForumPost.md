
[Sublime Forum Post](https://forum.sublimetext.com/t/accessing-settings-from-within-a-multi-module-st-package/46128)


Accessing settings from within a multi-module ST package


When handling settings in a multi-module ST package I've hit a problem. I'd like a single instance global of the settings class which can be shared/accessed from within all the other Python modules. As far as I can tell this is not possible within a ST package (or if I'm wrong please enlighten me!).

As an alternative I've used a settings class which has no instance created. Instead each method is defined with the `@classmethod` decorator. That way the settings class can be imported from the settings module into the other modules and the settings can be accessed easily everywhere.

I have a proof of concept project which I've uploaded to this [GitHub repository](https://github.com/mattst/TestSettings).

The problem is in `MiscModule.py` which defines a single function which fails to access the setting it is supposed to handle. The settings are all accessed correctly from `TestSettings.py` and from `TestSettingsSubClass.py`.

Can anyone explain why the `MiscModule.py` function fails to retrieve the setting and how I can fix it?

Thanks.
