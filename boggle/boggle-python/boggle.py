"""
Boggle puzzle game. Find words in a grid, according to the following rules: The letters must be adjoining in a 'chain'.
Letters in the chain may be adjacent horizontally, vertically, or diagonally. The letter position cannot be used more
than once in the chain.

This reads the puzzle and list of words from stdin. Example usage: cat input.txt | python boggle.py
"""

import sys


class Boggle:
    """
    Boggle puzzle game.
    """
    puzzle = None

    class _Position:
        """
        Internal class to store the x-y position in the puzzle grid.
        """
        col = None
        row = None

        def __init__(self, col, row):
            """
            Constructor.
            :param row: row in the puzzle
            :param col: column in the puzzle
            y position in the grid
            """
            self.col = col
            self.row = row

        def __key__(self):
            """
            Return key to this object.
            :return: key to this object
            """
            return self.col, self.row

        def __eq__(self, other):
            """
            Test for equality.
            :param other: other position
            :return: true if the other position has the same coordinates as this position
            """
            return self.__key__() == other.__key__()

        def __ne__(self, other):
            """
            Test for inequality.
            :param other: other position
            :return: true if the other position has different coordinates as this position
            """
            return not self.__eq__(other)

        def __hash__(self):
            """
            Return hash of this object.
            :return: hash of this object
            """
            return hash(self.__key__())

    def __init__(self, puzzle):
        """
        Boggle constructor.
        :param puzzle: list of same-length strings representing the grid.
        """
        self.puzzle = puzzle
        puzzle_len = len(self.puzzle)
        for i in range(0, len(self.puzzle)):
            s = self.puzzle[i]
            if puzzle_len != len(s):
                raise ValueError('Illegal puzzle len %d instead of %d at line %d' %
                                 (len(s), puzzle_len, i))

    def solve(self, words):
        """
        Solve the puzzle.
        :param words: list of words to look for in the puzzle
        :return: list of words actually found in the puzzle
        """
        found_words = []

        # look for complete word starting at each character
        for y in range(0, len(self.puzzle)):
            for x in range(0, len(self.puzzle)):
                found_words.extend(self._solve_position(position=self._Position(x, y),
                                                        visited=set(),
                                                        partial_word="",
                                                        words=words))
        return found_words

    def _get_partial_words(self, partial_word, words):
        """
        Check partial word matches.
        :param partial_word: partial word
        :param words: list of words that match so far
        :return: list of words where the first len(word) characters match
        """
        result = set()
        for word in words:
            if partial_word == word[0:len(partial_word)]:
                result.add(word)
        return result

    def _solve_position(self, position, visited, partial_word, words):
        """
        Solve puzzle recursively at current position.
        :param position: current position
        :param visited: previously visited positions
        :param partial_word: the partial word
        :param words: list of words that match so far
        :return: list of found words
        """
        # set list of found words to empty
        # set this position to visited
        # add character to partial word
        found_words = []
        visited.add(position)
        char = self.puzzle[position.row][position.col]
        partial_word = '%s%s' % (partial_word, char)

        if partial_word in words:
            found_words.append(partial_word)

        # check partial matches
        words = self._get_partial_words(partial_word=partial_word,
                                       words=words)

        # add neighboring characters to the partial word
        if len(words) > 0:
            for row in self._get_row_col_neighbors(position.row):
                for col in self._get_row_col_neighbors(position.col):
                    next_position = self._Position(col, row)
                    if next_position not in visited:
                        found_words.extend(self._solve_position(next_position, visited, partial_word, words))

        visited.remove(position)

        return found_words

    def _get_row_col_neighbors(self, row_col):
        """
        Get neighbors around a row or column
        :param row_col: row or column
        :return: row or column and its neighbors
        """
        # inclusive start
        start = max(row_col - 1, 0)
        # exclusive limit
        limit = min(row_col + 2, len(self.puzzle))
        r = range(start, limit)
        return r


def read_puzzle():
    """
    Read puzzle from stdin.
    :return: puzzle
    """
    puzzle_size = int(sys.stdin.readline())
    puzzle = [None] * puzzle_size
    print('puzzle:')
    for row in range(0, puzzle_size):
        puzzle[row] = sys.stdin.readline().rstrip()
        if len(puzzle[row]) != puzzle_size:
            raise ValueError(f'{puzzle[row]} is the wrong length should be {puzzle_size}')
        print(puzzle[row])
    print()
    return puzzle


def read_words():
    """
    Read list of words from stdin.
    :return: list of words
    """
    word_count = int(sys.stdin.readline())
    words = [None] * word_count
    print('words:')
    for i in range(0, word_count):
        words[i] = sys.stdin.readline().rstrip()
        print(words[i])
    print()
    return words


if __name__ == '__main__':
    puzzle = read_puzzle()
    words = read_words()

    boggle = Boggle(puzzle)
    found_words = boggle.solve(words)
    print('found:')
    for found_word in found_words:
        print(found_word)

    sys.exit(0)
