# -*- coding: utf-8 -*-
try:
    from .local import *
except ImportError:
    from .default import *
