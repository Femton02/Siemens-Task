# Project README

## Connection Manager Code Review

### Overview
This project involves reviewing and providing feedback on a connection manager codebase responsible for managing server-client connections. The code handles broadcasting formatted messages between the server and multiple clients. The review focuses on identifying issues, suggesting improvements, and ensuring robust error handling.

### Review Summary
- **Issue Identification**: Identified problems related to message handling, including improper trimming of messages, incorrect server removal from the client list upon closure, and inadequate error handling for unknown prefixes.
- **Recommendations**: Suggested improvements to error handling, message formatting, and message length validation to prevent crashes.
- **Bug Report**: Documented specific bugs and their potential impact, along with suggested fixes and enhancements.

---

## Data Fragmentation Code Implementation

### Overview
This project focuses on implementing a system for generating and managing message fragments between a server and client. The implementation simulates sending messages with specified lengths, channels, and number of messages, ensuring that fragments are logged and formatted correctly.

### Recent Changes
- **Code Implementation**: Completed the initial setup of the message generation code, including fragmentation and logging of message fragments.
- **Validation**: Added input validation and ensured the code is runnable with a Makefile on Linux OS.
- **Directory Structure**:
  - `src/`: Contains `main.cpp` and other source files responsible for the core functionality of message generation and handling.
  - `include/`: Header files defining interfaces and constants for message generation.
  - `test/`: Contains unit tests for validating message generation.
  - `docs/`: Documentation related to the data fragmentation codebase.
- **Makefile**: Updated the Makefile to include commands for running the program with specified arguments and testing the implementation.

### Usage
To compile and run the program, use the following commands:

```sh
make
make run ARGS="VALUE1 VALUE2 VALUE3"
```

To run tests:
```sh
make test
```

---
## Ethernet Packet Generator

### Overview
The Ethernet Packet Generator project is designed to simulate the generation of Ethernet packets and eCPRI IQ Message Type 0 packets. Users can configure various parameters such as packet size, burst periodicity, and the number of IQ samples while ensuring proper 4-byte alignment of the generated packets. The project generates packets in bursts and logs the results in a JSON file.

### Features
- Configurable packet generation based on user-defined parameters.
- Supports Ethernet and eCPRI over Ethernet packet formats.
- Ensures proper 4-byte alignment and handling of Inter-Frame Gaps (IFGs).
- Outputs generated packets to a JSON file.


### Usage

#### Running the Main Program

To run the Ethernet Packet Generator, execute the following command:

```sh
make run
```

This command generates packets based on the settings specified in the `config/config.txt` file.

#### Running Unit Tests

To run the unit tests, use the following command:

```sh
make test
```
