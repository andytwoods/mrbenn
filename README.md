# MrBenn Toolbar Plugin

<p align="center">
    <img alt="MrBenn explainer animation" src="https://github.com/andytwoods/mrbenn/blob/main/.github/images/mrbenn.gif?raw=true">
</p>

<p align="center">
Saving you 10 seconds, 100 times a day.
</p>

<p align="center">
    <a href="https://mrbenn.readthedocs.io/en/latest/index.html">Docs</a> |
    <a href="https://pypi.org/project/mrbenn-toolbar-plugin/">Install</a> |
    <a href="https://github.com/andytwoods/mrbenn/projects/1">Contribute</a> 
</p>

The MrBenn Toolbar Plugin is an addon for the Django Debug Toolbar which allows you to quickly open template files and
views in your IDE.

<p align="center">
<img alt="MrBenn demo" src="https://github.com/andytwoods/mrbenn/blob/main/.github/images/panel.jpg?raw=true">
</p>

## Installation

To install the MrBenn, you can use `pip`! Simply follow the command below:

```pip install mrbenn-toolbar-plugin```

After the package has been installed, head over to your settings.py. You need to add the following:

- In ``INSTALLED_APPS`` add ``mrbenn_panel``
- Under ``DEBUG_TOOLBARS`` add ``mrbenn_panel.panel.MrBennPanel``. We recommend you remove
  `debug_toolbar.panels.staticfiles.StaticFilesPanel`.
- Finally, in settings, you need to add the location of the IDE you would like to use to open files with an
  option called ``DJANGO_WINDOWS_IDE``. Be careful with the type of slash you use. For example, the setting for the PyCharm Interpreter would
  be `DJANGO_WINDOWS_IDE="C:/Program Files/JetBrains/PyCharm 2023.1.1/bin/pycharm64.exe"`.

## Limitations and next steps

Do not use this package in production. Do not use Django-Debug-Toolbar in production either! In this package, Template
file-system location information is sent to the backend via a url-parameter. As it stands, any files on your file system
could be opened by manipulating this parameter. An easy pull-request would be to check that a file to be opened exists
within the current project, before opening it.

Django-debug-toolbar cleverly uses keys instead of raw file system information (
see [here](https://github.com/jazzband/django-debug-toolbar/blob/5665d6808ce0780d2594157684dd6869d1e048a5/debug_toolbar/panels/templates/views.py#L19))
. This would also be good next step for this package to implement.

## Requirements

On top of Django, MrBenn requires the Django Debug Toolbar package found
[here](https://github.com/jazzband/django-debug-toolbar).

## How to contribute?

All contributions are appreciated! To contribute, simply create a new branch with your contribution and raise a PR! You
can ping @andywoods should any issues arize!

Should you get stuck on something, we also have a contributing section in our wiki! LINK TBD

## What's with the name?

Mr Benn was a kids UK TV show from the 70s ([wikipedia](https://en.wikipedia.org/wiki/Mr_Benn)). The main character, Mr
Benn, on each episode walked through a magical door which took him on different adventures. Perhaps I was thinking that
this package in a similar fashion performs a little IDE magic, transporting you to the right file, each time you click
the link to your current view or template. #ModernKidsTVshowsSuck #CBEEBIESthoughRocks