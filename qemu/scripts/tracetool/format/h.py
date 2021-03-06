#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Generate .h file.
"""

__author__     = "Lluís Vilanova <vilanova@ac.upc.edu>"
__copyright__  = "Copyright 2012, Lluís Vilanova <vilanova@ac.upc.edu>"
__license__    = "GPL version 2 or (at your option) any later version"

__maintainer__ = "Stefan Hajnoczi"
__email__      = "stefanha@linux.vnet.ibm.com"


from tracetool import out


def begin(events):
    out('/* This file is autogenerated by tracetool, do not edit. */',
        '',
        '#ifndef TRACE__GENERATED_TRACERS_H',
        '#define TRACE__GENERATED_TRACERS_H',
        '',
        '#include "qemu-common.h"')

def end(events):
    out('#endif /* TRACE__GENERATED_TRACERS_H */')

def nop(events):
    for e in events:
        out('',
            'static inline void trace_%(name)s(%(args)s)',
            '{',
            '}',
            name = e.name,
            args = e.args,
            )
