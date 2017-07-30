<p align="center">
    <img src="https://rawgit.com/hui-z/ForgiveDB/master/pics/logo.jpg" height="130">
</p>
<p align="center">
    <a href="https://pypi.python.org/pypi/forgive">
        <img src="https://img.shields.io/pypi/v/forgive.svg" alt="Package"/>
    </a>
    <a href="https://pyup.io/repos/github/hui-z/ForgiveDB/">
        <img src="https://pyup.io/repos/github/hui-z/ForgiveDB/shield.svg" alt="Updates"/>
    </a>
    <a href="https://travis-ci.org/hui-z/ForgiveDB">
        <img src="https://travis-ci.org/hui-z/ForgiveDB.svg?branch=master" alt="CI" />
    </a>
    <a href="http://codecov.io/github/hui-z/ForgiveDB?branch=master">
        <img src="http://codecov.io/github/hui-z/ForgiveDB/coverage.svg?branch=master" alt="Coverage" />
    </a>
    <a href="README.cn.md">
        <img src="https://img.shields.io/badge/简介-中文-brightgreen.svg" alt="README-CN"/>
    </a>
</p>

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
