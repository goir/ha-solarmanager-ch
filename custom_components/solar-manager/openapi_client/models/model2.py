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
from openapi_client.models.model1 import Model1

class Model2(BaseModel):
    """
    Model2
    """
    gateway_id: Optional[StrictStr] = Field(default=None, alias="gatewayId")
    period: Optional[StrictStr] = None
    data: Optional[conlist(Model1)] = None
    total_consumption: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalConsumption", description="total power consumption in Wh")
    total_production: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalProduction", description="total production in Wh")
    __properties = ["gatewayId", "period", "data", "totalConsumption", "totalProduction"]

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
    def from_json(cls, json_str: str) -> Model2:
        """Create an instance of Model2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Model2:
        """Create an instance of Model2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Model2.parse_obj(obj)

        _obj = Model2.parse_obj({
            "gateway_id": obj.get("gatewayId"),
            "period": obj.get("period"),
            "data": [Model1.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "total_consumption": obj.get("totalConsumption"),
            "total_production": obj.get("totalProduction")
        })
        return _obj


