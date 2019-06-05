"""
Find first consecutive values in a list that total to a specified sum.
Example:
    Given input [1, 2, 3, 4] and 1, return [1]
    Given input [1, 2, 3, 4] and 3, return [1, 2]
    Given input [1, 2, 3, 4] and 5, return [2, 3]
    Given input [1, 2, 3, 4] and 7, return [3, 4]
    Given input [1, 2, 3, 4] and 4, return [4]
    Given input [1, 2, 3, 4] and 11, return None
"""


def find_sum_in_list(lst, sm):
    """
    Find first consecutive values in a list that total to a sum.
    Algorithm: use a totals dictionary to store running total and running position as key-value pairs.
    If the difference of a calculated running total and the desired sum is already in totals,
    then return the sub-list starting at the stored running position and ending at the current position.
    :param lst: the list to examine
    :param sm: the sum to match
    :return: the range that totals to the sum, or None if not found
    """

    # keep and store running totals
    total = 0
    totals = {total: -1}
    for i in range(0, len(lst)):
        total += lst[i]
        diff = total - sm

        # find running total that equals the difference
        if diff in totals:
            # remove the sub list containing the difference
            # and return the resulting sub-list
            return range(totals[diff] + 1, i + 1)

        # store the running total
        totals[total] = i

    return None


def demo(lst, sm):
    rng = find_sum_in_list(lst, sm)
    print("find_sum_in_list(%s, %s) = %s" % (lst, sm, rng))
    if rng is not None:
        for value in lst[rng.start:rng.stop]:
            sm -= value
        assert (sm == 0)
    # TODO test this is the first occurrence of the sum
    # TODO test when result is None


if __name__ == '__main__':
    demo([], 0)
    demo([1], 5)
    demo([5], 5)
    demo([1, 5], 5)
    demo([1, 2, 3], 5)
    demo([1, 2, 3, 5], 5)
    demo([1, 2, 4, 5], 5)
