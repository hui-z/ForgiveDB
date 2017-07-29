原谅数据库
=====

看不懂英文不是你的错，
是世界的错。
你有没有想过：

* 没人帮你合 Pull Request 怎么办 ?
* 第三方库老是要升依赖版本怎么办 ?
* 老是有新的需求怎么办 ?

.. image:: pics/forgive.jpg

`lowdb <https://github.com/typicode/lowdb>`_ 是 JS 写的，
`tinydb <http://tinydb.readthedocs.io/en/latest/intro.html>`_ 也不够小。
`ForgiveDB <https://github.com/hui-z/ForgiveDB>`_ 才是你的归宿。

ForgiveDB 是一个无依赖的微型数据库，
支持内存存储和 JSON 文件格式存储。


安装
--

使用 pip 一键安装，
这可是个好东西。

.. code-block::

    pip install forgive


用法
--

代码就是最好的文档
（其实是因为我们文档写的烂）

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
