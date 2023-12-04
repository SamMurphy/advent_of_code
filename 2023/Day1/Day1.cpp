#include <iostream>
#include <fstream>
#include <regex>

#include "../Log.h"

// Ascii digits
static const int ascii_0 = int('0');
static const int ascii_9 = int('9');

int Part1(std::string input)
{
    int total = 0;

    // Read though the file line by line
    std::ifstream file(input);
    std::string line; 
    while (std::getline(file, line))
    {
        int first = 0;
        int last = 0;
        bool foundFirst = false;
        // Loop though the characters in the line
        for(char& c : line) 
        {
            // Check if the char is a digit
            if (int(c) >= ascii_0 && int(c) <= ascii_9)
            {
                int digit = int(c) - ascii_0;
                if (!foundFirst)
                {
                    first = digit;
                    foundFirst = true;
                }
                last = digit;
            }
        }
        total += first * 10;
        total += last;
        LOG_VERBOSE << "First: " << first << " Last: " << last;
    }
    LOG_VERBOSE << "Total: " << total;
    
    return total;
}

int StringToInt(std::string input)
{
    // If it's a digit then do the maths on the acsii value
    if (input.length() == 1)
    {
        return int(input[0]) - ascii_0;
    }

    static const std::string numbers[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    for (int i = 0; i < 9; i++)
    {
        if (input == numbers[i])
        {
            return i + 1;
        }
    }

    LOG_ERROR << "Failed to parse number correctly: " << input;
    return -1;
}

int Part2(std::string input)
{
    int total = 0;

    // ?= Lookahead means that the regex 'cursor' remains at the start of the mach, so that we can find overlapping matches like eightwo
    std::regex pattern("(?=(one|two|three|four|five|six|seven|eight|nine|\\d))");

    // Read though the file line by line
    std::ifstream file(input);
    std::string line; 
    while (std::getline(file, line))
    {
        std::string first = "";
        std::string last = "";
        bool foundFirst = false;

        std::sregex_iterator currentMatch(line.begin(), line.end(), pattern);
        std::sregex_iterator lastMatch = std::sregex_iterator();
        while (currentMatch != lastMatch)
        {
            std::smatch match = *currentMatch;
            if (!foundFirst)
            {
                first = match.str(1);
                foundFirst = true;
            }
            last = match.str(1);

            currentMatch++;
        }
        LOG_VERBOSE << "Line: " << line << " First: " << first << " Last: " << last;

        int foundNumber = StringToInt(first) * 10 + StringToInt(last);
        LOG_VERBOSE << "Found Number: " << foundNumber;
        
        total += foundNumber;
    }

    return total;
}


int main()
{
    Logger::ReportingLevel() = INFO;

    // Part 1
    int test = Part1("example.txt");
    if (test != 142)
    {
        LOG_ERROR << "PART 1 TEST FAILED - VALUE SHOULD BE 142 - VALUE WAS: " << test;
        return -1;
    }
    int part1 = Part1("input.txt");
    LOG_INFO << "Part 1: " << part1;

    // Part 2
    int test2 = Part2("example_part2.txt");
    if (test2 != 281)
    {
        LOG_ERROR << "PART 2 TEST FAILED - VALUE SHOULD BE 281 - VALUE WAS: " << test2;
        return -1;
    }
    int part2 = Part2("input.txt");
    LOG_INFO << "Part 2: " << part2;

    return 0;
}