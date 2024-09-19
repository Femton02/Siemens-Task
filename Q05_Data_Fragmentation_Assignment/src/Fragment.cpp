#include "../include/Fragment.hpp"

std::string Fragment::toString() const {
    std::string fragment = header.getHeader() + payload+ footer.getFooter();
    // Add padding if fragment size is less than channel width
    if (fragment.size() < static_cast<size_t>(channelWidth * 2)) {
        fragment += std::string(channelWidth * 2 - fragment.size(), '0');
    }
    return fragment;
}
