# -*- coding: utf-8 -*-
"""
Tests for the form generation.

:author: 2013, Pascal Hartig <phartig@weluse.de>
:license: BSD
"""

from __future__ import absolute_import, print_function, unicode_literals
from unittest import TestCase
from dougrain import Document
from dougrain_forms import FormsMixin
import os
import json


class HyperDocument(Document, FormsMixin):
    pass


class FormsTestCase(TestCase):

    @staticmethod
    def _load_json_fixture(filename):
        return json.load(open(os.path.join(os.path.dirname(
            __file__), 'fixtures', filename)))

    def test_set_form(self):
        doc = HyperDocument.empty()
        doc.add_link('self', '/foo')

        doc.set_form(
            'attack',
            '/attacks',
            headers={
                'Content-Type': 'application/json'
            },
            method='POST',
            schema=self._load_json_fixture('schema.json')
        )

        mike = self._load_json_fixture('mike.json')
        self.assertEqual(mike, doc.as_object())

    def test_delete_form(self):
        doc = HyperDocument.empty()
        doc.add_link('self', '/foo')

        doc.set_form(
            'attack',
            '/attacks'
        )

        self.assertTrue('attack' in doc.as_object()['_forms'])
        doc.delete_form('attack')
        self.assertFalse('attack' in doc.as_object()['_forms'])
