import requests
import bencodepy
from collections import OrderedDict
from typing import Union


def connect_to_tracker(tracker_url: str, info_hash: bytes, peer_id: str) -> Union[OrderedDict, str]:
    """
    connect to a http tracker through GET
    :param tracker_url: url of the tracker
    :param info_hash: info_hash of the torrent file
    :param peer_id: peer_id
    :return: str: error message | OrderedDict: decoded response of the tracker
    """

    params = {
        'info_hash': info_hash,
        'peer_id': peer_id,
        'uploaded': 0,
        'downloaded': 0,
        'left': 0,
        'event': 'started',
    }

    response = requests.get(tracker_url, params=params, timeout=1)

    # check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        peer_data = response.text
        peer_data = bencodepy.decode(str.encode(peer_data))
        return peer_data
    else:
        return f"Failed to connect to the tracker. HTTP Status Code: {response.status_code}"
