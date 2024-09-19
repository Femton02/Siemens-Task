#ifndef MESSAGE_GENERATOR_HPP
#define MESSAGE_GENERATOR_HPP

#include "Message.hpp"
#include "Log.hpp"

class MessageGenerator {
public:
    void run(int numMessages, int messageLength, int channelWidth);
private:
    int currentMessageId = 0;
    Message generateMessage(int length);
};

#endif
