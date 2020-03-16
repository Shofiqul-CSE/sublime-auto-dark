#!/usr/bin/env python
# coding: utf-8


import sublime

from .auto_dark import *


def plugin_loaded():
    if 3189 <= int(sublime.version()):
        auto_dark.plugin_loaded()

def plugin_unloaded():
    if 3189 <= int(sublime.version()):
        auto_dark.plugin_unloaded()
