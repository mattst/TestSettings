

When handling settings in a multi-module ST package I've hit a problem. I'd like a single instance global of the settings class which can be shared/accessed from within all the other Python modules. As far as I can tell this is not possible (or if I'm wrong please enlighten me!).

As an alternative I've used a settings class which has no instance created. Instead each method is defined with the `@classmethod` decorator. That way the settings class can be imported from the settings module into the other modules and the settings can be accessed.

I have a proof of concept project which I've uploaded to GitHub.

The problem is in `MiscModule.py` which defines a single function which fails to access the setting it is supposed to handle. The settings are all accessed correctly from `TestSettings.py` and from `TestSettingsSubClass.py`.

Can anyone explain the `MiscModule.py` function fails to retrieve the setting and how I can fix it?

Thanks.
