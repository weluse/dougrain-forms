# -*- coding: utf-8 -*-
"""
A forms generation extension for dougrain.

:author: 2013, Pascal Hartig <phartig@weluse.de>
:license: BSD
"""

from __future__ import absolute_import, print_function, unicode_literals
try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse


class Form(object):
    """Representation of a HALO form from a ``Document``.

       Constructors:

    - ``Form.from_object(o, base_uri=None)``:
        returns a new ``Form`` based on a JSON object.

    Public Instance Attributes:

    - ``href``: ``str`` containing the href of the form.
    - ``method``: ``str`` containing the method of the form. Absent if the
        form has no method.
    - ``schema``: ``dict`` containing the JSON schema of the form. Absent if
        the form has no schema.
    - ``headers``: ``dict`` containing the JSON schema of the form. Absent if
        the form has no headers.
    """

    def __init__(self, json_object, base_uri=None):
        self.o = json_object
        self.href = json_object['href']

        if 'method' in json_object:
            self.method = json_object['method']

        if 'schema' in json_object:
            self.method = json_object['schema']

        if 'headers' in json_object:
            self.method = json_object['headers']

        if base_uri is None:
            self._target = self.href
        else:
            self._target = urlparse.urljoin(base_uri, self.href)

    @classmethod
    def from_object(cls, o, base_uri=None):
        """Returns a new ``Form`` based on a JSON object or array.

        Arguments:

        - ``o``: a dictionary holding the deserializated JSON for the new
            ``Form``, or a ``list`` of such documents.
        - ``base_uri``: optional URL used as the basis when expanding
            relative URLs in the form href.
        """
        if isinstance(o, list):
            return map(lambda x: cls.from_object(x, base_uri), o)

        return cls(o, base_uri)

    def as_object(self):
        """Returns a dictionary representing the HALO JSON form."""

        return self.o

    def as_form(self):
        """Returns a ``Form`` to the same resource as this link.

        This method is trivial, but is provided for symmetry with ``Document``
        and ``Link``.
        """

        return self

    def __repr__(self):
        if hasattr(self, 'method'):
            return '<Form [{0}] {!r}>'.format(self.method, self._target)
        else:
            return '<Form {0!r}>'.format(self._target)

    def __iter__(self):
        yield self

    def __eq__(self, other):
        return (isinstance(other, Form) and
                self.as_object() == other.as_object())
