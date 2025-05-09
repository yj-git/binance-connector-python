#!/usr/bin/env python

import logging
import time
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient
from examples.utils.prepare_env import get_ed25519_api_key

api_key, private_key, private_key_pass = get_ed25519_api_key()

config_logging(logging, logging.DEBUG)


def on_close(_):
    logging.info("Do custom stuff when connection is closed")


def message_handler(_, message):
    logging.info(message)


my_client = SpotWebsocketAPIClient(
    stream_url="wss://ws-api.testnet.binance.vision/ws-api/v3",
    api_key=api_key,
    private_key=private_key,
    private_key_pass=private_key_pass,
    on_message=message_handler,
    on_close=on_close,
)

my_client.logon()

# my_client.subscribe_user_data()

time.sleep(100)

logging.info("closing ws connection")
# my_client.unsubscribe_user_data()
