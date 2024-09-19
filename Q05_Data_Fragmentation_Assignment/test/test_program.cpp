#include <iostream>
#include <cassert>
#include "Message.hpp"
#include "Fragment.hpp"
#include "Constants.hpp"

// Function to test the generateFragments method
void testGenerateFragments(int msgId, int length, int chWidth, const std::vector<std::string> expectedPayload) {
    // Test 1: Check number of fragments
    Message msg(msgId, length); // Example message
    int channelWidth = chWidth; // Example channel width

    auto fragments = msg.generateFragments(channelWidth);

    assert(fragments.size() == expectedPayload.size()); // Expecting 1 fragment
    std::cout << "Test 1 passed: Correct number of fragments\n";

    // Test 2: Check fragment payload
    for (size_t i = 0; i < fragments.size(); ++i) {
        assert(fragments[i].getPayload() == expectedPayload[i]);
        std::cout << "Test 2 passed for fragment " << i << "\n";
    }
}

int main() {
    std::cout << "Running tests...\n";
    std::cout << "Testing generating fragments\n";
    testGenerateFragments(1, 6, 20, {"FFFFFFFFFFFF"});
    testGenerateFragments(2, 5, 15, {"FFFFFF", "FFFF"});
    std::cout << "All tests passed!\n";
    return 0;
}
