from src.read_file.read_torrent import read_torrent
from src.tracker.udp_tracker import udp_request
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

    if not TorrentFile.announce_list:
        TorrentFile.announce_list = [[TorrentFile.announce]]
    for url in TorrentFile.announce_list:
        url = url[0]
        try:
            if b'udp' in url:

                print(url)
                udp_request(url)
            elif b'http' in url:
                print(url)
                connect_to_tracker(url, TorrentFile.info_hash, peer_id, 61234)

        except Exception as e:
            print(e)
