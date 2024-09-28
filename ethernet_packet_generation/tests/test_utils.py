import unittest
from src.utils import crc32, get_ifg_padding

class TestUtils(unittest.TestCase):

    def test_crc32(self):
        data = b"Hello, world!"
        crc = crc32(data)
        self.assertEqual(crc, b'\xeb\xe6\xc6\xe6')

        data = b"THIS IS A TEST MESSAGE"
        crc = crc32(data)
        self.assertEqual(crc, b'\x19M\xdfI')

    def test_get_ifg_padding(self):
        packet = bytes([0xAA] * 62)  # Length not a multiple of 4
        padding = get_ifg_padding(packet)
        self.assertEqual(padding, b'\x07\x07')

        packet = bytes([0xAA] * 64)  # Length already a multiple of 4
        padding = get_ifg_padding(packet)
        self.assertEqual(padding, b'')  # No padding needed

if __name__ == '__main__':
    unittest.main()
