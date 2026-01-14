import asyncio
import logging
import websockets
import json
import os

# LOGGING

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/log.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# SERVER

connected_clients = {}