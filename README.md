# Forgive DB 原谅数据库

![enough][enough]

受 [lowdb][lowdb] 启发，
并且 Python 里面的 [tinydb][tinydb] 也不够小...

我们决定造一个真正的小巧的好用的数据库！

不好用怎么办~
那当然是选择原谅他啦~

## 安装

使用 pip 一键安装

```bash
pip install forgive
```

## 使用

```python
from forgive.db import ForgiveDB

file_db = ForgiveDB('/some/path')
# file_db = ForgiveDB(r'C:\\some\\path')  # windows
file_db.set('key', 'value')
value = file_db.get('key')
default_value = file_db.get('no-such-key', 'default-value')

# Or in memory
memory_db = ForgiveDB()
memory_db.set([1], [2])
memory_db.get([1])  # [2]
```

[enough]: /pics/enough.jpg
[lowdb]: https://github.com/typicode/lowdb
[tinydb]: http://tinydb.readthedocs.io/en/latest/intro.html
