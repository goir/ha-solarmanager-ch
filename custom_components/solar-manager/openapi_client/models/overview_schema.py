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
from openapi_client.models.autarchy import Autarchy
from openapi_client.models.consumption import Consumption
from openapi_client.models.monitoring import Monitoring
from openapi_client.models.production import Production
from openapi_client.models.status import Status
from openapi_client.models.total_energy import TotalEnergy

class OverviewSchema(BaseModel):
    """
    OverviewSchema
    """
    plants: Optional[Union[StrictFloat, StrictInt]] = None
    support_contracts: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="supportContracts")
    production: Optional[Production] = None
    status: Optional[Status] = None
    monitoring: Optional[Monitoring] = None
    autarchy: Optional[Autarchy] = None
    consumption: Optional[Consumption] = None
    total_energy: Optional[TotalEnergy] = Field(default=None, alias="totalEnergy")
    __properties = ["plants", "supportContracts", "production", "status", "monitoring", "autarchy", "consumption", "totalEnergy"]

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
    def from_json(cls, json_str: str) -> OverviewSchema:
        """Create an instance of OverviewSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of production
        if self.production:
            _dict['production'] = self.production.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of monitoring
        if self.monitoring:
            _dict['monitoring'] = self.monitoring.to_dict()
        # override the default output from pydantic by calling `to_dict()` of autarchy
        if self.autarchy:
            _dict['autarchy'] = self.autarchy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of consumption
        if self.consumption:
            _dict['consumption'] = self.consumption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_energy
        if self.total_energy:
            _dict['totalEnergy'] = self.total_energy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OverviewSchema:
        """Create an instance of OverviewSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OverviewSchema.parse_obj(obj)

        _obj = OverviewSchema.parse_obj({
            "plants": obj.get("plants"),
            "support_contracts": obj.get("supportContracts"),
            "production": Production.from_dict(obj.get("production")) if obj.get("production") is not None else None,
            "status": Status.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "monitoring": Monitoring.from_dict(obj.get("monitoring")) if obj.get("monitoring") is not None else None,
            "autarchy": Autarchy.from_dict(obj.get("autarchy")) if obj.get("autarchy") is not None else None,
            "consumption": Consumption.from_dict(obj.get("consumption")) if obj.get("consumption") is not None else None,
            "total_energy": TotalEnergy.from_dict(obj.get("totalEnergy")) if obj.get("totalEnergy") is not None else None
        })
        return _obj


