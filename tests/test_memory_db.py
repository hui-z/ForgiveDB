# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from forgive.db import ForgiveDB


class MemoryDBTests(unittest.TestCase):
    def setUp(self):
        self.db = ForgiveDB()

    def test_in_memory_flag(self):
        self.assertTrue(self.db.in_memory)

    def test_set(self):
        self.db.set('key', 'value')
        self.db.set('', '')
        self.db.set(list, str)
        self.db.set(ForgiveDB, 'naive')

    def test_get(self):
        self.test_set()
        self.assertEqual('value', self.db.get('key'))
        self.assertEqual('', self.db.get(''))
        self.assertEqual(str, self.db.get(list))
        self.assertEqual('naive', self.db.get(ForgiveDB))
