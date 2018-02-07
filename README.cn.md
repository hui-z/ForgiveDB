![logo](https://rawgit.com/hui-z/ForgiveDB/master/pics/logo.svg)

[![Package](https://img.shields.io/pypi/v/forgive.svg)](https://pypi.python.org/pypi/forgive)
[![Updates](https://pyup.io/repos/github/hui-z/ForgiveDB/shield.svg)](https://pyup.io/repos/github/hui-z/ForgiveDB/)
[![Travis](https://img.shields.io/travis/hui-z/ForgiveDB.svg)](https://travis-ci.org/hui-z/ForgiveDB)
[![Codecov](https://img.shields.io/codecov/c/github/hui-z/ForgiveDB.svg)](http://codecov.io/github/hui-z/ForgiveDB?branch=master)
[![CodeHealth](https://landscape.io/github/hui-z/ForgiveDB/master/landscape.svg?style=flat)](https://landscape.io/github/hui-z/ForgiveDB/master)
[![License](https://img.shields.io/github/license/hui-z/ForgiveDB.svg)](https://github.com/hui-z/ForgiveDB/blob/master/LICENSE)
[![README](https://img.shields.io/badge/Intro-En-brightgreen.svg)](https://github.com/hui-z/ForgiveDB/blob/master/README.md)

* 没人帮你合 Pull Request 怎么办 ?
* 第三方库老是要升依赖版本怎么办 ?
* 老是有新的需求怎么办 ?

![forgive](https://rawgit.com/hui-z/ForgiveDB/master/pics/forgive.jpg)

[lowdb](https://github.com/typicode/lowdb) 是 JS 写的，
[tinydb](http://tinydb.readthedocs.io/en/latest/intro.html) 也不够小。
[ForgiveDB](https://github.com/hui-z/ForgiveDB) 才是你的归宿。

ForgiveDB 是一个无依赖的微型数据库，
支持内存存储和 JSON 文件格式存储。


## 安装

使用 [pip](https://pip.pypa.io/) 一键安装，这可是个好东西。

``` python
pip install forgive
```


## 用法

代码就是最好的文档
（其实是因为我们文档写的烂）

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

