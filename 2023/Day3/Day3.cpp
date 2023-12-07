#include <iostream>
#include <fstream>
#include <regex>
#include <vector>

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

struct Item 
{
    int startPos;
    int endPos;
    int lineNumber;
    std::string text;
    bool isCog;

    Item() : startPos(-1), endPos(-1), lineNumber(-1), text(""), isCog(false) {}
};

bool IsCog(std::string str)
{
    const std::regex symbolPattern("[*]");
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

void MatchPatten(std::string pattern, std::string line, std::vector<Item>& items, int lineNumber, bool isCog = false)
{
    std::regex rgxPattern(pattern);
    std::sregex_iterator currentMatch(line.begin(), line.end(), rgxPattern);
    std::sregex_iterator lastMatch = std::sregex_iterator();
    while (currentMatch != lastMatch)
    {
        std::smatch match = *currentMatch;
        std::string number = match.str(1);

        Item item;
        item.text = number;
        item.startPos = match.position();
        item.endPos = std::min(int(match.position() + match.length()), int(line.length()));
        item.lineNumber = lineNumber;
        item.isCog = isCog;

        items.push_back(item);

        currentMatch++;
    }
}

int Part2(std::string input)
{
    // Read though the file line by line
    std::ifstream file(input);
    std::string line;
    std::vector<Item> items;
    int lineNumber = 0;
    while (std::getline(file, line))
    {
        MatchPatten("(\\d+)", line, items, lineNumber);
        MatchPatten("([*])", line, items, lineNumber, true);
        lineNumber++;
    }

    int total = 0;
    for (auto &item : items)
    {
        if (item.isCog)
        {
            int adjCount = 0;
            int product = 1;
            for (auto &neighbour: items)
            {
                // Check it's a number
                if (neighbour.isCog == false)
                {
                    if (neighbour.lineNumber <= item.lineNumber + 1 &&
                        neighbour.lineNumber >= item.lineNumber - 1)
                    {
                        // Check if it's adjacent
                        if (item.startPos >= neighbour.startPos - 1 &&
                            item.endPos <= neighbour.endPos + 1)
                        {
                            adjCount++;
                            int partNumber = std::stoi(neighbour.text);
                            product *= partNumber;
                        }
                    }
                }
            }
            if (adjCount == 2)
            {
                total += product;
            }
        }
    }

    return total;
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