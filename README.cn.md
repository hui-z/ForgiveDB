<p align="center">
    <img src="https://rawgit.com/hui-z/ForgiveDB/master/pics/logo.jpg" height="130">
</p>
<p align="center">
    <a href="https://pypi.python.org/pypi/forgive">
        <img src="https://img.shields.io/pypi/v/forgive.svg">
    </a>
    <a href="https://travis-ci.org/hui-z/ForgiveDB">
        <img src="https://travis-ci.org/hui-z/ForgiveDB.svg?branch=master">
    </a>
    <a href="http://codecov.io/github/hui-z/ForgiveDB?branch=master">
        <img src="http://codecov.io/github/hui-z/ForgiveDB/coverage.svg?branch=master">
    </a>
    <a href="README.md">
        <img src="https://img.shields.io/badge/Intro-En-brightgreen.svg">
    </a>
</p>

* 没人帮你合 Pull Request 怎么办 ?
* 第三方库老是要升依赖版本怎么办 ?
* 老是有新的需求怎么办 ?

![forgive](pics/forgive.jpg)

[lowdb](https://github.com/typicode/lowdb) 是 JS 写的，
[tinydb](http://tinydb.readthedocs.io/en/latest/intro.html) 也不够小。
[ForgiveDB](https://github.com/hui-z/ForgiveDB) 才是你的归宿。

ForgiveDB 是一个无依赖的微型数据库，
支持内存存储和 JSON 文件格式存储。


## 安装

使用 pip 一键安装，
这可是个好东西。

``` python
pip install forgive
```


## 用法

代码就是最好的文档
（其实是因为我们文档写的烂）

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

