#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin

import datetime
import platform


def plugin_loaded():
    AutoDark.start()


def plugin_unloaded():
    AutoDark.stop()


class EventListener(sublime_plugin.EventListener):

    def on_activated(self, view):
        AutoDark.paint(view)


class AutoDark(object):

    running = False

    @classmethod
    def start(cls):
        if sublime.platform() == 'osx':
            from distutils.version import LooseVersion as V
            if V(platform.mac_ver()[0]) < V('10.14'):
                return
            # else:
                # pass
        elif sublime.platform() == 'linux':
            return
        # else:
            # pass
        cls.running = True
        cls._tick()

    @classmethod
    def stop(cls):
        cls.running = False

    @classmethod
    def paint(cls, view):
        try:
            PREF = sublime.load_settings('Preferences.sublime-settings')
            if sublime.platform() == 'osx':
                from .detect_macos import isDark
                IS_DARK = isDark()
            else:
                from .detect_win import isDark
                IS_DARK = isDark()
            if IS_DARK:
                # TODO: check default value for color_scheme
                CS_NOW = PREF.get('color_scheme')
                CS_NEW = PREF.get('color_scheme.dark', 'Mariana.sublime-color-scheme')
            else:
                # TODO: check default value for color_scheme
                CS_NOW = PREF.get('color_scheme')
                CS_NEW = PREF.get('color_scheme.light', 'Breakers.sublime-color-scheme')
            if CS_NOW != CS_NEW:
                PREF.set('color_scheme', CS_NEW)
                sublime.save_settings('Preferences.sublime-settings')
        except Exception as e:
            print('AutoDark: Error: ', e)

    @classmethod
    def _tick(cls):
        try:
            if cls.running:
                sublime.set_timeout_async(cls._tick, cls._update())
        except Exception as e:
            print('AutoDark: Error: ', e)
            cls.stop()

    @classmethod
    def _update(cls):
        now = datetime.datetime.now()
        try:
            cls.paint()
        except Exception as e:
            pass
        # every 5 mins max
        return 60000 * (4 - now.minute % 5) + 1000 * (60 - now.second)
