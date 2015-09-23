#!/usr/bin/env python
# coding: utf-8

"""
Copyright 2015 SYSTRAN Software, Inc. All rights reserved.

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

from .. import configuration
from ..api_client import ApiClient

class FileApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('https://api-platform.systran.net')
            self.api_client = configuration.api_client
    
    
    def multimodal_file_extract_text_get(self, input_file, **kwargs):
        """
        Extract text from a file
        Extract text from a file.\n

        :param File input_file: Input File (required)
        :param str lang: Language code of the input ([details](#description_langage_code_values)) or `auto` for automatic detection 
        :param str format: Format of the input file.\n\nValid values are the mimetypes returned by the supportedFormats service.\n 
        :param int profile: Profile id\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: FileExtractTextResponse
        """
        
        # verify the required parameter 'input_file' is set
        if input_file is None:
            raise ValueError("Missing the required parameter `input_file` when calling `multimodal_file_extract_text_get`")
        
        all_params = ['input_file', 'lang', 'format', 'profile', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method multimodal_file_extract_text_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/multimodal/file/extract/text'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'lang' in params:
            query_params['lang'] = params['lang']
        
        if 'format' in params:
            query_params['format'] = params['format']
        
        if 'profile' in params:
            query_params['profile'] = params['profile']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'input_file' in params:
            files['inputFile'] = params['input_file']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data', 'application/x-www-form-urlencoded', '*/*'])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='FileExtractTextResponse', auth_settings=auth_settings)
        
        return response
        
    def multimodal_file_supported_formats_get(self, **kwargs):
        """
        Supported file formats
        Get a list of supported file formats.\n

        :param int profile: Profile id\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: FileSupportedFormatsResponse
        """
        
        all_params = ['profile', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method multimodal_file_supported_formats_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/multimodal/file/supportedFormats'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'profile' in params:
            query_params['profile'] = params['profile']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='FileSupportedFormatsResponse', auth_settings=auth_settings)
        
        return response
        









