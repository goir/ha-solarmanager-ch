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
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class Monitoring(BaseModel):
    """
    Monitoring
    """
    ok: Optional[Union[StrictFloat, StrictInt]] = None
    not_connected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="notConnected")
    warning: Optional[Union[StrictFloat, StrictInt]] = None
    error: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["ok", "notConnected", "warning", "error"]

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
    def from_json(cls, json_str: str) -> Monitoring:
        """Create an instance of Monitoring from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Monitoring:
        """Create an instance of Monitoring from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Monitoring.parse_obj(obj)

        _obj = Monitoring.parse_obj({
            "ok": obj.get("ok"),
            "not_connected": obj.get("notConnected"),
            "warning": obj.get("warning"),
            "error": obj.get("error")
        })
        return _obj


