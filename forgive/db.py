# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json
import os


class ForgiveDB(object):
    _memory_db = {}

    def __init__(self, path=None):
        """
        Initialize a ForgiveDB instance using path as a json file storage.
        If path is None, ForgiveDB will be in memory.

        :param path: the json file path
        :type path: str | unicode
        """
        self.db_path = path

    @property
    def in_memory(self):
        """
        indicator for if ForgiveDB is in memory
        :rtype: bool
        """
        return self.db_path is None

    def get(self, key, default=None):
        """ Get key value, return default if key doesn't exist """
        if self.in_memory:
            return self._memory_db.get(key, default)
        else:
            db = self._read_file()
            return db.get(key, default)

    def set(self, key, value):
        """ Set key value """
        if self.in_memory:
            self._memory_db[key] = value
        else:
            db = self._read_file()
            db[key] = value
            with open(self.db_path, 'w') as f:
                f.write(json.dumps(db, ensure_ascii=False, indent=2))

    def _read_file(self):
        """
        read the db file content
        :rtype: dict
        """
        if not os.path.exists(self.db_path):
            return {}
        with open(self.db_path, 'r') as f:
            content = f.read()
            return json.loads(content)
