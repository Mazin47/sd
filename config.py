# Copyright (c) 2022 Itz-fork

import os
from telethon.sessions import StringSession

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 1234567))
    API_HASH = os.environ.get("API_HASH", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
