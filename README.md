![logo](https://rawgit.com/hui-z/ForgiveDB/master/pics/logo.jpg)

[![Package](https://img.shields.io/pypi/v/forgive.svg)](https://pypi.python.org/pypi/forgive)
[![Updates](https://pyup.io/repos/github/hui-z/ForgiveDB/shield.svg)](https://pyup.io/repos/github/hui-z/ForgiveDB/)
[![CI](https://travis-ci.org/hui-z/ForgiveDB.svg?branch=master)](https://travis-ci.org/hui-z/ForgiveDB)
[![Coverage](http://codecov.io/github/hui-z/ForgiveDB/coverage.svg?branch=master)](http://codecov.io/github/hui-z/ForgiveDB?branch=master)
[![Code Health](https://landscape.io/github/hui-z/ForgiveDB/master/landscape.svg?style=flat)](https://landscape.io/github/hui-z/ForgiveDB/master)
[![License](https://img.shields.io/github/license/hui-z/ForgiveDB.svg)](https://github.com/hui-z/ForgiveDB/blob/master/LICENSE)
[![README](https://img.shields.io/badge/简介-中文-brightgreen.svg)](README.cn.md)

* What if no one accept your PR ?
* What if lib upgrade their dependency ?
* What if you got a brand new requirement ?

![forgive](pics/forgive.jpg)

[lowdb](https://github.com/typicode/lowdb) is JavaScript,
[tinydb](http://tinydb.readthedocs.io/en/latest/intro.html) is not that tiny.
[ForgiveDB](https://github.com/hui-z/ForgiveDB) is your destiny.

ForgiveDB is a small, independent database,
supports in-memory or json-file storage.


## Installation

Use pip. Oh you should learn it.

``` python
pip install forgive
```


## Usage

Code is the best document.
(Because we are not good at writing documents.)

``` python
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
```
