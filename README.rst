==============
dougrain-forms
==============

.. image:: https://travis-ci.org/weluse/dougrain-forms.png?branch=master
    :target: https://travis-ci.org/weluse/dougrain-forms

A generator for hypermedia forms, following an unofficial draft by Mike Kelly.
The format is roughly based on
`this Gist <https://gist.github.com/mikekelly/3808215>`_ by `Mike Kelly`_.

.. _`Mike Kelly`: http://stateless.co/


Installation
============

::

    pip install dougrain-forms


Usage
=====

Example:

::

    from dougrain_forms import FormsMixin

    class FormsDocument(Document, FormsMixin):
        pass

    doc = FormsDocument.empty()
    doc.add_link('self', '/foo')

    doc.set_form(
        'attack',
        '/attacks',
        headers={
            'Content-Type': 'application/json'
        },
        method='POST',
        schema=ATTACK_SCHEMA
    )

    print(doc.as_object())

Output::

    {
        "_forms": {
            "attack": {
                "headers": {
                    "Content-Type": "application/json"
                },
                "href": "/attacks",
                "method": "POST",
                "schema": {
                    "required": [
                        "name",
                        "damage"
                    ],
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "damage": {
                            "minimum": 0,
                            "type": "integer",
                            "description": "How much does it hurt?"
                        }
                    },
                    "title": "Damage Schema"
                }
            }
        },
        "_links": {
            "self": {
                "href": "/foo"
            }
        }
    }


API
===

By mixing in ``FormMixin`` into your document, you get three new methods:

    * ``set_form(self, rel, target, **kwargs)``
    * ``delete_form(self, rel)``
    * ``form(self, href, **kwargs)``

Until real docs have been written, take a look at
`the source <https://github.com/weluse/dougrain-forms/blob/master/dougrain_forms/mixin.py>`_.
