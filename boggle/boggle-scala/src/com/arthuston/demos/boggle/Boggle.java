/**
 * Boggle puzzle game. Find words in a grid, according to the following rules: The letters must be adjoining in a
 * 'chain'. Letters in the chain may be adjacent horizontally, vertically, or diagonally. The letter position cannot be used more than once in the chain.
 */

package com.arthuston.demos.boggle;

import javafx.util.Pair;
import org.apache.commons.lang3.Range;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

import static java.lang.Math.max;
import static java.lang.Math.min;

/**
 * Boggle puzzle game.
 */
public class Boggle {

    private final String[] puzzle;

    /**
     * Constructor.
     *
     * @param puzzle the puzzle
     */
    public Boggle(String[] puzzle) {
        this.puzzle = puzzle;
        // for high-performance these checks would be removed
        for (String row : puzzle) {
            if (row.length() != this.puzzle.length) {
                throw new IllegalArgumentException(String.format("%s is the wrong length, expected %d",
                        row, this.puzzle.length));
            }
        }
    }

    /**
     * Solve the puzzle.
     *
     * @param words set of words to look for in the puzzle
     * @return list of words actually found in the puzzle
     */
    public List<String> solve(Set<String> words) {
        List<String> foundWords = new LinkedList<>();

        // look for complete word starting at each character
        for (int row = 0; row < puzzle.length; row++) {
            for (int col = 0; col < puzzle.length; col++) {
                // find words at current position
                Pair<Integer, Integer> position = position(row, col);
                Set<Pair<Integer, Integer>> visited = new HashSet<>();
                String partialWord = "";
                List<String> newFoundWords = solvePosition(position, visited, partialWord, words);

                // add new found words to list
                foundWords.addAll(newFoundWords);
            }
        }

        return foundWords;
    }


    /**
     * Solve puzzle recursively at current position.
     *
     * @param position      current position
     * @param visited       previously visited positions
     * @param partialWord   the partial word
     * @param words list of words that match so far
     * @return list of found words
     */
    private List<String> solvePosition(Pair<Integer, Integer> position,
                                       Set<Pair<Integer, Integer>> visited,
                                       String partialWord,
                                       Set<String> words) {
        // list of found words is empty,
        // set this position to visited,
        // and add character to partial word
        List<String> foundWords = new LinkedList<>();
        visited.add(position);
        char ch = puzzleChar(position);
        String newPartialWord = new StringBuilder(partialWord).append(ch).toString();

        // check partial words
        words = getPartialWords(newPartialWord, words);
        if (words.contains(newPartialWord)) {
            // check exact match
            foundWords.add(newPartialWord);
            words.remove(newPartialWord);
        }


        if (words.size() > 0) {

            // search neighboring characters
            Range<Integer> rowNeighbors = getRowColNeighbors(row(position));
            Range<Integer> collNeighbors = getRowColNeighbors(col(position));
            for (int row = rowNeighbors.getMinimum(); row <= rowNeighbors.getMaximum(); row++) {
                for (int col = collNeighbors.getMinimum(); col <= collNeighbors.getMaximum(); col++) {
                    Pair nextPosition = position(row, col);
                    if (!visited.contains(nextPosition)) {
                        List<String> newFoundWords = solvePosition(nextPosition,
                                visited, newPartialWord, words);
                        foundWords.addAll(newFoundWords);
                    }
                }
            }
        }

        visited.remove(position);
        return foundWords;
    }

    /**
     * Find partial word matches.
     *
     * @param partialWord   partial word
     * @param matchingWords list of words that match so far
     * @return set of words where the first len(word) characters match
     */
    private Set<String> getPartialWords(String partialWord, Set<String> matchingWords) {
        Set<String> newMatchingWords = new HashSet<String>();
        for (String matchingWord : matchingWords) {
            if (matchingWord.startsWith(partialWord)) {
                newMatchingWords.add(matchingWord);
            }
        }
        return newMatchingWords;
    }

    /**
     * Get neighbors and self of a row or column
     *
     * @param rowCol row or column
     * @return range row or column neighbors
     */
    private Range<Integer> getRowColNeighbors(int rowCol) {
        // inclusive first row
        int start = max(rowCol - 1, 0);
        // inclusive last column
        int stop = min(rowCol + 1, puzzle.length - 1);

        return Range.between(start, stop);
    }

    // helper methods that allow us to use Pair as Position
    Pair<Integer, Integer> position(int row, int col) {
        return new Pair<>(row, col);
    }

    int row(Pair<Integer, Integer> position) {
        return position.getKey();
    }

    int col(Pair<Integer, Integer> position) {
        return position.getValue();
    }

    char puzzleChar(Pair<Integer, Integer> position) {
        String row = puzzle[row(position)];
        return row.charAt(col(position));
    }


}


