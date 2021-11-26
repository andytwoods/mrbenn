Installation
================

To install the MrBenn, you can use `pip`! Simply follow the command below: ::

    pip install mrbenn-toolbar-plugin

After the package has been installed, head over to your settings.py. You need to add the following:

- in ``INSTALLED_APPS`` add ``mrbenn-panel``
- under ``DEBUG_TOOLBARS`` add ``mrbenn-panel.panel.MrBennPanel``. We recommend you remove
  ``debug_toolbar.panels.staticfiles.StaticFilesPanel``.
- finally, in your `env` file, you need to add the location of the IDE you would like to use to open files with an
  option called ``DJANGO_WINDOWS_IDE``. For example, the setting for the PyCharm Interpreter would
  be ``DJANGO_WINDOWS_IDE=C:\Program Files\JetBrains\PyCharm 2021.1.3\bin\pycharm64.exe``.