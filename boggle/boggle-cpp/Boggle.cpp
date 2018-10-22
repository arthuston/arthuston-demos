/**
 * Boggle puzzle game.
 * @author art@arthuston.com
 */

#include "Boggle.hpp"
#include <Algorithm>

void Boggle::solve(const std::set<std::string> &words, std::list<std::string> &foundWords) {
    foundWords.clear();

    // look for complete word starting at each character
    for (int row = 0; row < puzzle.size(); row++) {
        for (int col = 0; col < puzzle.size(); col++) {
            // find words at current position
            Position position(row, col);
            std::set<Position> visited;
            std::string partialWord;

            solvePosition(position, visited, partialWord, words, foundWords);
        }
    }
}

void Boggle::solvePosition(const std::pair<int, int> &position,
                           std::set<std::pair<int, int>> &visited,
                           const std::string &partialWord,
                           const std::set<std::string> &matchingWords,
                           std::list<std::string> &foundWords) {
    // add this position to visited,
    // and add character to partial word
    visited.insert(position);
    char ch = puzzleChar(position);
    std::string newPartialWord = std::string(partialWord);
    newPartialWord.push_back(ch);

    // check exact match
    if (matchingWords.find(newPartialWord) != matchingWords.end()) {
        foundWords.push_back(newPartialWord);
    }

    // check partial words
    std::set<std::string> newMatchingWords;
    findPartialMatches(newPartialWord, matchingWords, newMatchingWords);

    // add neighboring characters to the partial word
    if (newMatchingWords.size() > 0) {
        std::pair<int, int> rowNeighbors;
        getRowColNeighbors(position.first, rowNeighbors);
        std::pair<int, int> colNeighbors;
        getRowColNeighbors(position.second, colNeighbors);

        for (int row = rowNeighbors.first; row <= rowNeighbors.second; row++) {
            for (int col = colNeighbors.first; col <= colNeighbors.second; col++) {
                Position nextPosition(row, col);
                if (visited.find(nextPosition) == visited.end()) {
                    solvePosition(nextPosition,
                                  visited, newPartialWord, newMatchingWords, foundWords);
                }
            }
        }
    }

    visited.erase(position);
}

void Boggle::findPartialMatches(const std::string &partialWord, const std::set<std::string> &matchingWords,
                                std::set<std::string> &newMatchingWords) {
    newMatchingWords.clear();
    for (std::string matchingWord : matchingWords) {
        if (matchingWord.find(partialWord) == 0) {
            newMatchingWords.insert(matchingWord);
        }
    }
}

void Boggle::getRowColNeighbors(int rowCol, std::pair<int, int> &rowColNeighbors) {
    // inclusive first row
    rowColNeighbors.first = std::max(rowCol - 1, 0);
    // inclusive last column
    rowColNeighbors.second = std::min(rowCol + 1, static_cast<int>(puzzle.size() - 1));
}

char Boggle::puzzleChar(const Boggle::Position &position) {
    std::string row = puzzle[position.first];
    return row[position.second];
}



