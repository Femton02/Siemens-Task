#ifndef HEADER_HPP
#define HEADER_HPP

#include <string>

class Header {
public:
    Header(int messageId, int fragmentId, bool isFirstFragment) {generateHeader(messageId, fragmentId, isFirstFragment);};
    std::string getHeader() const {return header;};

private:
    std::string header;
    void generateHeader(int messageId, int fragmentId, bool isFirstFragment);
    std::string intToBinaryString(int value, bool isFragmentCount);
};

#endif
