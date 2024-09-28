import unittest
from src.packet import PacketGenerator
from src.config import Config
from src.ecpri_frame import eCPRIFrame
from src.ethernet_frame import EthernetFrame
from src.utils import crc32, get_ifg_padding

class TestPacketGenerator(unittest.TestCase):
    
    # def test_simulation_time(self):
    #     config = Config('config/config.txt')
    #     packet_generator = PacketGenerator(config)
    #     packet_generator.generate_packets()
    #     self.assertEqual(packet_generator.simulated_time, config.stream_duration_ms * 1000)

    def test_create_ethernet_packet(self):
        """
        Test the creation of an Ethernet packet
        """
        config = Config("config/config.txt")
        config.stream_duration_ms = 1
        config.burst_size = 3
        config.burst_periodicity_us = 100
        config.ifgs_number = 30
        config.source_address = 0x102030405060
        config.destination_address = 0x102030302010
        config.ether_type = 0x0800
        config.payload_type = 'RANDOM'
        config.packet_type = 'ECPRI'
        config.max_packet_size = 426
        config.iq_sample_num = 4
        packet_generator = PacketGenerator(config)
        packet = packet_generator._create_packet()
        self.assertIsInstance(packet, bytes)

    def test_create_ecpri_packet(self):
        """
        Test the creation of an eCPRI packet
        """
        config = Config("config/config.txt")
        config.stream_duration_ms = 1
        config.burst_size = 3
        config.burst_periodicity_us = 100
        config.ifgs_number = 30
        config.source_address = 0x102030405060
        config.destination_address = 0x102030302010
        config.ether_type = 0x0800
        config.payload_type = 'RANDOM'
        config.packet_type = 'ECPRI'
        config.max_packet_size = 426
        config.iq_sample_num = 4
        packet_generator = PacketGenerator(config)
        packet = packet_generator._create_packet()
        self.assertIsInstance(packet, bytes)

    def test_get_ether_type(self):
        """
        Test the get_ether_type method of the PacketGenerator
        """
        config = Config("config/config.txt")
        config.packet_type = 'ECPRI'
        packet_generator = PacketGenerator(config)
        ether_type = packet_generator._get_ether_type()
        self.assertEqual(ether_type, 0xAEFE)

        config.packet_type = 'ETHERNET'
        config.ether_type = 0x0800
        packet_generator = PacketGenerator(config)
        ether_type = packet_generator._get_ether_type()
        self.assertEqual(ether_type, 0x0800)

    def test_generate_payload(self):
        """
        Test the fixed payload generation of the ethernet packet
        """
        config = Config("config/config.txt")
        config.payload_type = 'FIXED'
        config.packet_type = 'ETHERNET'
        packet_generator = PacketGenerator(config)
        payload = packet_generator._generate_payload()
        self.assertEqual(payload, b'THIS IS A TEST')

    

if __name__ == '__main__':
    unittest.main()
