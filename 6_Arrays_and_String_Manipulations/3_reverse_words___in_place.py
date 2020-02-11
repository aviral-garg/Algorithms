import unittest


def reverse_words(message):
    # Decode the message by reversing the words
    n = len(message)
    i, j = 0, n - 1

    while i < j:
        message[i], message[j] = message[j], message[i]
        i += 1
        j -= 1

    i = 0
    s = 0
    while i < n:
        while i < n and message[i] != " ":
            i += 1
        p1, p2 = s, i - 1
        while p1 < p2:
            message[p1], message[p2] = message[p2], message[p1]
            p1 += 1
            p2 -= 1
        s = i + 1
        i += 1


# Tests


class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
