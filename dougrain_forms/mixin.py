# -*- coding: utf-8 -*-
"""
A mixin to use on your dougrain Document.

:author: 2013, Pascal Hartig <phartig@weluse.de>
:license: BSD
"""

from __future__ import absolute_import, print_function, unicode_literals


class FormsMixin(object):

    def add_form(self, rel, target, **kwargs):
        raise NotImplementedError()
