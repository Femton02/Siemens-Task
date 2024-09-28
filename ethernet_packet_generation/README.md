
# Ethernet Packet Generator

## Overview
The Ethernet Packet Generator is a Python project designed to simulate the generation of Ethernet packets and eCPRI IQ Message Type 0 packets. The program allows users to configure various parameters such as packet size, burst periodicity, and the number of IQ samples while ensuring proper 4-byte alignment of the generated packets. The packets are generated in bursts and the results are stored in a JSON format.

## Features
- Configurable packet generation based on user-defined parameters.
- Supports both Ethernet and eCPRI over Ethernet packet formats.
- Ensures proper 4-byte alignment and handling of Inter-Frame Gaps (IFGs).
- Outputs generated packets to a JSON file.

## Project Structure
```
ethernet_packet_generation/
│
├── src/        # Contains all source .py files
├── output/     # Contains packets.json
├── tests/      # Contains all unit test .py files
├── config/     # Contains config.txt (configuration settings)
└── Makefile    # Makefile for running the project
```

## Requirements
- Python 3.x
- Make

## Installation
1. Clone the repository or download the files.

2. Navigate to the project directory:
   ```bash
   cd ethernet_packet_generation
   ```


## Usage

### Running the Main Program

To run the Ethernet Packet Generator, execute the following command:

```bash
make run
```

This command will generate packets based on the settings specified in the `config/config.txt` file.

### Running Unit Tests

To run the unit tests, use the following command:

```bash
make test
```

This command will discover and execute all unit tests located in the `tests/` directory.

### Cleaning Output

To clean the output directory and remove generated files, run:

```bash
make clean
```

## Configuration

The configuration settings can be modified in the `config/config.txt` file. The file includes parameters such as:

- `STREAM_DURATION_MS`: Total duration of packet generation.
- `BURST_SIZE`: Number of packets in one burst.
- `BURST_PERIODICITY_US`: Time interval between bursts in microseconds.
- `IFGs_NUMBER`: Number of bytes for Inter-Frame Gaps.
- `SOURCE_ADDRESS`, `DESTINATION_ADDRESS`: MAC addresses for packet generation.
- `ETHER_TYPE`: Type of Ethernet frames.
- `PAYLOAD_TYPE`: Type of payload (RANDOM or FIXED).
- `MAX_PACKET_SIZE`: Maximum packet size in bytes.
- `IQ_SAMPLE_NUM`: Number of IQ samples in one eCPRI packet.
- `PAYLOAD_BYTES_NUM`: Number of bytes in payload of regular Ethernet packet.