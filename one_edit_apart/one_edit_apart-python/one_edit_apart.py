def one_edit_apart(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    if len(s2) - len(s1) > 1:
        return False

    i1 = 0
    i2 = 0

    found_difference = False
    while i1 < len(s1):
        if s1[i1] != s2[i2]:
            if found_difference:
                return False
            found_difference = True
            if len(s2) > len(s1):
                i1 += 1
                break
        i1 += 1
        i2 += 1

    return found_difference or len(s2) > len(s1)


def test(s1, s2):
    print('one_edit_apart(%s, %s) = %s' % (s1, s2, one_edit_apart(s1, s2)))

if __name__ == '__main__':
    test('dog', 'cat')
    test('dog', 'dog')
    test('ddog', 'dog')
    test('dogg', 'dog')
    test('doog', 'dog')
    test('dog', 'don')
    test('bog', 'dog')
