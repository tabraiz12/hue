#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pdb
from desktop.conf import LLM
import openai

def openai_completion_api(prompt, type=None):
    if LLM.OPENAI.ENABLE.get():
        prompt = prompt_type(type) + prompt
        try:
            openai_token = LLM.OPENAI.TOKEN.get()
            openai.api_key = openai_token
            model = LLM.OPENAI.MODEL.get()
            response = openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.5
            )
            choices = response.choices[0]
            text = choices.text.strip()
            return text
        except:
            return "Error Encountered While Callling OpenAI API"
    else:
        return "Open AI Not Enabled"

def prompt_type(type):
    if type=="generate_sql":
        return "Act as SQL Generator, and generate a sql query for the following SQL with metadata:"
    elif type=="explain":
        return "Act as SQL Expert, and explain the following query:"
    elif type=="auto_correct":
        return "Act as SQL Expert, and Correct the following query:"