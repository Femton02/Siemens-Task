import random

class eCPRIFrame:
    def __init__(self, num_samples):
        self.num_samples = num_samples
        self.payload = self._generate_iq_payload()
        self.frame = self.build_frame()

    def _generate_iq_payload(self):
        # Generate Random IQ samples
        iq_samples = bytearray()
        for _ in range(self.num_samples):
            iq_samples += bytearray(random.getrandbits(8) for _ in range(4))
        return iq_samples

    def build_frame(self):
        # Build the eCPRI frame (header + IQ payload)
        ecpri_header = self.build_ecpri_header()
        frame = ecpri_header + self.payload  # Concatenate the header with the IQ payload
        return frame

    def build_ecpri_header(self):
        # Build eCPRI header for Message Type 0
        header_length = 4  # 4 bytes for the header as per eCPRI specification
        common_header = bytearray(header_length)
        common_header[0] = 0x00  # Version: 0
        common_header[1] = 0x00  # Message Type: 0 (IQ Data)
        # Set Message Length: header length + IQ payload length
        message_length = len(self.payload)
        common_header[2:4] = message_length.to_bytes(2, byteorder='big')

        return common_header
