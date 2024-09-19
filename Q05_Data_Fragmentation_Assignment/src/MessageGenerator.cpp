#include "../include/MessageGenerator.hpp"
#include "../include/Constants.hpp"
#include <iostream>

void MessageGenerator::run(int numMessages, int messageLength, int channelWidth) {
    Log logger;  // Create a logger to log message fragments
    for (int i = 0; i < numMessages; i++) {
        // Generate a message of specified length
        Message msg = generateMessage(messageLength);

        // Fragment the message based on the channel width
        std::vector<Fragment> fragments = msg.generateFragments(channelWidth);

        // Log each fragment to the file
        for (size_t j = 0; j < fragments.size(); ++j) {
            logger.writeMessage(msg.getMessageId(), fragments[j].getFragmentId(), fragments[j].toString()); // Fragment ID starts from 1
        }
    }
}

Message MessageGenerator::generateMessage(int length) {
    // Increment message ID and generate a message with random payload
    currentMessageId = (currentMessageId + 1) % Constants::MAX_SMD_SX;  // Cycle between 0 to 3 for message ID
    return Message(currentMessageId, length);
}
