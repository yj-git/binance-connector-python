#!/usr/bin/env python

import os
import pathlib
from configparser import ConfigParser


def get_api_key():
    config = ConfigParser()
    config_file_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(), "..", "config.ini"
    )
    config.read(config_file_path)
    return config["keys"]["api_key"], config["keys"]["api_secret"]


# ed25519 配置 create by cyj
def get_ed25519_api_key():
    config = ConfigParser()
    config_file_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(), "..", "config.ini"
    )
    config.read(config_file_path)
    ed25519_private_key = config["keys"]["ed25519_private_key"]
    if ed25519_private_key:
        ed25519_private_key = f"""-----BEGIN PRIVATE KEY-----
        {ed25519_private_key}
        -----END PRIVATE KEY-----"""
    ed25519_private_key_pass = config["keys"]["ed25519_private_key_pass"]
    if str(ed25519_private_key_pass) == '':
        ed25519_private_key_pass = None
    return config["keys"]["ed25519_api_key"], ed25519_private_key, ed25519_private_key_pass
