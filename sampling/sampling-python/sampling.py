#!/usr/bin/env python3

from random import Random

data = [2, 4, 11, 7, 6, 24, 18, 15, 5, 20]


def sample(data, k):
    """
    Take a random sampling of k items in in-memory list of data.
    :param data: in memory list of data
    :param k: number of items to sample
    :return: list of k sampled items
    """

    # create random number generator
    r = Random()
    r.seed()

    # load all n items into dictionary
    n = len(data)
    data_dict = {i: data[i] for i in range(n)}
    samples = []

    for i in range(k):
        # select random item
        rand_i = r.randrange(0, n - 1) if n > 1 else 0  # randrange fails if start==stop
        samples.append(data_dict[rand_i])

        # replace selected item with last item and decrement number of items
        # to prevent duplicates
        data_dict[rand_i] = data_dict[n - 1]
        n -= 1

    return samples


def stream_sample(generator, k):
    """
    Take a random sampling of k items from a stream of data
    :param generator: generator returning a stream of data
    :param k: number of items to sample
    :return: list of k sampled items
    """

    # store first k items in dict
    samples = {}
    try:
        # take first k items
        while len(samples) < k:
            value = generator.__next__()
            samples[len(samples)] = value

        # take remaining item at probability k / number of items
        if k > 0:
            r = Random()
            r.seed()
            num_items = k
            while True:
                value = generator.__next__()
                replace = r.randrange(0, num_items)
                if replace < k:
                    # replace existing item in dict
                    samples[replace] = value
                num_items += 1

    except StopIteration:
        # end of stream
        pass

    return samples.values()


def stream_generator():
    for i in range(0, len(data)):
        yield data[i]


if __name__ == '__main__':

    print('data = %s' % data)
    for k in range(0, len(data) + 1):
        print('sample(data, %d) = %s' % (k, sample(data, k)))
    for k in range(0, len(data) + 1):
        print('stream_sample(data, %d) = %s' % (k, stream_sample(stream_generator(), k)))
