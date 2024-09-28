import os
from config import Config
from packet import PacketGenerator

def main():
    """
    Main function to generate packets
    """
    # Load configuration
    filename = 'config.txt'
    config = Config(filename)

    # Initialize packet generator
    packet_generator = PacketGenerator(config)

    # Start packet generation
    packet_generator.generate_packets()

if __name__ == "__main__":
    main()
