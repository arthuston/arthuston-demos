/**
 * Double Linked List with constant time insertion and removal.
 */

#ifndef DOUBLE_LINKED_LIST_HPP
#define DOUBLE_LINKED_LIST_HPP

/**
 * Linked List with constant time insertion and removal.
 */
public template class <T> DoubleLinkedList {

        public:
        /**
         * Node in the double linked list.
         */
        class Node {
            public:
            Node(Node * prev = NULL, NODE * nxt = NULL, T
            value = NULL): prev(prev), nxt(nxt), value(value)
            {
                // empty
            }
            private:
            Node *prev;
            Node *nxt;
            T value;
        }

        DoubleLinkedList() {
            front = Node();
            back = Node(front);
            front.nxt = back;
        }
}
/**






    private:

    }

    };

        class Node {
            public Node(

                    *
                            prev = NULL, Node
                                         *
                                         next = NULL, T
            value = NULL
            ):

prev (prev), nxt(nxt), value(value) {
    // empty
}
};

def __init__(self, prev, nxt, value=None):
self.prev = prev
self.nxt = nxt
self.key = key

def __str__(self):
return str(self.key)



def __init__(self):
        self.front = LinkedNode(None, None)
        self.back = LinkedNode(self.front, None)
        self.front.nxt = self.back

    def push(self, key):
        node = LinkedNode(self.back.prev, self.back, key)
        self.back.prev.nxt = node
        self.back.prev = node
        return node

    def move_to_end(self, node):
        self._remove(node)
        return self.push(node.key)

    def pop(self):
        node = self.front.nxt
        self._remove(self.front.nxt)
        return node

    def _remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def __str__(self):
        sep = ''
        s = 'lru: ['
        node = self.front.nxt
        while node != self.back:
            s += sep
            sep = ', '
            s += str(node.key)
            node = node.nxt
        s += ']'
        return s


class LRUCache:
    """
    Least recently used cache.
    """

    cache = {}
    used = LinkedList()

    def __init__(self, max_size):
        self.max_size = max_size

    def get(self, key):
        if key in self.cache:
            self.cache[key]['used'] = self.used.move_to_end(self.cache[key]['used'])
            return self.cache[key]['value']
        return None

    def put(self, key, value):
        if key in self.cache:
            # move used to now and set new value
            used = self.used.move_to_end(self.cache[key]['used'])
            self.cache[key] = {'value': value, 'used': used}
        else:
            if len(self.cache) == self.max_size:
                # remove lru
                used = self.used.pop()
                del self.cache[used.key]
            # add new key
            used = self.used.push(key)
            self.cache[key] = {'value': value, 'used': used}

    def __str__(self):
        s = 'cache: {'
        sep = ''
        for k, v in self.cache.items():
            s += sep
            sep = ', '
            s += '%d: ' % k
            s += ''
            s += str(v['value'])
        s += '}, '
        s += str(self.used)
        return s


if __name__ == '__main__':
    test_data = [6, 16, 5, 21, 24, 4, 3, 17, 20, 12]
    print('test_data: %s' % str(test_data))
    limit = 5
    cache = LRUCache(limit)

    print("adding values")
    for i in range(0, len(test_data)):
        cache.put(i, test_data[i])
        print('put %d %d %s' % (i, test_data[i], str(cache)))

    print("updating values")
    for i in range(5, len(test_data)):
        cache.put(i, test_data[i] + 1)
        print('put %d %d %s' % (i, test_data[i] + 1, str(cache)))

    print("getting values")
    for i in range(0, len(test_data)):
        result = str(cache.get(i))
        print('get %d = %s %s' % (i, result, str(cache)))

    print("done")
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
     * @param visited       previously visited positions
     * @param partialWord   the partial word
     * @param matchingWords std::set of words that match so far
     * @param foundWords    the list of found words actually in the puzzle
     */
    void solvePosition(const Position &position,
                       std::set<Position> &visited,
                       const std::string &partialWord,
                       const std::set<std::string> &matchingWords,
                       std::list<std::string> &foundWords);

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



**/
#endif //DOUBLE_LINKED_LIST_HPP
