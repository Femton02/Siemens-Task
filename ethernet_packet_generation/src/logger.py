import json
import os
import binascii

class PacketLogger:
    def __init__(self, output_file: str):
        # Get the directory of the current file (where logger.py resides)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Go up one level to the 'ethernet_packet_generation' directory
        project_dir = os.path.dirname(current_dir)

        # Construct the full path to the 'output' folder
        output_dir = os.path.join(project_dir, 'output')

        # Ensure that the 'output' directory exists, if not, create it
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Construct the full path to the output file
        self.output_file = os.path.join(output_dir, output_file)

        # Check if the file already exists; if not, create and initialize it
        if not os.path.exists(self.output_file):
            with open(self.output_file, 'w') as f:
                json.dump([], f)  # Initialize with an empty list
        
    def log_packet(self, packet: bytes):
        """
        Parse a packet from its raw bytes and append its fields to the JSON log.

        :param packet: The Ethernet packet as a byte sequence.
        """
        packet_data = self._parse_packet(packet)
        
        # Read the existing data, append the new packet, and rewrite the file
        with open(self.output_file, 'r+') as f:
            # Load the existing data from the file
            packets = json.load(f)
            
            # Append the new packet data
            packets.append(packet_data)
            
            # Move the file pointer to the beginning of the file to overwrite
            f.seek(0)
            # Write the updated list of packets back to the file
            json.dump(packets, f, indent=4)
            # Flush to ensure it's written immediately
            f.flush()
    
    def log_IFG(self, IFG: bytes):
        """
        Log an Inter-Frame Gap (IFG) to the JSON log.

        :param IFG: The Inter-Frame Gap as a byte sequence.
        """
        # Convert the IFG to a hexadecimal string for logging
        IFG_hex = binascii.hexlify(IFG).decode()
        
        # Read the existing data, append the new IFG, and rewrite the file
        with open(self.output_file, 'r+') as f:
            # Load the existing data from the file
            packets = json.load(f)
            
            # Append the new IFG data
            packets.append({"IFG": IFG_hex})
            
            # Move the file pointer to the beginning of the file to overwrite
            f.seek(0)
            # Write the updated list of packets back to the file
            json.dump(packets, f, indent=4)
            # Flush to ensure it's written immediately
            f.flush()

    def log_dropped_packet(self, message: str):
        """
        Log a message indicating that a packet was dropped.

        :param message: The reason why the packet was dropped.
        """
        with open(self.output_file, 'r+') as f:
            # Append the message to the file
            packets = json.load(f)

            # Append the new dropped packet message
            packets.append({"dropped_packet": message})
            
            # Move the file pointer to the beginning of the file to overwrite
            f.seek(0)

            # Write the updated list of packets back to the file
            json.dump(packets, f, indent=4)

            # Flush to ensure it's written immediately
            f.flush()
    
    def _parse_packet(self, packet: bytes) -> dict:
        """
        Parse an Ethernet packet from bytes into its components.

        :param packet: The raw Ethernet packet as bytes.
        :return: A dictionary with parsed fields from the packet.
        """

        # Parse the fields based on the Ethernet structure
        preamble = packet[:7]  # 7 bytes preamble
        sof = packet[7:8]      # 1 byte SOF (Start of Frame)
        dest_mac = packet[8:14] # 6 bytes Destination MAC
        src_mac = packet[14:20] # 6 bytes Source MAC
        ethertype = packet[20:22] # 2 bytes EtherType/Length
        data = packet[22:-4]    # Data field (everything until 4 bytes before the end)
        crc = packet[-4:]       # Last 4 bytes (CRC)

        if ethertype != b'\xAE\xFE':
            # Convert to hexadecimal strings for readability
            packet_data = {
                "preamble": binascii.hexlify(preamble).decode(),
                "SOF": binascii.hexlify(sof).decode(),
                "destination_adrs": ':'.join(f'{b:02x}' for b in dest_mac),
                "source_adrs": ':'.join(f'{b:02x}' for b in src_mac),
                "ethertype/length": binascii.hexlify(ethertype).decode(),
                "data": binascii.hexlify(data).decode(),
                "crc32": binascii.hexlify(crc).decode(),
            }
            return packet_data
        else:
            # eCPRI packet
            packet_data = {
                "preamble": binascii.hexlify(preamble).decode(),
                "SOF": binascii.hexlify(sof).decode(),
                "destination_adrs": ':'.join(f'{b:02x}' for b in dest_mac),
                "source_adrs": ':'.join(f'{b:02x}' for b in src_mac),
                "ethertype/length": binascii.hexlify(ethertype).decode(),
                "eCPRI data": self._parse_ecpri_data(data),
                "crc32": binascii.hexlify(crc).decode(),
            }
            return packet_data
        
    def _parse_ecpri_data(self, data: bytes) -> dict:
        """
        Parse the eCPRI data field into its components.

        :param data: The eCPRI data field as bytes.
        :return: A dictionary with parsed fields from the eCPRI data.
        """
        # Parse the eCPRI header fields
        version = data[0]  # Version (1 byte)
        message_type = data[1]
        message_length = int.from_bytes(data[2:4], byteorder='big')
        data_payload = data[4: 4 + message_length]  # Data payload based on message length
        padding = data[4 + message_length:]  # Padding (if any)

        # Convert to hexadecimal strings for readability
        ecpri_data = {
            "version": version,
            "message_type": message_type,
            "message_length": message_length,
            "data_payload": binascii.hexlify(data_payload).decode(),
            "padding": binascii.hexlify(padding).decode(),
        }

        return ecpri_data
