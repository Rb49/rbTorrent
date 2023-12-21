from ..torrent_object import TorrentObject
import bencodepy


def read_torrent(path: str) -> TorrentFile:
    # open and decode the data
    with open(path, 'rb') as file:
        content = file.read()
        content = bencodepy.decode(content)

    # create a Torrent instance
    # need to add support for distributed torrents and magnet links, non multi-file torrents and no announcers
    torrent_data = TorrentFile(info=content.get(b'info'),
                               announce=content.get(b'announce'),
                               comment=content.get(b'comment'),
                               announce_list=content.get(b'announce-list'))

    return torrent_data
