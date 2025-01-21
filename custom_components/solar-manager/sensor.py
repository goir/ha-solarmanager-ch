import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass, SensorEntityDescription
from homeassistant.const import UnitOfTemperature, UnitOfEnergy, UnitOfPower, PERCENTAGE
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.config_entries import ConfigEntry

from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator

from .coordinator import SolarUpdateCoordinator, SolarManagerStatisticsUpdateCoordinator
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

# Set-up from configuration.yaml
async def async_setup_platform(hass: HomeAssistant, config, async_add_entities: AddEntitiesCallback, discovery_info=None):
    _LOGGER.debug(f'sensor.py:async_setup_platform: {config}')
    await _do_setup_platform(hass, config, async_add_entities)


# Set-up from the entries in config-flow
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    _LOGGER.debug(f'sensor.py:async_setup_entry: {entry.options}')
    await _do_setup_platform(hass, entry.options, async_add_entities)


async def _do_setup_platform(hass: HomeAssistant, config, async_add_entities: AddEntitiesCallback, discovery_info=None):
    _LOGGER.debug(f'sensor.py:async_setup_platform: {config}')

    coordinator = SolarUpdateCoordinator(hass, config, _LOGGER, name=DOMAIN)
    await coordinator.async_refresh()
    await coordinator.async_config_entry_first_refresh()
    
    coordinator2 = SolarManagerStatisticsUpdateCoordinator(hass, config, _LOGGER, name=DOMAIN)
    await coordinator2.async_refresh()
    await coordinator2.async_config_entry_first_refresh()

    async_add_entities([EnergySensor(coordinator2, "consumption"),
                        EnergySensor(coordinator2, "production"),
                        EnergySensor(coordinator2, "self_consumption"),
                        EnergySensorPerc(coordinator2, "self_consumption_rate"),
                        EnergySensorPerc(coordinator2, "autarchy_degree")])

    sensors = []

    sensors.extend([PowerSensor(coordinator, 'current_power_consumption'),
                    PowerSensor(coordinator, 'current_pv_generation'),
                    PowerSensor(coordinator, 'current_battery_charge_discharge'),
                    PowerSensor(coordinator, 'current_grid_power'),
                    BatterySensor(coordinator, 'soc')])
    async_add_entities(sensors)


class SolarManagerDeviceSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator: DataUpdateCoordinator, device_info: DeviceInfo, attr: str, device_id: str) -> None:
        super().__init__(coordinator, None)

        self._device_info = device_info
        self._attr = attr
        self._device_id = device_id
        self.entity_description = SensorEntityDescription(key=self.unique_id, 
                                                          device_class=SensorDeviceClass.POWER, 
                                                          native_unit_of_measurement=UnitOfPower.WATT, 
                                                          state_class=SensorStateClass.MEASUREMENT)

    @property
    def device_info(self) -> DeviceInfo | None:
        return self._device_info

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        device_data = next((x for x in self.coordinator.data['gateway'].devices if x.id == self._device_id))
        self._attr_native_value = getattr(device_data, self._attr)
        self.async_write_ha_state()

    # @property
    # def icon(self):
    #     #  Return the icon of the sensor. """
    #     return self.p_icon

    @property
    def name(self):
        #  Return the name of the sensor.
        return "{}_{}".format(DOMAIN, self._attr)

    @property
    def unique_id(self):
        # Return a unique_id based on the serial number
        return "{}_{}_{}".format(DOMAIN, self._device_id, self._attr)


class SolarManagerDeviceTemperatureSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator: DataUpdateCoordinator, device_info: DeviceInfo, attr: str, device_id: str) -> None:
        super().__init__(coordinator, None)

        self._device_info = device_info
        self._attr = attr
        self._device_id = device_id
        self.entity_description = SensorEntityDescription(key=self.name, 
                                                          device_class=SensorDeviceClass.TEMPERATURE, 
                                                          native_unit_of_measurement=UnitOfTemperature.CELSIUS, 
                                                          state_class=SensorStateClass.MEASUREMENT)

    @property
    def device_info(self) -> DeviceInfo | None:
        return self._device_info

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        device_data = next((x for x in self.coordinator.data['gateway'].devices if x.id == self._device_id))
        self._attr_native_value = getattr(device_data, self._attr)
        self.async_write_ha_state()

    # @property
    # def icon(self):
    #     #  Return the icon of the sensor. """
    #     return self.p_icon

    @property
    def name(self):
        #  Return the name of the sensor.
        return "{}_{}".format(DOMAIN, self._attr)

    @property
    def unique_id(self):
        # Return a unique_id based on the serial number
        return "{}_{}_{}".format(DOMAIN, self._device_id, self._attr)

class SolarManagerSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator: DataUpdateCoordinator, context: Any = None) -> None:
        super().__init__(coordinator, context)

    @property
    def device_info(self):
        _LOGGER.info("SOLAR: device_info")
        """Return the device info."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self.device_id)
            },
            name="Solar Manager",
            model="Solar Manager",
            manufacturer="manufacturer"
        )

class PowerSensor(SolarManagerSensor):
    def __init__(self, coordinator: DataUpdateCoordinator, context: Any = None) -> None:
        super().__init__(coordinator, context)

        self.context = context
        self.device_id = "overall"
        self.entity_description = SensorEntityDescription(key=self.unique_id, 
                                                          device_class=SensorDeviceClass.POWER, 
                                                          native_unit_of_measurement=UnitOfPower.WATT, 
                                                          state_class=SensorStateClass.MEASUREMENT)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_native_value = getattr(self.coordinator.data['gateway'], self.context)
        self.async_write_ha_state()

    # @property
    # def icon(self):
    #     #  Return the icon of the sensor. """
    #     return self.p_icon

    @property
    def name(self):
        #  Return the name of the sensor.
        return "{}_{}".format("overall", self.context)

    @property
    def unique_id(self):
        _LOGGER.info("SOLAR: unique_id {}_{}".format("overall", self.context))
        # Return a unique_id based on the serial number
        return "{}_{}".format("overall", self.context)


class BatterySensor(SolarManagerSensor):
    def __init__(self, coordinator: DataUpdateCoordinator, context: Any = None) -> None:
        super().__init__(coordinator, context)

        self.context = context
        self.entity_description = SensorEntityDescription(key=self.context, 
                                                          device_class=SensorDeviceClass.BATTERY, 
                                                          native_unit_of_measurement=PERCENTAGE, 
                                                          state_class=SensorStateClass.MEASUREMENT, 
                                                          name=self.context)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_native_value = getattr(self.coordinator.data['gateway'], self.context)
        self.async_write_ha_state()


class EnergySensor(SolarManagerSensor):
    def __init__(self, coordinator: DataUpdateCoordinator, context: Any = None) -> None:
        super().__init__(coordinator, context)

        self.context = context
        self.entity_description = SensorEntityDescription(key=self.context, 
                                                          device_class=SensorDeviceClass.ENERGY, 
                                                          native_unit_of_measurement=UnitOfEnergy.WATT_HOUR, 
                                                          state_class=SensorStateClass.TOTAL_INCREASING, 
                                                          name=self.context)
        self.device_id = "statistics"
        # set initial value
        self._set_value()

    def _set_value(self):
        self._attr_native_value = getattr(self.coordinator.data, self.context)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._set_value()
        self.async_write_ha_state()

    @property
    def name(self):
        #  Return the name of the sensor.
        return "{}_{}".format(DOMAIN, self.context)

    @property
    def unique_id(self):
        _LOGGER.info("SOLAR: unique_id {}_{}".format("statistic", self.context))
        # Return a unique_id based on the serial number
        return "{}_{}_{}".format(DOMAIN, "statistic", self.context)


class EnergySensorPerc(SolarManagerSensor):
    def __init__(self, coordinator: DataUpdateCoordinator, context: Any = None) -> None:
        super().__init__(coordinator, context)

        self.context = context
        self.entity_description = SensorEntityDescription(key=self.context, 
                                                          device_class=SensorDeviceClass.POWER_FACTOR, 
                                                          native_unit_of_measurement=PERCENTAGE, 
                                                          state_class=SensorStateClass.MEASUREMENT, 
                                                          name=self.context)
        self.device_id = "statistics"
        # set initial value
        self._set_value()

    def _set_value(self):
        self._attr_native_value = getattr(self.coordinator.data, self.context)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._set_value()
        self.async_write_ha_state()

    @property
    def name(self):
        #  Return the name of the sensor.
        return "{}_{}".format(DOMAIN, self.context)

    @property
    def unique_id(self):
        _LOGGER.info("SOLAR: unique_id {}_{}".format("statistic", self.context))
        # Return a unique_id based on the serial number
        return "{}_{}_{}".format(DOMAIN, "statistic", self.context)


class GridPowerSensor(PowerSensor):
    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_native_value = self.coordinator.data['gateway'].current_pv_generation - self.coordinator.data['gateway'].current_power_consumption - self.coordinator.data['gateway'].current_battery_charge_discharge
        self.async_write_ha_state()
