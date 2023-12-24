from src.read_file.read_torrent import read_torrent
from src.tracker.http_tracker import connect_to_tracker

if __name__ == '__main__':
    # path for test torrent file
    test_path = "debian-edu-12.4.0-amd64-netinst.iso.torrent"
    test_path = "../../data/" + test_path

    # read torrent file
    TorrentFile = read_torrent(test_path)

    # connect to trackers

    # set peer_id, later will be chosen randomly in a file
    peer_id = "qR7pX2oH9wL4sZ8vE1aY"
    http_url = 'http://bttracker.debian.org:6969/announce'

    peersDict = connect_to_tracker(http_url, TorrentFile.info_hash, peer_id)

    pass

