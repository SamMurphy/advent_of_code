#include <iostream>
#include <fstream>
#include <regex>
#include <algorithm>

#include "../Log.h"

bool IsSymbol(std::string str)
{
    const std::regex symbolPattern("[^\\.\\d\\s]");
    std::smatch match;
    if (std::regex_search(str, match, symbolPattern))
    {
        if (match.ready())
        {
            return true;
        }
    }
    return false;
}

int CheckLines(std::string& line, std::string& prevLine)
{
    int total = 0;

    const std::regex pattern("(\\d+)");
    std::sregex_iterator currentMatch(line.begin(), line.end(), pattern);
    std::sregex_iterator lastMatch = std::sregex_iterator();
    while (currentMatch != lastMatch)
    {
        std::smatch match = *currentMatch;
        int partNumber = std::stoi(match.str(1));

        // Check left, right, and above
        int startPos = std::max(0, int(match.position()) - 1);
        int endPos = std::min(int(match.position() + match.length()), int(line.length()));

        std::string above = "";
        if (prevLine.length() > 0)
        {
            int prevLineEndPos = std::min(endPos, int(prevLine.length()));
            int length = std::max(0, prevLineEndPos - startPos) + 1;
            above = prevLine.substr(startPos, length);
        }
        
        std::string neighbours = "";
        endPos = std::min(endPos, int(line.length() - 1));
        neighbours = line[endPos] + above + line[startPos];
        
        if (IsSymbol(neighbours))
        {
            total += partNumber;
            LOG_VERBOSE << "Part Number: " << partNumber;

            // Remove the part so that we don't hit it again
            line.replace(size_t(match.position()), size_t(match.length()), size_t(match.length()), '.');
        }

        currentMatch++;
    }

    return total;
}

int Part1(std::string input)
{
    int total = 0;

    // Read though the file line by line
    std::ifstream file(input);
    std::string line;
    std::string prevLine = "";
    while (std::getline(file, line))
    {
        total += CheckLines(line, prevLine);
        total += CheckLines(prevLine, line);

        prevLine = line;
    }

    return total;
}

int Part2(std::string input)
{
    return 0;
}

int main()
{
    Logger::ReportingLevel() = INFO;
    fopen_s(&Output::Stream(), "log.txt", "w");


    int test = Part1("example.txt");
    if (test != 4361)
    {
        LOG_ERROR << "PART 1 TEST FAILED - VALUE SHOULD BE 4361 - VALUE WAS: " << test;
        return -1;
    }
    LOG_VERBOSE << "Running Part 1...";
    int part1 = Part1("input.txt");
    LOG_INFO << "Part 1: " << part1;

    int test2 = Part2("example.txt");
    if (test2 != 467835)
    {
        LOG_ERROR << "PART 2 TEST FAILED - VALUE SHOULD BE 467835 - VALUE WAS: " << test2;
        return -1;
    }
    int part2 = Part2("input.txt");
    LOG_INFO << "Part 2: " << part2;

    return 0;
}