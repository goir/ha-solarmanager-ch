"""Constants for solar_manager."""
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "Solar Manager"
DOMAIN = "solarmanagerch"
VERSION = "0.1.0"
ATTRIBUTION = "Data provided by SolarManager.ch"

CONF_SMART_MANAGER_ID = "smid"