# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import tempfile
import unittest

from forgive import ForgiveDB


class MemoryDBTests(unittest.TestCase):
    def setUp(self):
        with tempfile.NamedTemporaryFile(prefix='forgive', suffix='.db') as f:
            self.db_path = f.name
        self.db = ForgiveDB(self.db_path)

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.unlink(self.db_path)

    def test_in_memory_flag(self):
        self.assertFalse(self.db.in_memory)

    def test_set(self):
        self.db.set('key', 'value')
        self.db.set('', '')
        self.db.set('list', 'str')
        self.db.set('you', 'naive')

    def test_get(self):
        self.test_set()
        self.assertEqual('value', self.db.get('key'))
        self.assertEqual('', self.db.get(''))
        self.assertEqual('str', self.db.get('list'))
        self.assertEqual('naive', self.db.get('you'))
