from ..torrent_object import TorrentObject
from read_torrent import read_torrent

if __name__ == '__main__':
    # path for test torrent file
    test_path = "The.Truman.Show.1998.1080p.BluRay.H264.AAC-RARBG[TGx].torrent"
    test_path = "../../data/" + test_path

    # read torrent file
    TorrentFile = read_torrent(test_path)

    # hashes are in sha1, 20 bytes long
    pieces = TorrentFile.info[b'pieces']
    pieces_list = [pieces[i: i + 20] for i in range(0, len(pieces), 20)]

    # connect to trackers



