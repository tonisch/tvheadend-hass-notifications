# TVHeadend Notify

Home Assistant Custom Integration for notifications about new and completed TVHeadend recordings.

## Features
- Sensor entity for new and completed recordings
- Configuration via Home Assistant UI
- Automatable notifications

## Installation via HACS

1. Publish the repository on GitHub (e.g., as `tvheadend-hass-notifications`).
2. In Home Assistant → HACS → Integrations → "Custom Repository":
   - Enter your repository URL
   - Type: Integration
3. After a short time, "TVHeadend Notify" will appear in HACS and can be installed.
4. After installation, restart Home Assistant and set up the integration as usual.

## Manual Installation

1. Copy the folder `custom_components/tvheadend_notify` into your Home Assistant `custom_components` directory.
2. Restart Home Assistant.
3. Add the integration via the UI and enter your credentials.

## Configuration
The integration is fully configured via the UI (TVHeadend URL, username, password).

## Automation
Create an automation that reacts to changes in the sensor's state and sends notifications.

---

MIT License 