#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import systranMultimodalApi
import systranMultimodalApi.configuration

class SpeechApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        systranMultimodalApi.configuration.load_api_key(api_key_file)
        self.api_client = systranMultimodalApi.ApiClient()
        self.speech_api = systranMultimodalApi.SpeechApi(self.api_client)

    def test_multimodal_speech_supported_languages_get(self):
        result = self.speech_api.multimodal_speech_supported_languages_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_multimodal_speech_transcribe_get(self):
        audio_file = os.path.join(os.path.dirname(__file__), "", "test.mp3")
        lang = "en"
        result = self.speech_api.multimodal_speech_transcribe_get(audio_file=audio_file, lang=lang)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_multimodal_speech_transcribe_get_with_model(self):
        audio_file = os.path.join(os.path.dirname(__file__), "", "test.mp3")
        lang = "en"
        model = "eng"
        result = self.speech_api.multimodal_speech_transcribe_get(audio_file=audio_file, lang=lang, model=model)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_multimodal_speech_detect_language_get(self):
        audio_file = os.path.join(os.path.dirname(__file__), "", "test.mp3")
        result = self.speech_api.multimodal_speech_detect_language_get(audio_file=audio_file)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_multimodal_speech_segment_get(self):
        audio_file = os.path.join(os.path.dirname(__file__), "", "test.mp3")
        result = self.speech_api.multimodal_speech_segment_get(audio_file=audio_file)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_multimodal_speech_align_get(self):
        audio_file = os.path.join(os.path.dirname(__file__), "", "test.mp3")
        text_file = os.path.join(os.path.dirname(__file__), "", "test_mp3.txt")
        lang = "en"
        result = self.speech_api.multimodal_speech_align_get(audio_file=audio_file, text_file=text_file, lang=lang)
        self.assertIsNotNone(result)
        print result.__repr__()

if __name__ == '__main__':
    unittest.main()


