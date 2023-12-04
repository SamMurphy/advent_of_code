#include <iostream>
#include <fstream>
#include <regex>

#include "../Log.h"

static const std::regex gameIdPattern("Game (\\d+):");
static const int numberOfColours = 3;
static const std::regex colourPatterns[] = { 
        std::regex("(\\d+) red"), 
        std::regex("(\\d+) green"), 
        std::regex("(\\d+) blue")
    };

int Part1(std::string input)
{
    int total = 0;

    int maxCubes[] = { 12, 13, 14 };

    std::ifstream file(input);
    std::string line; 
    while (std::getline(file, line))
    {
        // Determine if the max showed cubes of each colour is more than the limits
        bool gamePossible = true;
        for (int i = 0; i < numberOfColours; i++)
        {
            std::sregex_iterator currentMatch(line.begin(), line.end(), colourPatterns[i]);
            std::sregex_iterator lastMatch = std::sregex_iterator();
            while (currentMatch != lastMatch)
            {
                std::smatch match = *currentMatch;
                int numberOfCubes = std::stoi(match.str(1));

                if (numberOfCubes > maxCubes[i])
                {
                    gamePossible = false;
                    break;
                }

                currentMatch++;
            }

            if (!gamePossible) break;
        }

        if (gamePossible)
        {
            // Get the game id
            std::smatch gameIdMatch;
            std::regex_search(line, gameIdMatch, gameIdPattern);
            int gameId = std::stoi(gameIdMatch.str(1));
            LOG_VERBOSE << "Game ID: " << gameId;

            total += gameId;
        }
    }

    return total;
}

int Part2(std::string input)
{
    int total = 0;

    std::ifstream file(input);
    std::string line; 
    while (std::getline(file, line))
    {
        int fewestCubes[] = {0,0,0};
        // Get the fewest cubes of each colour possible for a game
        for (int i = 0; i < numberOfColours; i++)
        {
            std::sregex_iterator currentMatch(line.begin(), line.end(), colourPatterns[i]);
            std::sregex_iterator lastMatch = std::sregex_iterator();
            while (currentMatch != lastMatch)
            {
                std::smatch match = *currentMatch;
                int numberOfCubes = std::stoi(match.str(1));

                if (numberOfCubes > fewestCubes[i])
                {
                    fewestCubes[i] = numberOfCubes;
                }

                currentMatch++;
            }
        }

        int powerOfSet = fewestCubes[0] * fewestCubes[1] * fewestCubes[2];
        total += powerOfSet;
    }

    return total;
}

int main()
{
    Logger::ReportingLevel() = INFO;

    int test = Part1("example.txt");
    if (test != 8)
    {
        LOG_ERROR << "PART 1 TEST FAILED - VALUE SHOULD BE 8 - VALUE WAS: " << test;
        return -1;
    }
    int part1 = Part1("input.txt");
    LOG_INFO << "Part 1: " << part1;

    int test2 = Part2("example.txt");
    if (test2 != 2286)
    {
        LOG_ERROR << "PART 2 TEST FAILED - VALUE SHOULD BE 2286 - VALUE WAS: " << test2;
        return -1;
    }
    int part2 = Part2("input.txt");
    LOG_INFO << "Part 2: " << part2;

    return 0;
}