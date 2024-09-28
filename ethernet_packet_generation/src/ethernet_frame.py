from utils import crc32

class EthernetFrame:
    def __init__(self, src_addr, dest_addr, ether_type, payload, max_size):
        self.src_addr = src_addr
        self.dest_addr = dest_addr
        self.ether_type = ether_type
        self.payload = payload
        self.max_size = max_size
        self.frame = self.build_frame()

    def build_frame(self):
        """ 
        Build an Ethernet frame with the given source and destination MAC addresses, EtherType, and payload.
        :return: The Ethernet frame as a byte string, or None if the frame exceeds the maximum size.
        """
        if len(self.payload) > 1500:
            return None  # Payload exceeds the maximum size
        # Build the Ethernet frame (including preamble, SOF, addresses, payload, and CRC)
        preamble = b'\x55' * 7  # Preamble (7 bytes)
        sop = b'\xFD'           # Start of Frame (1 byte)

        frame = preamble + sop
        frame += self.dest_addr.to_bytes(6, byteorder='big')  # Destination MAC
        frame += self.src_addr.to_bytes(6, byteorder='big')   # Source MAC
        frame += self.ether_type.to_bytes(2, byteorder='big')   # EtherType for eCPRI

        # Pad the payload to reach the minimum Ethernet frame size (46 bytes)
        if len(self.payload) < 46:
            frame += self.payload + b'\x00' * (46 - len(self.payload))
        else:
            frame += self.payload

        # Calculate and append CRC
        crc = crc32(frame)
        frame += crc

        if len(frame) > self.max_size:
            return None  # Frame exceeds the maximum size

        return frame

