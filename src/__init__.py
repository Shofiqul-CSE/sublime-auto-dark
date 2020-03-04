#!/usr/bin/env python
# coding: utf-8


import sublime

from .auto_dark import *
from .window_commands import *


def plugin_loaded():
    auto_dark.plugin_loaded()
