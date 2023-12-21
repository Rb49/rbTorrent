from ..torrent_object import TorrentObject
import requests
import socket
import asyncio
import bencodepy
import time
from collections import OrderedDict
import socket
from urllib.parse import urlparse


url = 'http://t.nyaatracker.com:80/announce'
response = requests.get(url)


def get_peers(torrent: TorrentObject, callback):
    pass
