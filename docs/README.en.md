# `auto-dark` plug-in for [Sublime Text](https://www.sublimetext.com)

> Automatic dark mode, switches Sublime Text's UI according to your operating system's appearance.

* [Requirements](#requirements)
* [Installation](#installation)
    * [Installation via Package Control](#installation-via-package-control)
* [Usage](#usage)
* [Source Code](#source-code)
    * [License](#license)
        * [Acknowledgements](#acknowledgements)
    * [Issues](#issues)
* [Donations](#donations)

## Requirements

auto-dark targets and is tested against the **latest Build** of Sublime Text, currently requiring **`Build 4065+`** or **`Build 3006+`**.

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

Automatically switch Sublime Text's UI with your operating system's appearance:

* when switching tabs within or switching to Sublime
* or every 5 mins (on the clock)

`auto-dark` will copy:

* `color_scheme.light`
* or `color_scheme.dark`

to `color_scheme` as well as:

* `theme.light`
* or `theme.dark`

to `theme` in `Preferences.sublime-settings` at that time.
You can use the resource name instead of its full (local) resource path.

## Source Code

[github.com/jrappen/sublime-auto-dark](https://www.github.com/jrappen/sublime-auto-dark)

### License

Copyright (c) 2020 Johannes Rappen, ISC License

See [`jrappen/sublime-auto-dark:LICENSE@master`](https://github.com/jrappen/sublime-auto-dark/blob/master/LICENSE).

#### Acknowledgements

> Copyright (c) 2016 Deathaxe, MIT License
>
> See [`deathaxe/sublime-clock:clock.py@master`](https://github.com/deathaxe/sublime-clock/blob/master/clock.py).

### Issues

Please use the command palette or the main menu to report an issue.

## Donations

[paypal.me/jrappen](https://www.paypal.me/jrappen)
