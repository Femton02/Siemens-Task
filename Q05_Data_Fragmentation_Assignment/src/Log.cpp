#include "../include/Log.hpp"
#include <iostream>

Log::Log() {
    // Open the log file in append mode
    logFile.open("./docs/message_log.txt", std::ios::out | std::ios::app);
}

Log::~Log() {
    if (logFile.is_open()) {
        logFile.close();
    }
}

void Log::writeMessage(int messageId, int fragmentId, const std::string& fragment) {
    logFile << messageId << ", " << fragmentId << ", ";
    // Format the output to be more readable
    for (size_t i = 0; i < fragment.size(); i++) {
        logFile << fragment[i];
        // Add space between bytes
        if (i % 2 == 1 && i != fragment.size() - 1) {
            logFile << " ";
        }
    }
    logFile << std::endl;
}
