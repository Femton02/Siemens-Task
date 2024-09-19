#include <iostream>
#include <cstdlib> // For std::atoi
#include "../include/MessageGenerator.hpp"
#include "../include/constants.hpp"

int main(int argc, char* argv[]) {
    // Check if enough arguments are provided
    if (argc != 4) {
        std::cout << "Usage: " << argv[0] << " <numMessages> <messageLength> <channelWidth>\n";
        return 1;
    }

    // Parse command-line arguments
    int numMessages = std::atoi(argv[1]);
    int messageLength = std::atoi(argv[2]);
    int channelWidth = std::atoi(argv[3]);

    // Validate number of messages
    if (numMessages < 0) {
        std::cout << "Error: Number of messages must be non-negative.\n";
        return 1;
    }

    // Validate message length
    // Min length is set to 2 for testing purposes
    if (messageLength < 64 || messageLength > 16000) {
        std::cout << "Error: Message length must be between 64 and 16,000 bytes.\n";
        return 1;
    }

    // Validate channel width
    if (channelWidth <= (Constants::HEADER_LENGTH + Constants::FOOTER_LENGTH)) {
        std::cout << "Error: Channel width must be larger than header + footer size (" 
                  << (Constants::HEADER_LENGTH + Constants::FOOTER_LENGTH) << " bytes).\n";
        return 1;
    }
    // Create an instance of the MessageGenerator and start generating messages
    MessageGenerator generator;
    generator.run(numMessages, messageLength, channelWidth);

    return 0;
}