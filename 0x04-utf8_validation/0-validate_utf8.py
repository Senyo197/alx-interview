#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """
    Determines if the given data set represents a valid UTF-8 encoding.

    Parameters:
    data (list of int): The data set to check.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    byte = 0
    while byte < len(data):
        num_bytes = 0
        current_byte = data[byte]
        while current_byte & (128 >> num_bytes):
            num_bytes += 1
        if num_bytes == 0:
            byte += 1
        elif num_bytes == 1 or num_bytes > 4:
            return False
        else:
            for j in range(1, num_bytes):
                if (byte + j >= len(data) or
                        (data[byte+j] & 0b11000000) != 0b10000000):
                    return False
            byte += num_bytes
    return True
