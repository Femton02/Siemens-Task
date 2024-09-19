#ifndef FOOTER_HPP
#define FOOTER_HPP

#include <string>
#include "../include/Constants.hpp"

class Footer {
public:
    Footer(bool isLastFragment) {generateFooter(isLastFragment);};
    std::string getFooter() const {return footer;};

private:
    std::string footer;
    void generateFooter(bool isLastFragment) {
        footer = isLastFragment ? Constants::FOOTER_LAST : Constants::FOOTER_NON_LAST;
    };
};

#endif
