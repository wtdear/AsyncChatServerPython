import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/log.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
