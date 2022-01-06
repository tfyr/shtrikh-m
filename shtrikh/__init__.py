ENQ = b'\x05'
STX = b'\x02'
ACK = b'\x06'
NAK = b'\x15'


def xor_control_sum(data):
    j = 0
    for i in data:
        j = j ^ i
    return j
