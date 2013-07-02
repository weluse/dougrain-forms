# -*- coding: utf-8 -*-
"""
A mixin to use on your dougrain Document.

:author: 2013, Pascal Hartig <phartig@weluse.de>
:license: BSD
"""

from __future__ import absolute_import, print_function, unicode_literals
from dougrain.document import mutator
from .form import Form


FORMS_KEY = '_forms'


class FormsMixin(object):

    def form(self, href, **kwargs):
        """Returns a new form relative to this resource."""

        return Form(dict(href=href, **kwargs), self.base_uri)

    @mutator()
    def set_form(self, rel, target, **kwargs):
        """Adds a form to the document.

        Calling code should use this method to add forms instead of
        modifying ``forms`` directly.

        This method adds a form to the given ``target`` to the document with
        the given ``rel``.

        If ``target`` is a string, a form is added with ``target`` as its
        ``href`` property and other properties from the keyword arguments.

        If ``target`` is a ``Form`` object, it is added to the document and the
        keyword arguments are ignored.

        Arguments:

        - ``rel``: a string specifying the link relationship type of the link.
          It should be a well-known link relation name from the IANA registry
          (http://www.iana.org/assignments/link-relations/link-relations.xml),
          a full URI, or a CURIE.
        - ``target``: the action of the form.

        """

        # Currently only used to match forms itself
        if hasattr(target, 'as_form'):
            form = target.as_form()
        else:
            form = self.form(target, **kwargs)

        forms = self.o.setdefault(FORMS_KEY, {})

        new_form = form.as_object()
        # Replace the current form instead of appending it
        forms[rel] = new_form

    @mutator()
    def delete_form(self, rel=None):
        """Removes a form resource from this document identified by its
        ``rel``.

        Arguments:
        - ``rel``: an optional string specifying form relationship type to be
            removed. If omitted, all forms will be removed.
        """

        if FORMS_KEY not in self.o:
            return

        if rel is None:
            for rel in self.o[FORMS_KEY]:
                self.delete_form(rel)

            return

        if rel not in self.o[FORMS_KEY]:
            return

        del self.o[FORMS_KEY][rel]
