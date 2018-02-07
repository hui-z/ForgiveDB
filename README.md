![logo](https://rawgit.com/hui-z/ForgiveDB/master/pics/logo.svg)

[![Package](https://img.shields.io/pypi/v/forgive.svg)](https://pypi.python.org/pypi/forgive)
[![Updates](https://pyup.io/repos/github/hui-z/ForgiveDB/shield.svg)](https://pyup.io/repos/github/hui-z/ForgiveDB/)
[![Travis](https://img.shields.io/travis/hui-z/ForgiveDB.svg)](https://travis-ci.org/hui-z/ForgiveDB)
[![Codecov](https://img.shields.io/codecov/c/github/hui-z/ForgiveDB.svg)](http://codecov.io/github/hui-z/ForgiveDB?branch=master)
[![CodeHealth](https://landscape.io/github/hui-z/ForgiveDB/master/landscape.svg?style=flat)](https://landscape.io/github/hui-z/ForgiveDB/master)
[![License](https://img.shields.io/github/license/hui-z/ForgiveDB.svg)](https://github.com/hui-z/ForgiveDB/blob/master/LICENSE)
[![README](https://img.shields.io/badge/简介-中文-brightgreen.svg)](https://github.com/hui-z/ForgiveDB/blob/master/README.cn.md)

* What if no one accepts your PR ?
* What if a lib upgrades their dependencies ?
* What if you get a brand new requirement ?

![forgive](https://rawgit.com/hui-z/ForgiveDB/master/pics/forgive.jpg)

[lowdb](https://github.com/typicode/lowdb) is written in JavaScript,
[tinydb](http://tinydb.readthedocs.io/en/latest/intro.html) is not that tiny.
[ForgiveDB](https://github.com/hui-z/ForgiveDB) is your destiny.

ForgiveDB is a tiny database with no depencencies,
supports in-memory or json-file storage.


## Installation

Use [pip](https://pip.pypa.io/). Oh you should learn it.

``` python
pip install forgive
```


## Usage

Code is the best document.
(Because we are not good at writing documents.)

``` python
from forgive import ForgiveDB

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
