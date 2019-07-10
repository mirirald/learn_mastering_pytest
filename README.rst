=====================
 Intermediate Pytest
=====================

..  export PS1="$ "

Copyright 2019 - Matt Harrison

@__mharrison__


http://bit.ly/2019-07-01-pytest

These assignments are based on a Python implementation
that models a lift at a ski resort.

https://github.com/mattharrison/skilift

Assignment 1
============

* Install pytest in a virtual environment
* Run::

    pytest -h

Assignment 2
============

* Download the skilift project from github.
* Create a ``test/`` directory in the ``skilift``
* Create a ``test/test_skilift.py`` file
* Create a test function ``test_line_take`` that
  creates a ``Line`` with 5 people and takes 7.
  Ensure that the amount returned is 5 and the
  ``.num_people`` attribute is 0.
* Create a test function ``test_lift_one_bench``
  that creates a line of 5, and a quad lift
  with 10 benches. Call ``.one_bench`` and
  assert that the correct results are returned.

Assignment 3
============

Parameterization

* Create a test function ``test_line_bad``,
  that creates lines with ``[]``, ``None``, and
  ``'10'`` in them. It tries to call ``.take(1)``
  on each, and checks that the appropriate error
  is raised.

* Create a test function ``test_line_sizes``
  that creates lines of size 0, 5, and 10.
  It takes 5, 2, and 0 from each respectively
  and asserts that the ``.num_people`` attribute
  is correct. (You should probably parameterize
  the result as well)

* Run only the ``test_line_sizes`` test when the line
  is created with size 10. (Hint use ``-v`` to get an id)



Assignment 4
============

* Create a fixture for a line of size 5. Use that
  fixture in ``test_line_take`` and ``test_lift_one_bench``

* Create a fixture for a Quad lift of size 10. Use that
  in ``test_lift_one_bench``


Assignment 5
============

* Create a fixture, ``line_n``, that depends on ``request``.
  Read off of the marker to get a line size. Create
  a test, ``test_line_6``, that creates a tests
  ``.take`` on a ``Line`` with length 6.

* Create a fixture, ``BenchN``, that depends on ``request``.
  Read off of the marker to get a bench size. Dynamically
  subclass ``_Bench`` to create a subclass with the passed
  in size. Create a test, ``test_bench6``, like ``test_left_one_bench``,
  that uses the fixture to create 6 person bench and test it.


Assignment 6
==============

* Create a test, ``test_half_take``, that monkey patches
  ``Line.take`` so that only half the amount requested are
  returned from the line. (ie. ``line.take(4)`` would only
  take 2 from the line)


Assignment 7
============

* Create a ``pytest.ini`` file

* Add an option to run the doctests

* Create a ``test/conftest.py`` file. Move the fixtures to
  this file


Assignment 8
============

* Examine the ``setup.py`` for ``pytest-cov`` on GitHub.

* What is the entry point?

* What hook does the plugin implement?


Assignment 9
============

* Install pytest-cov

* Run coverage on the project using the plugin
