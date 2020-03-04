#!/usr/bin/env python
# coding: utf-8


def isDark():
    try:
        import winreg
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(registry, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize')
        mode = winreg.QueryValueEx(key, 'AppsUseLightTheme')
        IS_DARK = not bool(mode[0])
    except Exception as e:
        print('AutoDark: Error: ', e)
        IS_DARK = False
    return IS_DARK
