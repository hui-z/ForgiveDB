Forgive DB
==========

`我看不懂英文 <README_CN.rst>`_

* What if no one accept your PR ?
* What if lib upgrade their dependency ?
* What if you got a brand new requirement ?

.. image:: pics/forgive.jpg

`lowdb <https://github.com/typicode/lowdb>`_ is JavaScript,
`tinydb <http://tinydb.readthedocs.io/en/latest/intro.html>`_ is not that tiny.
`ForgiveDB <https://github.com/hui-z/ForgiveDB>`_ is your destiny.

ForgiveDB is a small, independent database,
supports in-memory or json-file storage.


Installation
------------

Use pip. Oh you should learn it.

.. code-block::

    pip install forgive


Usage
-----

Code is the best document.
(Because we are not good at writing documents.)

.. code-block::

    from forgive.db import ForgiveDB

    file_db = ForgiveDB('/some/path')
    # file_db = ForgiveDB(r'C:\\some\\path')  # windows
    file_db.set('key', 'value')
    value = file_db.get('key')
    default_value = file_db.get('no-such-key', 'default-value')

    # Or in memory
    memory_db = ForgiveDB()
    memory_db.set(ForgiveDB, 'simple and interesting')
    memory_db.get(ForgiveDB)  # simple and interesting
