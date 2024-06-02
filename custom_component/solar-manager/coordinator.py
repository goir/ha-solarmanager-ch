import datetime
import logging
from datetime import timedelta
from typing import Callable, Awaitable, Coroutine, Any

from homeassistant.components.rainmachine import CONF_SOLARRAD
from homeassistant.const import CONF_USERNAME, CONF_PASSWORD
from homeassistant.core import HomeAssistant
from homeassistant.helpers.debounce import Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, _DataT
from .openapi_client import ApiClient, Configuration, CustomerApi, UserApi, GetOverviewApi, DataApi, \
    SensorApi, GetStatisticsOfTheGatewayApi

from const import CONF_SMART_MANAGER_ID

_LOGGER = logging.getLogger(__name__)


class SolarUpdateCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, config, logger: logging.Logger, *, name: str,
                 update_interval: timedelta | None = None, update_method: Callable[[], Awaitable[_DataT]] | None = None,
                 request_refresh_debouncer: Debouncer[Coroutine[Any, Any, None]] | None = None) -> None:
        super().__init__(hass, logger, name=name, update_interval=timedelta(seconds=10))

        _LOGGER.debug("SOLAR: INIT COORDINATOR with cfg: {}".format(config))

        conf = Configuration(host="https://cloud.solar-manager.ch",
                             username=config[CONF_USERNAME],
                             password=config[CONF_PASSWORD])

        self.sm_id = config[CONF_SMART_MANAGER_ID]

        client = ApiClient(configuration=conf)
        self.gateway_api = DataApi(client)
        self.sensor_api = SensorApi(client)

    def _update_all(self):
        gateway_data = self.gateway_api.get_v1_stream_gateway_smid(sm_id=self.sm_id)
        device_data = self.sensor_api.get_v1_info_sensors_smid(sm_id=self.sm_id)

        return {'gateway': gateway_data, 'device_info': device_data}

    async def _async_update_data(self) -> _DataT:
        _LOGGER.debug("SOLAR: update data")
        return await self.hass.async_add_executor_job(self._update_all)


class SolarManagerStatisticsUpdateCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, config, logger: logging.Logger, *, name: str,
                 update_interval: timedelta | None = None, update_method: Callable[[], Awaitable[_DataT]] | None = None,
                 request_refresh_debouncer: Debouncer[Coroutine[Any, Any, None]] | None = None) -> None:
        super().__init__(hass, logger, name=name, update_interval=timedelta(minutes=5))

        _LOGGER.debug("SOLAR: INIT COORDINATOR with cfg: {}".format(config))

        conf = Configuration(host="https://cloud.solar-manager.ch",
                             username=config[CONF_USERNAME],
                             password=config[CONF_PASSWORD])

        self.sm_id = config[CONF_SMART_MANAGER_ID]

        client = ApiClient(configuration=conf)
        self.gateway_api = GetStatisticsOfTheGatewayApi(client)

    def _update_all(self):
        today_start = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = datetime.datetime.now().replace(hour=23, minute=59, second=59, microsecond=999)
        gateway_data = self.gateway_api.get_v1_statistics_gateways_smid(self.sm_id, "high", today_start, today_end)

        _LOGGER.debug("SOLAR statistics data: {}".format(gateway_data))

        return gateway_data

    async def _async_update_data(self) -> _DataT:
        _LOGGER.debug("SOLAR: update SolarManagerStatisticsUpdateCoordinator")
        return await self.hass.async_add_executor_job(self._update_all)
