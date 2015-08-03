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

# import models into sdk package
from .models.speech_channel import SpeechChannel
from .models.speech_speaker import SpeechSpeaker
from .models.speech_lang_speaker import SpeechLangSpeaker
from .models.speech_transcribe_speaker import SpeechTranscribeSpeaker
from .models.speech_word import SpeechWord
from .models.speech_segment import SpeechSegment
from .models.speech_lang_segment import SpeechLangSegment
from .models.speech_transcribe_segment import SpeechTranscribeSegment
from .models.speech_align_segment import SpeechAlignSegment
from .models.speech_detect_language_response import SpeechDetectLanguageResponse
from .models.speech_segment_response import SpeechSegmentResponse
from .models.speech_align_response import SpeechAlignResponse
from .models.speech_transcribe_response import SpeechTranscribeResponse
from .models.speech_supported_languages_response import SpeechSupportedLanguagesResponse
from .models.file_extract_text_response import FileExtractTextResponse
from .models.file_format import FileFormat
from .models.file_supported_formats_response import FileSupportedFormatsResponse

# import apis into sdk package
from .apis.file_api import FileApi
from .apis.speech_api import SpeechApi

# import ApiClient
from .api_client import ApiClient
