#ifndef MESSAGE_HPP
#define MESSAGE_HPP

#include <vector>
#include <string>
#include "Fragment.hpp"

class Message {
public:
    Message(int messageId, int length): messageId(messageId), length(length) {payload = generatePayload(length);};
    std::vector<Fragment> generateFragments(int channelWidth);
    int getMessageId() const {return messageId;};
private:
    int messageId;
    int length;
    std::string payload;
    std::string generatePayload(int length);
};

#endif