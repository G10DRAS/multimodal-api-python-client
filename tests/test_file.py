#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import systran_multimodal_api
import systran_multimodal_api.configuration

class FileApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        systran_multimodal_api.configuration.load_api_key(api_key_file)
        self.api_client = systran_multimodal_api.ApiClient()
        self.file_api = systran_multimodal_api.FileApi(self.api_client)

    def test_multimodal_file_supported_formats_get(self):
        result = self.file_api.multimodal_file_supported_formats_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_multimodal_file_extract_text_get(self):
        input_file = os.path.join(os.path.dirname(__file__), "", "extract_test.html")
        result = self.file_api.multimodal_file_extract_text_get(input_file=input_file)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_multimodal_file_extract_text_get_with_format(self):
        input_file = os.path.join(os.path.dirname(__file__), "", "extract_test.html")
        format = "text/html"
        result = self.file_api.multimodal_file_extract_text_get(input_file=input_file, format=format)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_multimodal_file_extract_text_get_with_format_and_lang(self):
        input_file = os.path.join(os.path.dirname(__file__), "", "extract_test.html")
        lang = "en"
        format = "text/html"
        result = self.file_api.multimodal_file_extract_text_get(input_file=input_file, lang=lang, format=format)
        self.assertIsNotNone(result)
        print result.__repr__()

if __name__ == '__main__':
    unittest.main()