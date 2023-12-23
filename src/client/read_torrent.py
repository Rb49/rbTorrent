import bencodepy
from torrent_object import TorrentObject
import hashlib


def read_torrent(path: str) -> TorrentObject:
    # open and decode the data
    with open(path, 'rb') as file:
        content = file.read()
        content = bencodepy.decode(content)

    # create a Torrent instance
    # need to add support for distributed torrents and magnet links, non multi-file torrents and no announcers
    torrent_data = TorrentObject(info=content.get(b'info'),
                                 info_hash=None,
                                 piece_hashes=None,
                                 announce=content.get(b'announce'),
                                 comment=content.get(b'comment'),
                                 announce_list=content.get(b'announce-list'))
    # set info_hash and piece_hashes:
    # hashes are in sha1, 20 bytes long
    pieces = torrent_data.info[b'pieces']
    torrent_data.piece_hashes = [pieces[i: i + 20] for i in range(0, len(pieces), 20)]

    data = bencodepy.encode(torrent_data.info)
    sha1_hash = hashlib.sha1()
    sha1_hash.update(data)
    hash_result = sha1_hash.digest()
    torrent_data.info_hash = hash_result

    return torrent_data
