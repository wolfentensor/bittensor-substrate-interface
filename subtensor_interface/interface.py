# Python Substrate Interface Library
#
# Copyright 2018-2023 Stichting Polkascan (Polkascan Foundation).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import warnings

from datetime import datetime
from hashlib import blake2b

import json
import logging

import requests
from typing import Optional, Union, List

from websocket import create_connection, WebSocketConnectionClosedException

from scalecodec.base import ScaleBytes, RuntimeConfigurationObject, ScaleType
from scalecodec.types import (
    GenericCall,
    GenericExtrinsic,
    Extrinsic,
    MultiAccountId,
    GenericRuntimeCallDefinition,
)
from scalecodec.type_registry import load_type_registry_preset
from scalecodec.updater import update_type_registries

from substrateinterface import SubstrateInterface
from substrateinterface.extensions import Extension
from substrateinterface.interfaces import ExtensionInterface

from substrateinterface.storage import StorageKey

from substrateinterface.exceptions import (
    SubstrateRequestException,
    ConfigurationError,
    StorageFunctionNotFound,
    BlockNotFound,
    ExtrinsicNotFound,
    ExtensionCallNotFound,
)
from substrateinterface.constants import *
from substrateinterface.keypair import Keypair, KeypairType, MnemonicLanguageCode
from substrateinterface.utils.ss58 import ss58_decode, ss58_encode, is_valid_ss58_address, get_ss58_format


__all__ = ["BittensorSubstrateInterface", "logger"]

logger = logging.getLogger(__name__)


class BittensorSubstrateInterface(SubstrateInterface):

    def __init__(self):
        super().__init__(url="wss://node.bittensor.com", type_registry_preset="bittensor")

        warnings.filterwarnings("ignore")

    def initialize(self):
        pass

    def rpc_request(self, method, params, result_handler=None):
        pass









