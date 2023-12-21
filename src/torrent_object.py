from collections import OrderedDict
from dataclasses import dataclass
from typing import Optional, List, Union


@dataclass(frozen=True)
class TorrentObject:
    info: OrderedDict  # metadate dict
    announce: Optional[bytearray]  # tracker
    comment: Optional[bytearray] = None  # comment added by uploader, optional

    # other extensions to the protocol
    nodes: Optional[list] = None  # support distributed hash tables
    announce_list: Optional[list] = None  # support of multiple trackers
    http_seeds: Optional[list] = None  # support http seeds to retrieve torrent file and later support https
    private: Optional[bool] = False  # if 'private' key in 'info' dict is 1 (private torrent)
