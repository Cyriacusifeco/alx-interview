#!/usr/bin/python3
"""
Function to validate utf8 character sequence.

"""


def validUTF8(data):
    # Function to check if a byte is a continuation byte(starts with '10')
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    # Main validation logic
    num_bytes_to_check = 0

    for byte in data:
        if num_bytes_to_check == 0:
            # Count the number of bytes in the current character
            if byte & 0b10000000 == 0b00000000:  # Single-byte character
                num_bytes_to_check = 0
            elif byte & 0b11100000 == 0b11000000:  # Two-byte character
                num_bytes_to_check = 1
            elif byte & 0b11110000 == 0b11100000:  # Three-byte character
                num_bytes_to_check = 2
            elif byte & 0b11111000 == 0b11110000:  # Four-byte character
                num_bytes_to_check = 3
            else:
                return False
        else:
            # Check if the byte is a continuation byte
            if not is_continuation(byte):
                return False

            num_bytes_to_check -= 1

    # If all bytes have been checked, it's a valid UTF-8 encoding
    return num_bytes_to_check == 0
