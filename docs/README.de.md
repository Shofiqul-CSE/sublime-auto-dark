# `auto-dark` Erweiterung für [Sublime Text](https://www.sublimetext.com)

> Automatischer "dark mode", der deine Sublime Color Schemes aufgrund des Aussehens deines Operationssystems ändert.

* [Voraussetzungen](#voraussetzungen)
* [Installation](#installation)
    * [Installation über Package Control](#installation-über-package-control)
* [Verwendung](#verwendung)
* [Quellcode](#quellcode)
    * [Lizenz](#lizenz)
        * [Danksagungen](#danksagungen)
    * [Feedback](#feedback)
* [Spenden](#spenden)

## Voraussetzungen

print ist als Erweiterung für die **neusten Build** von Sublime Text gedacht und erfordert im Moment **`Build 4065+`** oder **`Build 3006+`**.

* Lade [Sublime Text](https://www.sublimetext.com) herunter
    * (stable channel)
    * (dev channel)

## Installation

Die Verwendung von **Package Control** wird nicht zwingend vorausgesetzt, aber durchaus empfohlen, da es deine Erweiterungen (mit ihren Abhängigkeiten) aktuell hält.

### Installation über Package Control

* [Installiere Package Control](https://packagecontrol.io/installation)
    * Schließe und öffne Sublime Text nach der Installation von Package Control.
* Öffne die Befehlseingabe (`Tools > Command Palette`).
* Wähle `Package Control: Install Package`.
* Suche nach [`auto-dark` in Package Control](https://packagecontrol.io/packages/auto-dark) und wähle die Erweiterung aus, um sie zu installieren.

## Verwendung

Wechsle automatisch Sublime Color Schemes mit dem Aussehen deines Operationssystems:

* beim Wechseln von Tabs innerhalb oder beim Wechseln zu Sublime
* oder alle 5 Min (auf der Uhr)

`auto-dark` kopiert:

* `color_scheme.light`
* oder `color_scheme.dark`

zu dem Zeitpunkt zu `color_scheme` in `Preferences.sublime-settings`.
Du kannst dafür auch den Name der Ressource anstatt des vollen (lokalen) Pfads verwenden.

## Quellcode

[github.com/jrappen/sublime-auto-dark](https://www.github.com/jrappen/sublime-auto-dark)

### Lizenz

Copyright (c) 2020 Johannes Rappen, ISC Lizenz

Siehe [`jrappen/sublime-auto-dark:LICENSE@master`](https://github.com/jrappen/sublime-auto-dark/blob/master/LICENSE).

#### Danksagungen

> Copyright (c) 2016 Deathaxe, MIT Lizenz
>
> Siehe [`deathaxe/sublime-clock:clock.py@master`](https://github.com/deathaxe/sublime-clock/blob/master/clock.py).

### Feedback

Verwende für Feedback bitte die Befehlseingabe (command palette) oder das Menü.

## Spenden

[paypal.me/jrappen](https://www.paypal.me/jrappen)
