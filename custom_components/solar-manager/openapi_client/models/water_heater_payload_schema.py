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


from typing import Optional
from pydantic import BaseModel, Field, conint

class WaterHeaterPayloadSchema(BaseModel):
    """
    WaterHeaterPayloadSchema
    """
    water_heater_mode: Optional[conint(strict=True, le=6, ge=1)] = Field(default=None, alias="waterHeaterMode")
    power_setting_percent: Optional[conint(strict=True, le=100, ge=0)] = Field(default=None, alias="powerSettingPercent", description="not for ASKOHEAT+")
    __properties = ["waterHeaterMode", "powerSettingPercent"]

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
    def from_json(cls, json_str: str) -> WaterHeaterPayloadSchema:
        """Create an instance of WaterHeaterPayloadSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WaterHeaterPayloadSchema:
        """Create an instance of WaterHeaterPayloadSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WaterHeaterPayloadSchema.parse_obj(obj)

        _obj = WaterHeaterPayloadSchema.parse_obj({
            "water_heater_mode": obj.get("waterHeaterMode"),
            "power_setting_percent": obj.get("powerSettingPercent")
        })
        return _obj

