import socket
import numpy as np
import random
from typing import Tuple
import struct


def conn_req() -> Tuple[bytes, str]:
    connection_id = np.int64(0x41727101980)  # connection_id for connect
    action = np.int32(0)  # action = connect (0)
    transaction_id = np.int32(struct.unpack('<i', struct.pack('<I', random.getrandbits(32)))[0])

    data = connection_id.tobytes() + action.tobytes() + transaction_id.tobytes()

    return data, transaction_id


def udp_request(tracker_url: bytes):
    # remove the 'udp://' and '/announce' from address
    tracker_url = tracker_url.decode('utf-8').replace('udp://', '')
    tracker_url = tracker_url.split('/')[0]

    server_address = tracker_url.split(':')[0], int(tracker_url.split(':')[1])

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.settimeout(1)

    request, transaction_id = conn_req()

    udp_socket.sendto(request, server_address)

    while True:
        data, server = udp_socket.recvfrom(1024)
        print(data)


if __name__ == '__main__':
    upd_url = b'udp://tracker.tiny-vps.com:6969/announce'
    udp_request(upd_url)
