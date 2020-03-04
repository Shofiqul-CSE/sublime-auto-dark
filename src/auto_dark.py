#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin


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
    def is_dark_macos(cls):
        try:
            get_status = 'defaults read -g AppleInterfaceStyle'
            import subprocess
            status = subprocess.check_output(get_status.split(), stderr=subprocess.STDOUT).decode()
            status = status.replace('\n', '')
        except subprocess.CalledProcessError:
            return False
        if status == 'Dark':
            return True
        else:
            return False

    @classmethod
    def is_dark_windows(cls):
        import winreg
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(registry, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize')
        mode = winreg.QueryValueEx(key, 'AppsUseLightTheme')
        return not bool(mode[0])

    @classmethod
    def start(cls):
        if sublime.platform() == 'osx':
            from distutils.version import LooseVersion as V
            import platform
            if V(platform.mac_ver()[0]) < V('10.14'):
                return
        elif sublime.platform() == 'linux':
            return
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
                IS_DARK = cls.is_dark_macos()
            elif sublime.platform() == 'windows':
                IS_DARK = cls.is_dark_windows()
            else:
                IS_DARK = False
            CS_NOW = PREF.get('color_scheme', 'Monokai.sublime-color-scheme')
            if IS_DARK:
                CS_NEW = PREF.get('color_scheme.dark', 'Mariana.sublime-color-scheme')
            else:
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
        import datetime
        now = datetime.datetime.now()
        try:
            cls.paint()
        except Exception as e:
            pass
        # every 5 mins max
        return 60000 * (4 - now.minute % 5) + 1000 * (60 - now.second)
