import unittest
from src.config import Config
import os

class TestConfig(unittest.TestCase):

    def setUp(self):
        # Create a sample config file for testing
        self.sample_config_file = 'test_config.cfg'
        with open(self.sample_config_file, 'w') as f:
            f.write('STREAM_DURATION_MS=5000\n')
            f.write('BURST_SIZE=1500\n')
            f.write('BURST_PERIODICITY_US=1000\n')
            f.write('IFGs_NUMBER=10\n')
            f.write('SOURCE_ADDRESS=0xAABBCCDDEEFF\n')
            f.write('DESTINATION_ADDRESS=0x112233445566\n')
            f.write('ETHER_TYPE=0x0800\n')
            f.write('PAYLOAD_TYPE=Data\n')
            f.write('PACKET_TYPE=eCPRI\n')
            f.write('MAX_PACKET_SIZE=9000\n')
            f.write('IQ_SAMPLE_NUM=256\n')

    def tearDown(self):
        # Remove the sample config file after testing
        os.remove(self.sample_config_file)

    def test_load_config(self):
        config = Config(self.sample_config_file)
        self.assertEqual(config.stream_duration_ms, 5000)
        self.assertEqual(config.burst_size, 1500)
        self.assertEqual(config.burst_periodicity_us, 1000)
        self.assertEqual(config.ifgs_number, 10)
        self.assertEqual(config.source_address, 0xAABBCCDDEEFF)
        self.assertEqual(config.destination_address, 0x112233445566)
        self.assertEqual(config.ether_type, 0x0800)
        self.assertEqual(config.payload_type, 'Data')
        self.assertEqual(config.packet_type, 'eCPRI')
        self.assertEqual(config.max_packet_size, 9000)
        self.assertEqual(config.iq_sample_num, 256)

if __name__ == '__main__':
    unittest.main()
