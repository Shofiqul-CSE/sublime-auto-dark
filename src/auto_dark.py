#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin


def plugin_loaded():
    AutoDark.start()


def plugin_unloaded():
    AutoDark.stop()


class EventListener(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        AutoDark.paint()


class AutoDark(object):

    running = False

    @classmethod
    def has_dark_mode_support():
        current_pf = sublime.platform()
        if current_pf == 'osx':
            from distutils.version import LooseVersion as V
            import platform
            if V(platform.mac_ver()[0]) < V('10.14'):
                return False
        elif current_pf == 'linux':
            return False
        return True

    @classmethod
    def start(cls):
        if not cls.has_dark_mode_support():
            return
        cls.running = True
        cls._tick()

    @classmethod
    def stop(cls):
        cls.running = False

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

    @classmethod
    def paint(cls):
        try:
            PREF = sublime.load_settings('Preferences.sublime-settings')
            current_pf = sublime.platform()
            IS_DARK = False if current_pf == 'linux' else cls.is_dark_os()
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
    def is_dark_os(cls):
        current_pf = sublime.platform()
        if current_pf == 'osx':
            try:
                get_status = 'defaults read -g AppleInterfaceStyle'
                import subprocess
                status = subprocess.check_output(
                    get_status.split(),
                    stderr = subprocess.STDOUT
                ).decode()
                status = status.replace('\n', '')
            except subprocess.CalledProcessError as e:
                return False
            return True if status.lower() == 'dark' else False
        elif current_pf == 'windows':
            value = 1 # default to light theme
            try:
                import winreg
                with winreg.ConnectRegistry(
                    None,
                    winreg.HKEY_CURRENT_USER
                ) as registry:
                    with winreg.OpenKey(
                        registry,
                        'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize'
                    ) as key:
                        value, value_type = winreg.QueryValueEx(key, 'AppsUseLightTheme')
            except Exception as e:
                pass
            return value > 0
        else:
            return False
