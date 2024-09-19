#include "../include/Header.hpp"
#include "../include/Constants.hpp"
#include <bitset>
#include <iomanip>


void Header::generateHeader(int messageId, int fragmentId, bool isFirstFragment) {
    header = "";

    // Add preamble to header
    for(int i = 0; i < Constants::PREAMBLE_LENGTH; i++) {
        header += Constants::PREAMBLE_VALUE;
    }

    // Add message id to header in 2 digit hex format
    header += intToBinaryString(messageId - 1, false); // Subtract 1 to make it 0-indexed

    // Add SFD / fragment count to header
    isFirstFragment ? header += Constants::SFD_VALUE : header += intToBinaryString(fragmentId - 1, true);
}

std::string Header::intToBinaryString(int value, bool isFragmentCount) {
    // Convert integer to binary string
    if (isFragmentCount) {
        std::bitset<Constants::FRAGMENT_COUNT_BITS> bits(value);
        return bits.to_string();
    }
    else {
        std::bitset<Constants::SMD_SX_BITS> bits(value);
        return bits.to_string();
    }
}

