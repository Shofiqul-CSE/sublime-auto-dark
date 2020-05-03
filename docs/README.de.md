# `auto-dark` Erweiterung für [Sublime Text](https://www.sublimetext.com)

> Automatischer "dark mode", der das Sublime Text UI aufgrund des Aussehens deines Operationssystems ändert.

* [Dokumentation](#dokumentation)
* [Voraussetzungen](#voraussetzungen)
* [Installation](#installation)
* [Verwendung](#verwendung)
* [Quellcode](#quellcode)
* [Spenden](#spenden)

## Dokumentation

> Eine plug-in Dokumentation ist über das Menü oder die Kurzbefehleingabe (command palette) verfügbar.

* Englisch (English):
  <https://github.com/jrappen/sublime-auto-dark/blob/master/docs/README.en.md>
* Deutsch:
  <https://github.com/jrappen/sublime-auto-dark/blob/master/docs/README.de.md>

### Code of conduct

> ist in den **default community health files** zu finden

<https://github.com/jrappen/.github/blob/master/CODE_OF_CONDUCT.md>

### Contributing guide

> ist in den **default community health files** zu finden

<https://github.com/jrappen/.github/blob/master/CONTRIBUTING.md>

## Voraussetzungen

print ist als Erweiterung für die **neusten Build** von Sublime Text gedacht und erfordert im Moment **`Build 4074+`** oder **`Build 3006+`**.

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

Wechsle automatisch das Sublime Text UI mit dem Aussehen deines Operationssystems:

* beim Wechseln von Tabs innerhalb oder beim Wechseln zu Sublime
* oder alle 5 Min (auf der Uhr)

`auto-dark` kopiert hierbei:

* `color_scheme.light`
* oder `color_scheme.dark`

zu `color_scheme` sowie:

* `theme.light`
* oder `theme.dark`

zu `theme` zu jenem Zeitpunkt in `Preferences.sublime-settings`.
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
