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
from pydantic import BaseModel, Field
from openapi_client.models.model20 import Model20
from openapi_client.models.model21 import Model21
from openapi_client.models.model22 import Model22

class Model23(BaseModel):
    """
    Model23
    """
    monday_friday: Optional[Model20] = Field(default=None, alias="mondayFriday")
    saturday: Optional[Model21] = None
    sunday: Optional[Model22] = None
    __properties = ["mondayFriday", "saturday", "sunday"]

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
    def from_json(cls, json_str: str) -> Model23:
        """Create an instance of Model23 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of monday_friday
        if self.monday_friday:
            _dict['mondayFriday'] = self.monday_friday.to_dict()
        # override the default output from pydantic by calling `to_dict()` of saturday
        if self.saturday:
            _dict['saturday'] = self.saturday.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sunday
        if self.sunday:
            _dict['sunday'] = self.sunday.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Model23:
        """Create an instance of Model23 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Model23.parse_obj(obj)

        _obj = Model23.parse_obj({
            "monday_friday": Model20.from_dict(obj.get("mondayFriday")) if obj.get("mondayFriday") is not None else None,
            "saturday": Model21.from_dict(obj.get("saturday")) if obj.get("saturday") is not None else None,
            "sunday": Model22.from_dict(obj.get("sunday")) if obj.get("sunday") is not None else None
        })
        return _obj


