import time
from config import Config
from packet import PacketGenerator

def main():
    # Load configuration
    config = Config('config/config.txt')

    # Initialize packet generator
    packet_generator = PacketGenerator(config)

    # Start packet generation
    packet_generator.generate_packets()

if __name__ == "__main__":
    main()
