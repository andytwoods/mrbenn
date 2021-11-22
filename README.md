# MrBenn Toolbar Plugin

<p align="center">
    <a href="https://mrbenn.readthedocs.io/en/latest/">Docs</a> |
    <a href="">Contribute</a>
</p>

The MrBenn Toolbar Plugin is an addon for the Django Debug Toolbar which allows you to quickly
open static files and views, on top of the useful debug information provided by
the Django Debug Toolbar.

<p align="center">
    <img alt="MrBenn demo" src="https://user-images.githubusercontent.com/36422452/142882309-3885b572-45ed-4b98-876a-f25abb68192a.png">
</p>

## Installation

To install the MrBenn, you can use `pip`! Simply follow the command below:

```pip install mrbenn-plugin```

After the package has been installed, head over to your settings.py. You need to
add the following:

- in ``INSTALLED_APPS`` add ``mrbenn-plugin``
- under ``DEBUG_TOOLBARS`` add ``mrbenn-plugin.panel.MrBennPanel``. We recommend you remove
`debug_toolbar.panels.staticfiles.StaticFilesPanel`.
- finally, in your `env` file, you need to add the location of the IDE you would like to use to
open files with an option called ``DJANGO_WINDOWS_IDE``. For example, the setting for the PyCharm
Interpreter would be `DJANGO_WINDOWS_IDE=C:\Program Files\JetBrains\PyCharm 2021.1.3\bin\pycharm64.exe`. 

## Requirements

On top of Django, MrBenn requires the Django Debug Toolbar package found 
[here](https://github.com/jazzband/django-debug-toolbar).

## How to contribute?

All contributions are appreciated! To contribute, simply create a new branch with your contribution
and raise a PR! You can ping @andywoods should any issues arize!

Should you get stuck on something, we also have a contributing section in our wiki! LINK TBD