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





class Tariff(str, Enum):
    """
    Tariff
    """

    """
    allowed enum values
    """
    LOW = 'low'

    @classmethod
    def from_json(cls, json_str: str) -> Tariff:
        """Create an instance of Tariff from a JSON string"""
        return Tariff(json.loads(json_str))


