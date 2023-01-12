# Copyright 2022 Expedia, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional
from enum import Enum
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Location(Enum):
    HEADER = "HEADER"
    PATH = "PATH"
    QUERY = "QUERY"
    BODY = "BODY"


@dataclass_json
@dataclass
class ErrorCause:
    type: str
    detail: str
    location: Location
    name: str
    value: str


@dataclass_json
@dataclass
class Error:
    type: str
    detail: str
    causes: Optional[list[ErrorCause]] = None
