/**
 * Boggle puzzle game. Find words in a grid, according to the following rules: The letters must be adjoining in a
 * 'chain'. Letters in the chain may be adjacent horizontally, vertically, or diagonally. The letter position cannot be used more than once in the chain.
 * @author art@arthuston.com
 */

#ifndef BOGGLE_HPP
#define BOGGLE_HPP


#include <vector>
#include <string>
#include <list>
#include <set>

/**
 * Boggle puzzle game.
 *
 */
class Boggle {

public:
    /**
     * Constructor.
     *
     * @param puzzle the puzzle
     */
    Boggle(const std::vector<std::string> &puzzle) :
            puzzle(puzzle) {
        // empty
    }

    /**
     * Solve the puzzle.
     * Returns result by reference instead of stack for performance.
     *
     * @param words std::set of words to look for in the puzzle
     * @param foundWords the std::set of found words actually in the puzzle
    */
    void solve(const std::set<std::string> &words, std::list<std::string> &foundWords);

private:

    typedef std::pair<int, int> Position;
    typedef std::pair<int, int> IntRange;

    /**
     * Solve puzzle recursively at current position.
     * Returns result by reference instead of stack for performance.
     *
     * @param position      current position
     * @param partialWord   the partial word
     * @param matchingWords std::set of words that match so far
     * @param visited       previously visited positions
     * @param foundWords    the list of found words actually in the puzzle
     */
    void
    solvePosition(const Position &position, const std::string &partialWord, const std::set<std::string> &matchingWords,
                  std::set<Position> &visited, std::list<std::string> &foundWords);

    /**
     * Find partial word matches.
     * Returns result by reference instead of stack for performance.
     *
     * @param partialWord   partial word
     * @param matchingWords list of words that match so far
     * @param newMatchingWords std::set of words where the first len(word) characters match
     */
    void findPartialMatches(const std::string &partialWord, const std::set<std::string> &matchingWords,
                            std::set<std::string> &newMatchingWords);

    /**
     * Get neighbors and self of a row or column
     * Returns result by reference instead of stack for performance.
     *
     * @param rowCol row or column
     * @rowColNeighbors row or column neighbors and rowCol
     */
    void getRowColNeighbors(int rowCol, IntRange &rowColNeighbors);


    /**
     * Get character at position.
     * @param position the position
     * @return character at position.
     */
    char puzzleChar(const Position &position);

    std::vector<std::string> puzzle;

};


#endif //BOGGLE_BOGGLE_HPP
