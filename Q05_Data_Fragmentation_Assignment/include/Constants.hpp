#ifndef CONSTANTS_HPP
#define CONSTANTS_HPP
#include <string>
#include <cmath>

namespace Constants {
    const int HEADER_LENGTH = 8;
    const int FOOTER_LENGTH = 4;
    const int PREAMBLE_LENGTH = 6;
    const int SMD_SX_BITS = 2;
    const int FRAGMENT_COUNT_BITS = 2;

    const std::string PAYLOAD_VALUE = "FF";

    const std::string PREAMBLE_VALUE = "07";
    const std::string SFD_VALUE = "D5";

    const std::string FOOTER_LAST = "AABBCCDD";
    const std::string FOOTER_NON_LAST = "11223344";

    const int MAX_SMD_SX = pow(2, SMD_SX_BITS);  // Cycle through 0-3 for SMD-Sx
    const int MAX_FRAGMENT_COUNT = pow(2, FRAGMENT_COUNT_BITS);  // Cycle through 0-3 for fragment count
}

#endif
