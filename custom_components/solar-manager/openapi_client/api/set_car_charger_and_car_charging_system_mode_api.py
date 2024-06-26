# coding: utf-8

"""
    Solar Manager external API 

    This is a Solar Manager external communication service

    The version of the OpenAPI document: 1.19.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from pydantic import StrictStr

from typing import Optional

from openapi_client.models.car_charger_payload_schema import CarChargerPayloadSchema

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SetCarChargerAndCarChargingSystemModeApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def put_v1_control_carcharger_sensorid(self, sensor_id : StrictStr, body : Optional[CarChargerPayloadSchema] = None, **kwargs) -> None:  # noqa: E501
        """put_v1_control_carcharger_sensorid  # noqa: E501

        INFO  chargingMode:  0 = Fast Charge   1 = Only solar  2 = Solar & tariff optimized  3 = Do not charge  4 = Constant current  5 = Minimal & Solar  6 = Minimum charge quantity  7 = Charging Target(%)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_v1_control_carcharger_sensorid(sensor_id, body, async_req=True)
        >>> result = thread.get()

        :param sensor_id: (required)
        :type sensor_id: str
        :param body:
        :type body: CarChargerPayloadSchema
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the put_v1_control_carcharger_sensorid_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.put_v1_control_carcharger_sensorid_with_http_info(sensor_id, body, **kwargs)  # noqa: E501

    @validate_arguments
    def put_v1_control_carcharger_sensorid_with_http_info(self, sensor_id : StrictStr, body : Optional[CarChargerPayloadSchema] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """put_v1_control_carcharger_sensorid  # noqa: E501

        INFO  chargingMode:  0 = Fast Charge   1 = Only solar  2 = Solar & tariff optimized  3 = Do not charge  4 = Constant current  5 = Minimal & Solar  6 = Minimum charge quantity  7 = Charging Target(%)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_v1_control_carcharger_sensorid_with_http_info(sensor_id, body, async_req=True)
        >>> result = thread.get()

        :param sensor_id: (required)
        :type sensor_id: str
        :param body:
        :type body: CarChargerPayloadSchema
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'sensor_id',
            'body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_v1_control_carcharger_sensorid" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['sensor_id'] is not None:
            _path_params['sensorId'] = _params['sensor_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['body'] is not None:
            _body_params = _params['body']

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['basic', 'BearerAuth']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/v1/control/car-charger/{sensorId}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
