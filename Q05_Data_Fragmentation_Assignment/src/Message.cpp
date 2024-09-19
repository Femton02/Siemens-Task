#include "../include/Message.hpp"
#include "../include/Constants.hpp"

std::vector<Fragment> Message::generateFragments(int channelWidth) {
    std::vector<Fragment> fragments;
    int payloadLengthPerFragment = channelWidth - Constants::HEADER_LENGTH - Constants::FOOTER_LENGTH;  // Channel width minus header and footer sizes
    int remainingLength = length;
    int fragmentId = 0;

    // Break message into fragments
    while (remainingLength > 0) {
        int fragmentLength = std::min(payloadLengthPerFragment, remainingLength);
        Fragment fragment(messageId, fragmentId, payload.substr(fragmentId* payloadLengthPerFragment, fragmentLength * 2), remainingLength <= payloadLengthPerFragment, channelWidth);
        fragmentId++;
        fragments.emplace_back(fragment);
        remainingLength -= fragmentLength;
    }

    return fragments;
}

std::string Message::generatePayload(int length) {
    std::string payload = "";
    for (int i = 0; i < length; i++) {
        payload += Constants::PAYLOAD_VALUE; // Add payload value
    }
    return payload;
}
