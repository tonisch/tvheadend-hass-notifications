# sensor.py für TVHeadend Notify 
import logging
from datetime import timedelta
import requests
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_URL, CONF_USERNAME, CONF_PASSWORD
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator
from .const import DOMAIN, DEFAULT_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = TVHeadendCoordinator(hass, entry.data)
    await coordinator.async_config_entry_first_refresh()
    async_add_entities([TVHeadendRecordingSensor(coordinator)])

class TVHeadendCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, config):
        super().__init__(
            hass,
            _LOGGER,
            name="TVHeadend Recording Sensor",
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.url = config[CONF_URL]
        self.username = config[CONF_USERNAME]
        self.password = config[CONF_PASSWORD]
        self._last_ids = set()

    def _fetch_recordings(self):
        try:
            resp = requests.get(
                f"{self.url}/api/dvr/entry/grid",
                auth=(self.username, self.password),
                timeout=10
            )
            resp.raise_for_status()
            return resp.json().get("entries", [])
        except Exception as e:
            _LOGGER.error(f"TVHeadend API error: {e}")
            return []

    async def _async_update_data(self):
        return await self.hass.async_add_executor_job(self._fetch_recordings)

class TVHeadendRecordingSensor(CoordinatorEntity, SensorEntity):
    _attr_name = "TVHeadend Aufnahme Status"
    _attr_icon = "mdi:television-box"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._state = None
        self._attr_extra_state_attributes = {}
        self._last_seen_ids = set()

    @property
    def state(self):
        entries = self.coordinator.data or []
        new_recordings = [e for e in entries if e.get("state") == "recording"]
        finished_recordings = [e for e in entries if e.get("state") == "completed"]
        if new_recordings:
            self._state = f"Neue Aufnahme: {new_recordings[0].get('disp_title', 'Unbekannt')}"
        elif finished_recordings:
            self._state = f"Abgeschlossen: {finished_recordings[0].get('disp_title', 'Unbekannt')}"
        else:
            self._state = "Keine neuen Aufnahmen"
        return self._state

    @property
    def extra_state_attributes(self):
        return {
            "recording_count": len([e for e in (self.coordinator.data or []) if e.get("state") == "recording"]),
            "finished_count": len([e for e in (self.coordinator.data or []) if e.get("state") == "completed"]),
        } 