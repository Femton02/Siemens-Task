def crc32(data: bytes) -> bytes:
    """
    Generate CRC-32 using a standard polynomial (0xEDB88320) and return it as 4 bytes.
    
    :param data: Input data as bytes.
    :return: Calculated CRC-32 as a 4-byte sequence.
    """
    # CRC-32 polynomial
    polynomial = 0xEDB88320
    # Initialize CRC to all 1's (0xFFFFFFFF)
    crc = 0xFFFFFFFF

    # Process each byte in the data
    for byte in data:
        # XOR byte into the low-order byte of CRC
        crc ^= byte
        # Perform the 8-bit CRC algorithm (repeated 8 times)
        for _ in range(8):
            # If LSB is set, shift right and XOR with the polynomial
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                # If LSB is not set, just shift right
                crc >>= 1

    # Final XOR with 0xFFFFFFFF to get the correct CRC value
    crc = crc ^ 0xFFFFFFFF

    # Convert the final CRC value to a 4-byte sequence in big-endian format
    return crc.to_bytes(4, byteorder='big')


def get_ifg_padding(packet: bytes) -> bytes:
    """
    Ensure the packet is 4-byte aligned by adding IFGs as padding if necessary.

    :param packet: Input packet as bytes.
    :return: IFG padding as bytes to align the packet to a multiple of 4 bytes.
    """
    packet_length = len(packet)
    remainder = packet_length % 4

    if remainder != 0:
        # Calculate how many bytes to add to make the length a multiple of 4
        padding_needed = 4 - remainder
        ifg_padding = b'\x07' * padding_needed
        print(f"Adding {padding_needed} bytes of IFG padding for 4-byte alignment.")
        return ifg_padding
    
    return b''  # No padding needed