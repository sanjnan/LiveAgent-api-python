# coding: utf-8

"""
ApiApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ApiApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_api_keys(self, **kwargs):
        """
        Creates api key
        Create api key

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_api_keys(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ApiKeyWithPrivileges api_key: 
        :return: ApiKeyWithPrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_api_keys" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/apikeys'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'api_key' in params:
            body_params = params['api_key']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ApiKeyWithPrivileges',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_api_key(self, apikey_id, **kwargs):
        """
        Deletes api key
        Delete an api key

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_api_key(apikey_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float apikey_id:  (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apikey_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_api_key" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'apikey_id' is set
        if ('apikey_id' not in params) or (params['apikey_id'] is None):
            raise ValueError("Missing the required parameter `apikey_id` when calling `delete_api_key`")

        resource_path = '/apikeys/{apikeyId}'.replace('{format}', 'json')
        path_params = {}
        if 'apikey_id' in params:
            path_params['apikeyId'] = params['apikey_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='OkResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def generate_api_key(self, **kwargs):
        """
        Gets new api keys
        Get new api key

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.generate_api_key(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ApiKey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_api_key" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/apikeys/_generate'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ApiKey',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_api_info(self, api_version, **kwargs):
        """
        Gets api info
        Get information about api

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_api_info(api_version, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_version: v1 - legacy api version,  v3 - current api version (required)
        :return: ApiInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_info" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'api_version' is set
        if ('api_version' not in params) or (params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `get_api_info`")

        resource_path = '/api/info/{apiVersion}'.replace('{format}', 'json')
        path_params = {}
        if 'api_version' in params:
            path_params['apiVersion'] = params['api_version']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ApiInfo',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_api_key(self, apikey_id, **kwargs):
        """
        Gets api keys
        Get information about api keys

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_api_key(apikey_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float apikey_id:  (required)
        :return: ApiKeyWithPrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apikey_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_key" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'apikey_id' is set
        if ('apikey_id' not in params) or (params['apikey_id'] is None):
            raise ValueError("Missing the required parameter `apikey_id` when calling `get_api_key`")

        resource_path = '/apikeys/{apikeyId}'.replace('{format}', 'json')
        path_params = {}
        if 'apikey_id' in params:
            path_params['apikeyId'] = params['apikey_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ApiKeyWithPrivileges',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_api_keys(self, **kwargs):
        """
        Gets api keys
        Get information about api keys

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_api_keys(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param str filters: Filters (json object {column:value, ...})
        :return: list[ApiKey]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page', '_from', 'to', 'sort_dir', 'sort_field', 'filters']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_keys" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/apikeys'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['_page'] = params['page']
        if 'per_page' in params:
            query_params['_perPage'] = params['per_page']
        if '_from' in params:
            query_params['_from'] = params['_from']
        if 'to' in params:
            query_params['_to'] = params['to']
        if 'sort_dir' in params:
            query_params['_sortDir'] = params['sort_dir']
        if 'sort_field' in params:
            query_params['_sortField'] = params['sort_field']
        if 'filters' in params:
            query_params['_filters'] = params['filters']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[ApiKey]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_api_privileges(self, **kwargs):
        """
        Gets api privileges
        Get api privileges

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_api_privileges(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[ApiPrivilege]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_privileges" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/privileges'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[ApiPrivilege]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_api_key(self, apikey_id, **kwargs):
        """
        Updates api key
        Update an api key

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_api_key(apikey_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float apikey_id:  (required)
        :param ApiKeyWithPrivileges api_key: 
        :return: ApiKeyWithPrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apikey_id', 'api_key']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_api_key" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'apikey_id' is set
        if ('apikey_id' not in params) or (params['apikey_id'] is None):
            raise ValueError("Missing the required parameter `apikey_id` when calling `update_api_key`")

        resource_path = '/apikeys/{apikeyId}'.replace('{format}', 'json')
        path_params = {}
        if 'apikey_id' in params:
            path_params['apikeyId'] = params['apikey_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'api_key' in params:
            body_params = params['api_key']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ApiKeyWithPrivileges',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response