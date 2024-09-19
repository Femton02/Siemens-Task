#ifndef LOG_HPP
#define LOG_HPP

#include <fstream>
#include <string>

class Log {
public:
    Log();
    ~Log();
    void writeMessage(int messageId, int fragmentId, const std::string& fragment);
private:
    std::ofstream logFile;
};

#endif
