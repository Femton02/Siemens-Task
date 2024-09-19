#ifndef FRAGMENT_HPP
#define FRAGMENT_HPP

#include <string>
#include "Header.hpp"
#include "Footer.hpp"

class Fragment {
public:
    Fragment(int messageId, int fragmentId, const std::string& payload, bool isLastFragment, int channelWidth)
        : header(messageId, fragmentId, fragmentId == 0),
        payload(payload),
        footer(isLastFragment),
        fragmentId(fragmentId + 1),
        channelWidth(channelWidth)
        {};
    int getFragmentId() const { return fragmentId; };
    std::string getPayload() const { return payload; };
    std::string toString() const;

private:
    Header header;
    std::string payload;
    Footer footer;
    int fragmentId;
    int channelWidth;
};

#endif
