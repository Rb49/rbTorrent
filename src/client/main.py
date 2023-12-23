from read_torrent import read_torrent

if __name__ == '__main__':
    # path for test torrent file
    test_path = "The.Truman.Show.1998.1080p.BluRay.H264.AAC-RARBG[TGx].torrent"
    test_path = "../../data/" + test_path

    # read torrent file
    TorrentFile = read_torrent(test_path)

    # connect to trackers

    # set peer_id, later will be chosen randomly in a file
    peer_id = "abcdefghijklmnopqrst"



    pass

