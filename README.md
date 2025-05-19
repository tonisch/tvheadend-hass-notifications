# TVHeadend Notify

Home Assistant Custom Integration für Benachrichtigungen über neue und abgeschlossene TVHeadend-Aufnahmen.

## Features
- Sensor-Entity für neue und abgeschlossene Aufnahmen
- Konfiguration über die Home Assistant UI
- Automatisierbare Benachrichtigungen

## Installation über HACS

1. Repository auf GitHub veröffentlichen (z.B. als `tvheadend-hass-notifications`).
2. In Home Assistant → HACS → Integrationen → "Custom Repository" hinzufügen:
   - URL deines Repos angeben
   - Typ: Integration
3. Nach kurzer Zeit erscheint "TVHeadend Notify" in HACS und kann installiert werden.
4. Nach Installation Home Assistant neu starten und Integration wie gewohnt einrichten.

## Manuelle Installation

1. Kopiere den Ordner `custom_components/tvheadend_notify` in dein Home Assistant `custom_components`-Verzeichnis.
2. Starte Home Assistant neu.
3. Integration über die Oberfläche hinzufügen und Zugangsdaten eingeben.

## Konfiguration
Die Integration wird komplett über die UI eingerichtet (TVHeadend-URL, Benutzername, Passwort).

## Automatisierung
Lege eine Automation an, die auf Statusänderungen des Sensors reagiert und Benachrichtigungen verschickt.

---

MIT License 