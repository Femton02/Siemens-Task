class Config:
    def __init__(self, filename):
        self.stream_duration_ms = 0
        self.burst_size = 0
        self.burst_periodicity_us = 0
        self.ifgs_number = 0
        self.source_address = 0
        self.destination_address = 0
        self.ether_type = 0
        self.payload_type = ''
        self.packet_type = ''
        self.max_packet_size = 0
        self.iq_sample_num = 0
        self.load_config(filename)

    def load_config(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith("//") or line.startswith("\n"):
                    continue  # Ignore comments
                key, value = line.split('=')
                # remove the // after the value
                value = value.split('//')[0]
                # remove any whitespaces from the value
                value = value.strip()

                # Parse each configuration
                if key.strip() == 'STREAM_DURATION_MS':
                    self.stream_duration_ms = int(value)
                elif key.strip() == 'BURST_SIZE':
                    self.burst_size = int(value)
                elif key.strip() == 'BURST_PERIODICITY_US':
                    self.burst_periodicity_us = int(value)
                elif key.strip() == 'IFGs_NUMBER':
                    self.ifgs_number = int(value)
                elif key.strip() == 'SOURCE_ADDRESS':
                    self.source_address = int(value, 16)  # Hex conversion
                elif key.strip() == 'DESTINATION_ADDRESS':
                    self.destination_address = int(value, 16)
                elif key.strip() == 'ETHER_TYPE':
                    self.ether_type = int(value, 16)
                elif key.strip() == 'PAYLOAD_TYPE':
                    self.payload_type = value
                elif key.strip() == 'MAX_PACKET_SIZE':
                    self.max_packet_size = int(value)
                elif key.strip() == 'PACKET_TYPE':
                    self.packet_type = value
                elif key.strip() == 'IQ_SAMPLE_NUM':
                    self.iq_sample_num = int(value)
