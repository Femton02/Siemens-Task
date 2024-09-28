import unittest
from src.ecpri_frame import eCPRIFrame

class TestECPRI(unittest.TestCase):
        
    def test_create_ecpri_frame(self):
        """
        Test the creation of an eCPRI frame
        """
        ecpri_frame = eCPRIFrame(num_samples=4)
        self.assertIsInstance(ecpri_frame.frame, bytearray)
        self.assertEqual(len(ecpri_frame.frame), 4 * 4 + 4)  # 4 IQ samples of 4 bytes each + 4 bytes for the header

    def test_create_ecpri_frame_large(self):
        """
        Test the creation of an eCPRI frame with a large number of IQ samples
        """
        ecpri_frame = eCPRIFrame(num_samples=80)
        self.assertIsInstance(ecpri_frame.frame, bytearray)
        self.assertEqual(len(ecpri_frame.frame), 80 * 4 + 4)

    def test_create_header(self):
        """
        Test the creation of an eCPRI header
        """
        ecpri_frame = eCPRIFrame(num_samples=4)
        header = ecpri_frame.build_ecpri_header()
        self.assertIsInstance(header, bytearray)
        self.assertEqual(len(header), 4)
        self.assertEqual(header[0], 0x00)


if __name__ == '__main__':
    unittest.main()