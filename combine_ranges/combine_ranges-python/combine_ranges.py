#!/usr/bin/env python3
# ranges facebook interview question for python3
# ranges are a built-in type for python3 with start and stop
# NOTE: python3 ranges have an EXCLUSIVE STOP.

from copy import copy
import unittest


def intersect(r1, r2):
    """
    Check if two ranges intersect.
    Note that range.stop is exclusive.
    :param r1: the first range
    :param r2: the second range
    :return: true if the ranges intersect else false
    """
    # note that start is inclusive, and stop is exclusive
    return r1.start < r2.stop and r1.stop > r2.start


def union(r1, r2):
    """
    Get the union of two intersecting ranges
    raise AssertionError if they do not intersect
    :param r1: the first intersecting range
    :param r2: the second intersecting range
    :return: the union of the ranges
    """
    assert (intersect(r1, r2))
    return range(min(r1.start, r2.start), max(r1.stop, r2.stop))


def sorted_unions(ranges):
    """
    Combine ranges that intersect and return the combined ranges in ascending order
    total complexity O((n log n) + n) where n = len(ranges)
    :param ranges: the list of ranges
    :return: new list of ranges containing the unions of the ranges sorted in ascending order
    """
    if len(ranges) < 2:
        # no sorting, return copy
        return copy(ranges)

    # sort in ascending order by start (by end would also work)
    # O(n log n) where n = len(ranges)
    ranges.sort(key=lambda r: r.start)

    # get the unions
    # O(n) where n = len(ranges)
    current_range = ranges[0]
    unions = []
    i = 1
    while i < len(ranges):
        if intersect(current_range, ranges[i]):
            # take union and continue
            current_range = union(current_range, ranges[i])
        else:
            # emit current range and resume finding unions
            unions.append(current_range)
            current_range = ranges[i]
        i += 1
    unions.append(current_range)

    # sort the unions is not required since they are already sorted
    # total complexity O((n log n) + n) where n = len(ranges)
    return unions


class TestRanges(unittest.TestCase):
    def test_intersect(self):
        # negative tests
        # empty ranges
        self.assertFalse(intersect(range(0, 0), range(0, 1)))
        self.assertFalse(intersect(range(0, 1), range(0, 0)))
        # off by one
        self.assertFalse(intersect(range(0, 1), range(1, 1)))
        self.assertFalse(intersect(range(1, 1), range(0, 1)))
        # on by one
        self.assertTrue(intersect(range(0, 2), range(1, 3)))
        self.assertTrue(intersect(range(1, 3), range(0, 2)))

    def test_union(self):
        # test empty ranges and off by one
        with self.assertRaises(AssertionError):
            union(range(0, 0), range(0, 1))
            union(range(0, 1), range(0, 0))
            union(range(0, 1), range(1, 1))
            union(range(1, 1), range(0, 1))
        # test on by one
        self.assertEqual(range(0, 3), union(range(0, 2), range(1, 3)))
        self.assertEqual(range(0, 3), union(range(1, 3), range(0, 2)))

    def test_sorted_unions(self):
        # test empty list
        self.assertEqual([], sorted_unions([]))
        # test one item
        self.assertEqual([range(0, 1)], sorted_unions([range(0, 1)]))
        # test two items that do not intersect
        self.assertEqual([range(0, 2), range(2, 3)], sorted_unions([range(0, 2), range(2, 3)]))
        self.assertEqual([range(0, 2), range(2, 3)], sorted_unions([range(2, 3), range(0, 2)]))
        # test two items that intersect
        self.assertEqual([range(0, 3)], sorted_unions([range(0, 2), range(1, 3)]))
        self.assertEqual([range(0, 3)], sorted_unions([range(1, 3), range(0, 2)]))
        # test two items that intersect and one that doesn't
        self.assertEqual([range(0, 3), range(3, 5)], sorted_unions([range(0, 2), range(1, 3), range(3, 5)]))
        self.assertEqual([range(0, 3), range(3, 5)], sorted_unions([range(3, 5), range(1, 3), range(0, 2)]))
        # test two sets  of items that intersect
        self.assertEqual([range(0, 3), range(3, 6)],
                         sorted_unions([range(0, 2), range(1, 3), range(3, 5), range(4, 6)]))
        self.assertEqual([range(0, 3), range(3, 6)],
                         sorted_unions([range(4, 6), range(3, 5), range(1, 3), range(0, 2)]))


if __name__ == '__main__':
    unittest.main()
