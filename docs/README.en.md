# `auto-dark` plug-in for [Sublime Text](https://www.sublimetext.com)

> Automatic dark mode, switches your Sublime Color Schemes according to your operating system's appearance.

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
