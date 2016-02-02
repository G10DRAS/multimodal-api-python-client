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

import sys
from setuptools import setup, find_packages



# To install the library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed.
# Try reading the setuptools documentation:
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi"]

setup(
    name="multimodal-api-python-client",
    version="1.0.1",
    description="REST Multimodal API",
    author_email="",
    url="",
    keywords=["Systran", "REST Multimodal API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    ### Introduction\n\nREST API to use the Multimodal features: Speech recognition, Image Processing, Text extraction.\n\n### Cross Domain\n\nMultimodal API supports cross-domain requests through the JSONP or the CORS mechanism.\n\nMultimodal API also supports the Silverlight client access policy file (clientaccesspolicy.xml) and the Adobe Flash cross-domain policy file (crossdomain.xml) that handles cross-domain requests.\n\n#### JSONP Support\n\nMultimodal API supports JSONP by providing the name of the callback function as a parameter. The response body will be contained in the parentheses:\n\n```javascript\ncallbackFunctionName(/* response body as defined in each API section */);\n```\n\nFor example for a supportedLanguages call with the callback set to supportedLanguagesCallback the response body will be similar to the following:\n\n```javascript\nsupportedLanguagesCallback({\n  \&quot;languages\&quot;: [\n     {\n         \&quot;lang\&quot;: \&quot;en\&quot;, /* language */\n         \&quot;model\&quot;: \&quot;eng\&quot;, /* model */\n     }\n  ]\n});\n```\n\n#### CORS\n\nMultimodal API supports the CORS mechanism to handle cross-domain requests. The server will correctly handle the OPTIONS requests used by CORS.\n\nThe following headers are set as follows:\n\n```\nAccess-Control-Allow-Origin: *\nAccess-Control-Allow-Headers: X-Requested-With,Content-Type,X-HTTP-METHOD-OVERRIDE\n```\n\n### Langage Code Values\n\nThe language codes to be used are the two-letter codes defined by the ISO 639-1:2002, Codes for the representation of names of languages - Part 1: Alpha-2 code standard.\n\nRefer to the column &#39;ISO 639-1 code&#39; of this list: http://www.loc.gov/standards/iso639-2/php/code_list.php.\n\nIn addition to this list, the following codes are used:\n\nLanguage Code |	Language\n--------------|---------\nauto | Language Detection\ntj | Tajik (cyrillic script)\nzh-Hans | Chinese (Simplified)\nzh-Hant |	Chinese (Traditional)\n\n### Audio files\n\nFor an API accepting an audio file, the following formats are supported (all single track):\n  * AIFF\n  * ASF/WMA\n  * FLAC\n  * MS-Wave\n  * MPEG\n  * Ogg/Vorbis\n  * Nist Sphere\n  * Sun AU .input text\nThe maximum accepted audio file size is 110M bytes.\n
    """
)










