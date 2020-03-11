[![License](https://img.shields.io/github/license/jrappen/sublime-auto-dark.svg?style=flat-square)](https://github.com/jrappen/sublime-auto-dark/blob/master/LICENSE)
[![Required ST Build](https://img.shields.io/badge/ST-Build%204065+-orange.svg?style=flat-square&logo=sublime-text)](https://www.sublimetext.com)
[![Downloads Package Control](https://img.shields.io/packagecontrol/dt/auto-dark.svg?style=flat-square)](https://packagecontrol.io/packages/auto-dark)
[![Latest tag](https://img.shields.io/github/tag/jrappen/sublime-auto-dark.svg?style=flat-square&logo=github)](https://github.com/jrappen/sublime-auto-dark/tags)
[![Donate via PayPal](https://img.shields.io/badge/paypal.me-jrappen-009cde.svg?style=flat-square&logo=paypal)](https://www.paypal.me/jrappen)
[![SublimeHQ Discord](https://img.shields.io/discord/280102180189634562?label=SublimeHQ%20Discord&logo=discord&style=flat-square)](https://discord.gg/D43Pecu)

# `auto-dark` plug-in for [Sublime Text](https://www.sublimetext.com)

> Automatically switch Sublime Color Schemes with your operating system's appearance.

## Documentation

### English 🇺🇸🇬🇧🇨🇦🇦🇺🇳🇿

> Plugin documentation is available in English via the menu or command palette.

[`jrappen/sublime-auto-dark:docs/README.en.md@master`](https://github.com/jrappen/sublime-auto-dark/blob/master/docs/README.en.md)

### German (Deutsch) 🇩🇪🇦🇹🇨🇭

> Eine plug-in Dokumentation ist über das Menü oder die Kurzbefehleingabe (command palette) verfügbar.

[`jrappen/sublime-auto-dark:docs/README.de.md@master`](https://github.com/jrappen/sublime-auto-dark/blob/master/docs/README.de.md)

## Requirements

auto-dark targets and is tested against the **latest Build** of Sublime Text, currently requiring **`Build 4065`** or later.

* Download [Sublime Text](https://www.sublimetext.com)
    * (stable channel)
    * (dev channel)

## Installation

Using **Package Control** is not required, but recommended as it keeps your packages (with their dependencies) up-to-date!

### Installation via Package Control

* [Install Package Control](https://packagecontrol.io/installation)
    * Close and reopen Sublime Text after having installed Package Control.
* Open the Command Palette (`Tools > Command Palette`).
* Choose `Package Control: Install Package`.
* Search for [`auto-dark` on Package Control](https://packagecontrol.io/packages/auto-dark) and select to install.

## Usage

Automatically switch Sublime Color Schemes with your operating system's appearance:

* when switching tabs within or switching to Sublime
* or every 5 mins (on the clock)

`auto-dark` will copy:

* `color_scheme.light`
* or `color_scheme.dark`

to `color_scheme` in `Preferences.sublime-settings` at that time.
You can use the resource name instead of its full (local) resource path.

## Source Code

[github.com/jrappen/sublime-auto-dark](https://www.github.com/jrappen/sublime-auto-dark)

### License

See [`LICENSE`](https://github.com/jrappen/sublime-auto-dark/blob/master/LICENSE).

#### Acknowledgements

> [`deathaxe/sublime-clock:clock.py@master`](https://github.com/deathaxe/sublime-clock/blob/master/clock.py)
>
> Copyright (c) 2016 Deathaxe, MIT License

### Issues

Please use the command palette or the main menu to report an issue.

## Donations

[paypal.me/jrappen](https://www.paypal.me/jrappen)
