from ethernet_frame import EthernetFrame
from ecpri_frame import eCPRIFrame
from utils import get_ifg_padding
from logger import PacketLogger
import random

class PacketGenerator:
    def __init__(self, config):
        self.config = config
        self.simulated_time = 0  # Simulated time in µs
        self.logger = PacketLogger("packets.json")

    def generate_packets(self):
        """
        Generate and send packets based on the configuration
        """
        total_duration_us = self.config.stream_duration_ms * 1000  # Convert ms to µs
        time_per_packet = self.config.burst_periodicity_us / self.config.burst_size

        while self.simulated_time < total_duration_us:  # Loop until the stream duration is reached
            if self.simulated_time + self.config.burst_periodicity_us <= total_duration_us: # Check if burst can be sent
                self._send_burst()
                self._send_ifgs()
                self.simulated_time += self.config.burst_periodicity_us
                print (f"Simulated time after burst: {self.simulated_time} µs")
            else:
                for _ in range(self.config.burst_size): # Send the remaining packets one by one
                    if self.simulated_time + time_per_packet <= total_duration_us:
                        self._send_packet()
                        self.simulated_time += time_per_packet
                    else:
                        print (f"Stream duration ended, sending IFGs...")
                        self._send_ifgs()
                        self.simulated_time = total_duration_us
                        break
        print (f"Stream duration finished, simulation ends at time: {self.simulated_time} µs")

    def _send_burst(self):
        """
        Send a burst of packets.
        """
        for _ in range(self.config.burst_size):
            self._send_packet()

    def _send_packet(self):
        """
        Send and log an Ethernet packet with an optional Inter-Frame Gap (IFG) padding.
        """
        # Create the packet
        packet = self._create_packet()

        if packet is None:
            # Log the dropped packet
            self.logger.log_dropped_packet("Packet dropped due to size, sending IFGs...")
            self._send_ifgs()
            return
        # Log the packet
        self.logger.log_packet(packet)

        # Align the packet to the line rate
        ifg_padding = get_ifg_padding(packet)

        # log the IFG padding
        if ifg_padding:
            self.logger.log_IFG(ifg_padding)

        # Send the packet + IFG padding
        print(f"Sending packet: {packet.hex() + ifg_padding.hex()}")

    def _create_packet(self):
        """
        Create an Ethernet packet.
        :return: The Ethernet packet as a byte sequence.
        """
        # Create the Ethernet frame (common for both types)
        ethernet_frame = EthernetFrame(
            src_addr=self.config.source_address,
            dest_addr=self.config.destination_address,
            ether_type=self._get_ether_type(),  # Choose the appropriate EtherType
            payload=self._generate_payload(),    # Payload based on packet type
            max_size=self.config.max_packet_size
        )
        return ethernet_frame.frame

    def _get_ether_type(self):
        """
        Get the appropriate EtherType based on the packet type configuration.
        :return: The EtherType as an integer.
        """
        # Return the correct EtherType based on packet type
        if self.config.packet_type == "ECPRI":
            return 0xAEFE  # EtherType for eCPRI
        else:
            return self.config.ether_type  # Standard EtherType

    def _generate_payload(self):
        """
        Generate the payload based on the packet type.
        :return: The payload as a byte sequence.
        """
        if self.config.packet_type == "ECPRI":
            # Create an eCPRI frame with the number of IQ samples specified in the configuration
            num_samples = self.config.iq_sample_num
            ecpri_frame = eCPRIFrame(num_samples=num_samples)  # Pass the number of samples
            return ecpri_frame.frame
        else:
            # Standard Ethernet payload (random or fixed)
            return self._generate_standard_payload()

    def _generate_standard_payload(self):
        """
        Generate a standard Ethernet payload based on the configuration.
        :return: The payload as a byte sequence.
        """
        # Generate the standard Ethernet payload
        if self.config.payload_type == "RANDOM":
            return bytearray(random.getrandbits(8) for _ in range(self.config.payload_bytes_num))  # Example standard data
        else:
            return bytearray(b'THIS IS A TEST')  # Example fixed value

    def _send_ifgs(self):
        """
        Send Inter-Frame Gaps (IFGs) if the packet is discarded or streaming ends.
        """

        remainder = self.config.ifgs_number % 4
        if remainder != 0:
            # Calculate how many bytes to add to make the length a multiple of 4
            padding_needed = 4 - remainder
            ifg_padding = b'\x07' * padding_needed
            self.logger.log_IFG(ifg_padding)
            print(f"Adding {padding_needed} bytes of IFG padding for 4-byte alignment: {ifg_padding.hex()}")

        # IFGs are inserted as padding, with a value of 0x07
        ifg = b'\x07' * self.config.ifgs_number
        self.logger.log_IFG(ifg)
        print(f"Sending IFGs: {ifg.hex()}")

