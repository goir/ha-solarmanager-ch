# coding: utf-8

"""
    Solar Manager external API 

    This is a Solar Manager external communication service

    The version of the OpenAPI document: 1.19.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ModelFrom(str, Enum):
    """
    ModelFrom
    """

    """
    allowed enum values
    """
    ENUM_00_COLON_00 = '00:00'

    @classmethod
    def from_json(cls, json_str: str) -> ModelFrom:
        """Create an instance of ModelFrom from a JSON string"""
        return ModelFrom(json.loads(json_str))


