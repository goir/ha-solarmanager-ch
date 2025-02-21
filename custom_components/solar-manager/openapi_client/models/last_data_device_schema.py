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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist

class LastDataDeviceSchema(BaseModel):
    """
    LastDataDeviceSchema
    """
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    signal: Optional[StrictStr] = None
    soc: Optional[StrictInt] = Field(default=None, alias="SOC", description="battery capacity")
    current_power: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="currentPower", description="power of device in W")
    current_water_temp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="currentWaterTemp")
    errors: Optional[conlist(StrictStr)] = None
    __properties = ["_id", "signal", "SOC", "currentPower", "currentWaterTemp", "errors"]

    class Config:
        """Pydantic configuration"""
        populate_by_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> LastDataDeviceSchema:
        """Create an instance of LastDataDeviceSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LastDataDeviceSchema:
        """Create an instance of LastDataDeviceSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LastDataDeviceSchema.parse_obj(obj)

        _obj = LastDataDeviceSchema.parse_obj({
            "id": obj.get("_id"),
            "signal": obj.get("signal"),
            "soc": obj.get("SOC"),
            "current_power": obj.get("currentPower"),
            "current_water_temp": obj.get("currentWaterTemp"),
            "errors": obj.get("errors")
        })
        return _obj


