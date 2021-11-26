Contributing
===============

Why should I contribute?
=========================
Contributing is a great way to keep this project up to date but also allows you to add any new feature that you think
might be useful to this!

You will also be mentioned in our contributors list and receive our forever love!

How do I contribute?
====================

First, have a look around! We have a Development Board, similar to a Trello where most issues will go! Have a look under
Proposed first, as these are issues that haven't been picked up by other contributors! If you have an idea or anything
that isn't an issue, feel free to add one and assign yourself to it, that way, we know you are workin on it!

Getting the code
--------------------

Simply create a new branch from ``main`` and start there! You shouldn't touch anything else other than the ``mrbenn_panel``
folder, as that's where the code base is located! To clone the code, simply type in your favourite console: ::

    git clone https://github.com/andytwoods/mrbenn.git

After successfully getting the code, make sure to create a new virtual environment and install the required packages by running: ::

    pip install -r requirements.txt

Should everything work correctly, now you are able to start coding!

Style
----------

We don't use any specific code formatter at the moment, however the styling should be similar to the Google Style Guide
which is quite a common style, found at https://google.github.io/styleguide/.

Tests
----------

The tests are location in the ``tests.py`` file. When creating a new feature or fixing older ones, please run the test suite
and create or fix tests to ensure they pass! Tests will be checked before code is merged!

Pull Requests
---------------

When you finished coding, simply create a new pull request from you Github Issue and ensure these are linked between each other.
Our Development Board has clever automations which make life easier!

When your PR will be accepted, you issue will be closed and the code will be merged into the ``main`` branch! At the same time
a new release might be available and your name will be added to our contributors list!
