"""Config flow for SolarMAN logger integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from voluptuous.schema_builder import Schema

from homeassistant import config_entries
from homeassistant.core import HomeAssistant, callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError

from homeassistant.const import (EVENT_HOMEASSISTANT_STOP, CONF_NAME, CONF_SCAN_INTERVAL, CONF_USERNAME, CONF_PASSWORD)
from .const import *

_LOGGER = logging.getLogger(__name__)


def step_user_data_schema(data: dict[str, Any] = {CONF_NAME: "Name", CONF_USERNAME: "Username", CONF_PASSWORD: "Password", CONF_SMART_MANAGER_ID: "smid"}) -> Schema:
    _LOGGER.debug(f'config_flow.py:step_user_data_schema: {data}')
    STEP_USER_DATA_SCHEMA = vol.Schema(
        {
            vol.Required(CONF_NAME, default=data.get(CONF_NAME)): str,
            vol.Required(CONF_USERNAME, default=data.get(CONF_USERNAME)): str,
            vol.Required(CONF_PASSWORD, default=data.get(CONF_PASSWORD)): str,
            vol.Required(CONF_SMART_MANAGER_ID, default=data.get(CONF_SMART_MANAGER_ID)): str
        },
        extra=vol.PREVENT_EXTRA
    )
    _LOGGER.debug(
        f'config_flow.py:step_user_data_schema: STEP_USER_DATA_SCHEMA: {STEP_USER_DATA_SCHEMA}')
    return STEP_USER_DATA_SCHEMA


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """
    Validate the user input allows us to connect.

    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """

    _LOGGER.debug(f'config_flow.py:validate_input: {data}')

    # try:
    #     getaddrinfo(
    #         data[CONF_INVERTER_HOST], data[CONF_INVERTER_PORT], family=0, type=0, proto=0, flags=0
    #     )
    # except herror:
    #     raise InvalidHost
    # except gaierror:
    #     raise CannotConnect
    # except timeout:
    #     raise CannotConnect

    return {"title": data[CONF_NAME]}


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for SolarMAN logger."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(entry: config_entries.ConfigEntry) -> OptionsFlow:
        """Get the options flow for this handler."""
        _LOGGER.debug(f'config_flow.py:ConfigFlow.async_get_options_flow: {entry}')
        return OptionsFlow(entry)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        _LOGGER.debug(f'config_flow.py:ConfigFlow.async_step_user: {user_input}')
        """Handle the initial step."""
        if user_input is None:
            return self.async_show_form(
                step_id="user", data_schema=step_user_data_schema()
            )

        errors = {}

        try:
            info = await validate_input(self.hass, user_input)
        except InvalidHost:
            errors["base"] = "invalid_host"
        except CannotConnect:
            errors["base"] = "cannot_connect"
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Unexpected exception")
            errors["base"] = "unknown"
        else:
            _LOGGER.debug(f'config_flow.py:ConfigFlow.async_step_user: validation passed: {user_input}')
            # await self.async_set_unique_id(user_input.device_id) # not sure this is permitted as the user can change the device_id
            # self._abort_if_unique_id_configured()
            return self.async_create_entry(
                title=info["title"], data=user_input, options=user_input
            )

        _LOGGER.debug(f'config_flow.py:ConfigFlow.async_step_user: validation failed: {user_input}')

        return self.async_show_form(
            step_id="user",
            data_schema=step_user_data_schema(user_input),
            errors=errors,
        )


class OptionsFlow(config_entries.OptionsFlow):
    """Handle options."""

    def __init__(self, entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        _LOGGER.debug(f'config_flow.py:OptionsFlow.__init__: {entry}')
        self.entry = entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        _LOGGER.debug(f'config_flow.py:OptionsFlow.async_step_init: {user_input}')
        if user_input is None:
            return self.async_show_form(
                step_id="init",
                data_schema=step_user_data_schema(self.entry.options),
            )

        errors = {}

        try:
            info = await validate_input(self.hass, user_input)
        except InvalidHost:
            errors["base"] = "invalid_host"
        except CannotConnect:
            errors["base"] = "cannot_connect"
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Unexpected exception")
            errors["base"] = "unknown"
        else:
            return self.async_create_entry(title=info["title"], data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=step_user_data_schema(user_input),
            errors=errors,
        )


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidHost(HomeAssistantError):
    """Error to indicate there is invalid hostname or IP address."""
