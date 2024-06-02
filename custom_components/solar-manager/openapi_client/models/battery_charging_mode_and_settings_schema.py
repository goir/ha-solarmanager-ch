# coding: utf-8

"""
    Solar Manager external API 

    This is a Solar Manager external communication service

    The version of the OpenAPI document: 1.19.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, confloat, conint

class BatteryChargingModeAndSettingsSchema(BaseModel):
    """
    BatteryChargingModeAndSettingsSchema
    """
    battery_charging_mode: Optional[conint(strict=True, le=4, ge=0)] = Field(default=None, alias="batteryChargingMode")
    soc_upper_limit: Optional[Union[confloat(le=1E+2, ge=0, strict=True), conint(le=100, ge=0, strict=True)]] = Field(default=None, alias="socUpperLimit")
    soc_lower_limit: Optional[Union[confloat(le=1E+2, ge=0, strict=True), conint(le=100, ge=0, strict=True)]] = Field(default=None, alias="socLowerLimit")
    soc_limit: Optional[conint(strict=True, le=100, ge=0)] = Field(default=None, alias="socLimit")
    battery_power: Optional[conint(strict=True, ge=0)] = Field(default=None, alias="batteryPower")
    __properties = ["batteryChargingMode", "socUpperLimit", "socLowerLimit", "socLimit", "batteryPower"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BatteryChargingModeAndSettingsSchema:
        """Create an instance of BatteryChargingModeAndSettingsSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BatteryChargingModeAndSettingsSchema:
        """Create an instance of BatteryChargingModeAndSettingsSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BatteryChargingModeAndSettingsSchema.parse_obj(obj)

        _obj = BatteryChargingModeAndSettingsSchema.parse_obj({
            "battery_charging_mode": obj.get("batteryChargingMode"),
            "soc_upper_limit": obj.get("socUpperLimit"),
            "soc_lower_limit": obj.get("socLowerLimit"),
            "soc_limit": obj.get("socLimit"),
            "battery_power": obj.get("batteryPower")
        })
        return _obj

