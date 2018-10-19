"""
Boggle puzzle game.
Find words in a grid, according to the following rules: The letters must be adjoining in a 'chain'.
Letters in the chain may be adjacent horizontally, vertically, or diagonally. The letter position cannot be used
more than once in the chain.

This reads the puzzle and list of words from stdin. Example usage:
cat input.txt | python boggle.py

Sample input:
5
dogca
ebirt
rxxdm
gesuo
erbil
6
dog
cat
deer
bird
gerbil
mouse

The sample input will find dog in the first line, cat in lines 1-2, bird in lines 2-3, mouse in lines 3-4, and gerbil
twice on lines 4-5. deer will not be found.
"""

import sys


class Boggle:
    """
    Boggle puzzle game.
    """
    puzzle = None

    class _Position:
        """
        Internal class to store the x-y position in the puzzle grtid.
        """
        x = None
        y = None

        def __init__(self, x, y):
            """
            Constructor.
            :param x: x position in the grid
            :param y: y position in the grid
            """
            self.x = x
            self.y = y

        def __key(self):
            """
            Return key to this object.
            :return: key to this object
            """
            return self.x, self.y

        def __eq__(self, other):
            """
            Test for equality.
            :param other: other position
            :return: true if the other position has the same coordinates as this position
            """
            return self.__key() == other.__key()

        def __hash__(self):
            """
            Return hash of this object.
            :return: hash of this object
            """
            return hash(self.__key())

    def __init__(self, puzzle):
        """
        Boggle constructor.
        :param puzzle: list of same-length strings representing the grid. The number of items in the list must be the same as the length of each string.
        """
        self.puzzle = puzzle
        puzzle_len = len(self.puzzle)
        for i in range(0, len(self.puzzle)):
            str = self.puzzle[i]
            if puzzle_len != len(str):
                raise ValueError('Illegal puzzle len %d instead of %d at line %d' %
                                 (len(str), puzzle_len, i))

    def solve(self, words):
        """
        Solve the puzzle.
        :param words: list of words to lo ok for in the puzzle
        :return: list of words actually found in the puzzle
        """
        found_words = []

        # look for complete word starting at each character
        for x in range(0, len(self.puzzle)):
            for y in range(0, len(self.puzzle)):
                found_words.extend(self._solve_puzzle(position=self._Position(x, y),
                                                      visited=set(),
                                                      partial_word="",
                                                      matching_words=words))
        return found_words

    def _check_partial_word(self, partial_word, matching_words):
        """
        Check partial word matches.
        :param partial_word: partial word
        :param matching_words: list of words that match so far
        :return: list of words where the first len(word) characters match
        """
        result = set()
        for w in matching_words:
            if partial_word == w[0:len(partial_word)]:
                result.add(w)
        return result

    def _solve_puzzle(self, position, visited, partial_word, matching_words):
        """
        Solve puzzle recursively at current position.
        :param position: current position
        :param visited: previously visited positions
        :param partial_word: the partial word
        :param matching_words: list of words that match so far
        :return: list of found words
        """
        # set list of found words to empty
        # set this position to visited
        # add character to partial word
        found_words = []
        visited.add(position)
        partial_word = '%s%s' % (partial_word, self.puzzle[position.x][position.y])

        # check exact match
        if partial_word in matching_words:
            found_words.append(partial_word)

        # check partial matches
        matching_words = self._check_partial_word(partial_word=partial_word,
                                                  matching_words=matching_words)

        # add neighboring characters to the partial word
        if len(matching_words) > 0:
            for x in self._get_neighbors(position.x):
                for y in self._get_neighbors(position.y):
                    next_position = self._Position(x, y)
                    if next_position not in visited:
                        found_words.extend(self._solve_puzzle(next_position, visited, partial_word, matching_words))

        visited.remove(position)

        return found_words

    def _get_neighbors(self, x_or_y_coord):
        """
        Get neighbors around an x or y coordinate
        :param x_or_y_coord: the x or y coordinate
        :return: the x or y range of neighbors
        """
        # first x or y to consider
        start = max(x_or_y_coord - 1, 0)
        # last + 1 x or y to consider
        stop = min(x_or_y_coord + 2, len(self.puzzle))
        r = range(start, stop)
        return r


def read_puzzle():
    """
    Read puzzle from stdin.
    :return: puzzle
    """
    puzzle_size = int(sys.stdin.readline())
    puzzle = [None] * puzzle_size
    print('puzzle:')
    for i in range(0, puzzle_size):
        puzzle[i] = sys.stdin.readline().rstrip()
        if len(puzzle[i]) != puzzle_size:
            raise ValueError(f'{puzzle[i]} is the wrong length should be {puzzle_size}')
        print(puzzle[i])
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
