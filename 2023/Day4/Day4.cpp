#include <iostream>
#include <fstream>
#include <regex>
#include <vector>
#include <map>

#include "../Log.h"

void ParseNumbers(std::string input, std::vector<int>& nums)
{
    std::regex pattern("(\\d+)");
    std::sregex_iterator currentMatch(input.begin(), input.end(), pattern);
    std::sregex_iterator lastMatch = std::sregex_iterator();
    while (currentMatch != lastMatch)
    {
        std::smatch match = *currentMatch;
        std::string numStr = match.str(1);
        int num = std::stoi(numStr);
        nums.push_back(num);

        currentMatch++;
    }
}

void ParseLine(std::string line, std::vector<int>& winningNums, std::vector<int>& ourNums)
{
    const std::regex pattern(": ([\\d+\\s+]+)\\| ([\\d+\\s+]+)$");
    std::sregex_iterator currentMatch(line.begin(), line.end(), pattern);
    std::sregex_iterator lastMatch = std::sregex_iterator();
    while (currentMatch != lastMatch)
    {
        std::smatch match = *currentMatch;

        std::string winningNumsStr = match.str(1);
        ParseNumbers(winningNumsStr, winningNums);
        std::string ourNumsStr = match.str(2);
        ParseNumbers(ourNumsStr, ourNums);

        currentMatch++;
    }
}

int Part1(std::string input)
{
    int total = 0;

    // Read though the file line by line
    std::ifstream file(input);
    std::string line; 
    while (std::getline(file, line))
    {
        // Get the numbers
        std::vector<int> winningNums;
        std::vector<int> ourNums;
        ParseLine(line, winningNums, ourNums);

        int points = 0;
        bool first = true;
        for (int num : ourNums)
        {
            for (int winningNum : winningNums)
            {
                if (num == winningNum)
                {
                    if (first)
                    {
                        first = false;
                        points = 1;
                    }
                    else
                    {
                        points *= 2;
                    }
                }
            }
        }
        total += points;
    }
    return total;
}

int Part2(std::string input)
{
    int totalCards = 0;
    std::map<int, int> cards;
    int currentCard = 0;
    // Read though the file line by line
    std::ifstream file(input);
    std::string line; 
    while (std::getline(file, line))
    {
        // Get the numbers
        std::vector<int> winningNums;
        std::vector<int> ourNums;
        ParseLine(line, winningNums, ourNums);

        int numThisCard = 1;
        if (cards.find(currentCard) != cards.end())
        {
            numThisCard += cards[currentCard];
        }

        int numWinners = 0;
        for (int winningNum : winningNums)
        {
            for (int num : ourNums)
            {
                if (num == winningNum)
                {
                    numWinners++;
                }
            }
        }

        for (int i = 1; i <= numWinners; i++)
        {
            if (cards.find(currentCard + i) == cards.end())
            {
                // haven't won any of these cards yet
                cards[currentCard + i] = numThisCard;
            }
            else
            {
                // already won some
                cards[currentCard + i] += numThisCard;
            }
        }

        totalCards += numThisCard;
        currentCard++;
    }
    return totalCards;
}

int main()
{
    Logger::ReportingLevel() = INFO;

    // Part 1
    int test = Part1("example.txt");
    if (test != 13)
    {
        LOG_ERROR << "PART 1 TEST FAILED - VALUE SHOULD BE 13 - VALUE WAS: " << test;
        return -1;
    }
    int part1 = Part1("input.txt");
    LOG_INFO << "Part 1: " << part1;

    // Part 2
    int test2 = Part2("example.txt");
    if (test2 != 30)
    {
        LOG_ERROR << "PART 2 TEST FAILED - VALUE SHOULD BE 30 - VALUE WAS: " << test2;
        return -1;
    }
    int part2 = Part2("input.txt");
    LOG_INFO << "Part 2: " << part2;

    return 0;
}