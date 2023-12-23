from collections import OrderedDict
from dataclasses import dataclass
from typing import Optional, List, Union


@dataclass
class TorrentObject:
    info: OrderedDict  # metadate dict
    info_hash: Union[bytes, None]  # sha-1 hash of the entire bencoded info dict
    piece_hashes: Union[List[bytes], None]  # list of sha-1 hashes of all the pieces

    announce: Optional[bytes]  # tracker
    comment: Optional[Union[bytes, None]] = None  # comment added by uploader, optional

    # other extensions to the protocol
    nodes: Optional[list] = None  # support distributed hash tables
    announce_list: Optional[list] = None  # support of multiple trackers
    http_seeds: Optional[list] = None  # support http seeds to retrieve torrent file and later support https
    private: Optional[bool] = False  # if 'private' key in 'info' dict is 1 (private torrent)
