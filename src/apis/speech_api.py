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

class SpeechApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('https://api-platform.systran.net')
            self.api_client = configuration.api_client
    
    
    def multimodal_speech_align_get(self, audio_file, text_file, lang, **kwargs):
        """
        Align speech
        Align text and audio files.\n

        :param File audio_file: Audio file ([details](#description_audio_files)).\n (required)
        :param File text_file: Plain text file, ASCII, ISO-8859 or UTF8 encoded.\n\nThe text should include one sentence or clause per line ending with a punctuation mark.\n (required)
        :param str lang: Language code of the input ([details](#description_langage_code_values)) (required)
        :param str model: Model name\n 
        :param str sampling: Sampling quality of the audio file.\n * high: wide band audio such as radio and TV broadcast (sampling higher or equal to 16KHz)\n * low: telephone data with sampling rates higher or equal to 8KHz. It is highly recommended to not use a bit rate lower than 32Kbps.\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: SpeechAlignResponse
        """
        
        # verify the required parameter 'audio_file' is set
        if audio_file is None:
            raise ValueError("Missing the required parameter `audio_file` when calling `multimodal_speech_align_get`")
        
        # verify the required parameter 'text_file' is set
        if text_file is None:
            raise ValueError("Missing the required parameter `text_file` when calling `multimodal_speech_align_get`")
        
        # verify the required parameter 'lang' is set
        if lang is None:
            raise ValueError("Missing the required parameter `lang` when calling `multimodal_speech_align_get`")
        
        all_params = ['audio_file', 'text_file', 'lang', 'model', 'sampling', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method multimodal_speech_align_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/multimodal/speech/align'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'lang' in params:
            query_params['lang'] = params['lang']
        
        if 'model' in params:
            query_params['model'] = params['model']
        
        if 'sampling' in params:
            query_params['sampling'] = params['sampling']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'audio_file' in params:
            files['audioFile'] = params['audio_file']
        
        if 'text_file' in params:
            files['textFile'] = params['text_file']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='SpeechAlignResponse', auth_settings=auth_settings)
        
        return response
        
    def multimodal_speech_detect_language_get(self, audio_file, **kwargs):
        """
        Speech language detection
        Detect languages from an audio file.\n

        :param File audio_file: Audio file ([details](#description_audio_files)).\n (required)
        :param str sampling: Sampling quality of the audio file.\n * high: wide band audio such as radio and TV broadcast (sampling higher or equal to 16KHz)\n * low: telephone data with sampling rates higher or equal to 8KHz. It is highly recommended to not use a bit rate lower than 32Kbps.\n 
        :param int max_speaker: Maximum number of speakers. Default 1 for low sampling and infinity for high sampling 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: SpeechDetectLanguageResponse
        """
        
        # verify the required parameter 'audio_file' is set
        if audio_file is None:
            raise ValueError("Missing the required parameter `audio_file` when calling `multimodal_speech_detect_language_get`")
        
        all_params = ['audio_file', 'sampling', 'max_speaker', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method multimodal_speech_detect_language_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/multimodal/speech/detectLanguage'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'sampling' in params:
            query_params['sampling'] = params['sampling']
        
        if 'max_speaker' in params:
            query_params['maxSpeaker'] = params['max_speaker']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'audio_file' in params:
            files['audioFile'] = params['audio_file']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='SpeechDetectLanguageResponse', auth_settings=auth_settings)
        
        return response
        
    def multimodal_speech_segment_get(self, audio_file, **kwargs):
        """
        Segment speech
        Segment an audio file.\n

        :param File audio_file: Audio file ([details](#description_audio_files)).\n (required)
        :param str sampling: Sampling quality of the audio file.\n * high: wide band audio such as radio and TV broadcast (sampling higher or equal to 16KHz)\n * low: telephone data with sampling rates higher or equal to 8KHz. It is highly recommended to not use a bit rate lower than 32Kbps.\n 
        :param int max_speaker: Maximum number of speakers. Default 1 for low sampling and infinity for high sampling 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: SpeechSegmentResponse
        """
        
        # verify the required parameter 'audio_file' is set
        if audio_file is None:
            raise ValueError("Missing the required parameter `audio_file` when calling `multimodal_speech_segment_get`")
        
        all_params = ['audio_file', 'sampling', 'max_speaker', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method multimodal_speech_segment_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/multimodal/speech/segment'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'sampling' in params:
            query_params['sampling'] = params['sampling']
        
        if 'max_speaker' in params:
            query_params['maxSpeaker'] = params['max_speaker']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'audio_file' in params:
            files['audioFile'] = params['audio_file']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='SpeechSegmentResponse', auth_settings=auth_settings)
        
        return response
        
    def multimodal_speech_supported_languages_get(self, **kwargs):
        """
        Supported Languages
        List of languages in which Speech is supported.\n

        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: SpeechSupportedLanguagesResponse
        """
        
        all_params = ['callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method multimodal_speech_supported_languages_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/multimodal/speech/supportedLanguages'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
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
                                            response='SpeechSupportedLanguagesResponse', auth_settings=auth_settings)
        
        return response
        
    def multimodal_speech_transcribe_get(self, audio_file, lang, **kwargs):
        """
        Transcribe speech
        Get text from an audio file.\n

        :param File audio_file: Audio file ([details](#description_audio_files)).\n (required)
        :param str lang: Language code of the input ([details](#description_langage_code_values)) (required)
        :param str model: Model name\n 
        :param str sampling: Sampling quality of the audio file.\n * high: wide band audio such as radio and TV broadcast (sampling higher or equal to 16KHz)\n * low: telephone data with sampling rates higher or equal to 8KHz. It is highly recommended to not use a bit rate lower than 32Kbps.\n 
        :param int max_speaker: Maximum number of speakers. Default 1 for low sampling and infinity for high sampling 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: SpeechTranscribeResponse
        """
        
        # verify the required parameter 'audio_file' is set
        if audio_file is None:
            raise ValueError("Missing the required parameter `audio_file` when calling `multimodal_speech_transcribe_get`")
        
        # verify the required parameter 'lang' is set
        if lang is None:
            raise ValueError("Missing the required parameter `lang` when calling `multimodal_speech_transcribe_get`")
        
        all_params = ['audio_file', 'lang', 'model', 'sampling', 'max_speaker', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method multimodal_speech_transcribe_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/multimodal/speech/transcribe'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'lang' in params:
            query_params['lang'] = params['lang']
        
        if 'model' in params:
            query_params['model'] = params['model']
        
        if 'sampling' in params:
            query_params['sampling'] = params['sampling']
        
        if 'max_speaker' in params:
            query_params['maxSpeaker'] = params['max_speaker']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'audio_file' in params:
            files['audioFile'] = params['audio_file']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='SpeechTranscribeResponse', auth_settings=auth_settings)
        
        return response
        









