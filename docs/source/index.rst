MrBenn Toolbar Plugin Docs
============================

The MrBenn Toolbar Plugin is an addon for the Django Debug Toolbar which allows you to quickly open static files and
views in your IDE.

.. image:: https://user-images.githubusercontent.com/36422452/142882309-3885b572-45ed-4b98-876a-f25abb68192a.png
  :align: center
  :alt: Logo

Limitations and next steps
------------------------------

Do not use this package in production. Do not use Django-Debug-Toolbar in production either! In this package, template
file-system location information is sent to the backend via a url-parameter. As it stands, any files on your file system
could be opened by manipulating this parameter. An easy pull-request would be to check that a file to be opened exists
within the current project, before opening it.

Django-debug-toolbar cleverly uses keys instead of raw file system information (https://github.com/jazzband/django-debug-toolbar/blob/5665d6808ce0780d2594157684dd6869d1e048a5/debug_toolbar/panels/templates/views.py#L19)
. This would also be good next step for this package to implement.

What's with the name?
-------------------------

Mr Benn was a kids UK TV show from the 70s (https://en.wikipedia.org/wiki/Mr_Benn). The main character, Mr
Benn, on each episode walked through a magical door which took him on different adventures. Perhaps I was thinking that
this package in a similar fashion performs a little IDE magic, transporting you to the right file, each time you click
the link to your current view or template. #ModernKidsTVshowsSuck #CBEEBIESthoughRocks

Documentation
---------------

.. toctree::
   :maxdepth: 2

   installation
   changes
   contributing