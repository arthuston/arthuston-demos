/**
 * Run boggle using standard input.
 * @author art@arthuston.com
 */

#include <istream>
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <list>
#include "Boggle.hpp"

std::istream& operator>>(std::istream&, std::vector<std::string>&);
std::istream& operator>>(std::istream&, std::set<std::string>&);

int main(int argc, char** argv) {
    if (argc != 2) {;
        std::cerr << "Usage: Main <input-file>" << std::endl;
        exit(1);
    }

    // read puzzle and words
    std::vector<std::string> puzzle;
    std::set<std::string> words;
    std::ifstream in;

    in.open(argv[1]);
    in >> puzzle;
    in >> words;

    // solve boggle
    Boggle boggle(puzzle);
    std::list<std::string> foundWords;
    boggle.solve(words, foundWords);

    std::cout << "Found:" << std::endl;
    for (std::string foundWord : foundWords) {
        std::cout << foundWord << std::endl;
    }

    exit(0);
}

std::istream& operator>>(std::istream& is, std::vector<std::string>& puzzle) {
    std::cout << "Puzzle:" << std::endl;

    int puzzleSize;
    std::string s;
    puzzle.clear();

    is >> puzzleSize;
    puzzle.reserve(puzzleSize);

    for (int i = 0; i < puzzleSize; i++) {
        is >> s;
        if (s.size() != puzzleSize) {
            throw std::invalid_argument(s + " is the wrong length");
        }
        std::cout << s << std::endl;
        puzzle.push_back(s);
    }

    std::cout << std::endl;
    return is;
}

std::istream& operator>>(std::istream& is, std::set<std::string>& words) {
    std::cout << "Words:" << std::endl;

    int wordCount;
    std::string s;
    words.clear();

    is >> wordCount;

    for (int i = 0; i < wordCount; i++) {
        is >> s;
        words.insert(s);
        std::cout << s << std::endl;
    }

    std::cout << std::endl;
    return is;
}



