# https://www.chegg.com/homework-help/questions-and-answers/amazon-wants-improve-audible-experience-customers-offering-better-book-recommendations-bas-q39657786
# https://www.chegg.com/homework-help/questions-and-answers/amazon-following-information-identify-user-s-interest-s-name-user-mapped-collection-books--q39657727
# Similar question on LeetCode: https://leetcode.com/discuss/interview-question/373006

import collections
from collections import defaultdict


def initialize():
    userBooks = {
        "Aba": ["shining", "carrie", "pride"],  # horror 2 romance 1
        "Ben": ["wuthering", "1984", "shining"],
        "Catherine": ["carrie", "1984"]  # horror 1 fiction 1
    }
    bookGenres = {
        "Horror": ["shining", "carrie"],
        "Fiction": ["1984"],
        "Romance": ["pride", "wuthering"],
    }
    return userBooks, bookGenres

# count = {
#     horror: 2
#     fiction: 0
#     romance: 0
# }

# TIme: O(ubg)

# Space: O(bg) auxilary + O(ug) res
# Time: O(gb + ub)


def favGenres(numBooks, userBooks, numGenres, bookGenres):
    res = {}
    genreBooks = {}
    if genre is None:
        continue
    for book in bookGenres[genre]:
        genreBooks[book] = genre

    for user in userBooks:
        books = userBooks[user]
        if books is None:
            continue
        count = {}

        for genre in bookGenres:
            for book in books:
                genre = genreBooks[book]

                count[genre] = count.get(genre, 0) + 1

        res[user] = [g for g in count if count[g] == max(count.values())]
    return res


if __name__ == '__main__':
    userBooks, bookGenres = initialize()
    print(favGenres(len(userBooks), userBooks, len(bookGenres), bookGenres))


# import unittest
# import collections
# from collections import defaultdict


# class Solution:
#     def gfg(self, nU, u2b, nG, g2b):
#         res = defaultdict(list)
#         b2g = defaultdict(str)

#         for genre in g2b:
#             books = g2b[genre]
#             for book in books:
#                 b2g[book] = genre

#         for user in u2b:
#             books = u2b[user]
#             if books is None:
#                 continue
#             count = defaultdict(int)
#             for book in books:
#                 count[b2g[book]] += 1
#             res[user] = [g for g in count if count[g] == max(count.values())]
#         return res

#         # res = collections.defaultdict(list)
#         # for user in u2b:
#         #     books = u2b[user]
#         #     if not books:
#         #         continue
#         #     count = collections.defaultdict(int)
#         #     for book in books:
#         #         for genre in g2b:
#         #             if book in g2b[genre]:
#         #                 count[genre] += 1
#         #     res[user] = [g for g in count if count[g] == max(count.values())]
#         # return res


# class TestFavGenre(unittest.TestCase):
#     def setUp(self):
#         self.obj = Solution()

#     def test_3_users_3_genres(self):
#         u2b_ = {
#             "abe": ["shining", "carrie"],
#             "bella": ["war", "happy"],
#             "catherine": ["shining"]
#         }
#         g2b = {
#             "horror": ["shining", "carrie"],
#             "fiction": ["war"],
#             "comedy": ["happy"]
#         }
#         result = defaultdict()
#         result["abe"] = ["horror"]
#         result["bella"] = ["fiction", "comedy"]
#         result["catherine"] = ["horror"]

#         self.assertDictEqual(self.obj.gfg(3, u2b_, 3, g2b), result)


# if __name__ == "__main__":
#     unittest.main()


# class Solution:
#     def f(self, numU, u2b, nG, g2b):
#         # res = defaultdict(list)
#         # for user in u2b:
#         #     books = u2b[user]
#         #     count = defaultdict(int)
#         #     if not books:
#         #         continue
#         #     for book in books:
#         #         for genre in g2b:
#         #             if book in g2b[genre]:
#         #                 count[genre] += 1
#         #     res[user] = ([g for g in count if count[g] == max(count.values())])
#         # return res
#         # res = defaultdict(list)
#         # b2g = defaultdict(str)
#         #
#         # for genre in g2b:
#         #     for book in g2b[genre]:
#         #         b2g[book] = genre
#         #
#         # for user in u2b:
#         #     books = u2b[user]
#         #     count = defaultdict(int)
#         #
#         #     if not books:
#         #         continue
#         #
#         #     for book in books:
#         #         genre = b2g[book].lower()
#         #         count[genre] += 1
#         #     res[user] = [g for g in count if count[g] == max(count.values())]
#         # return res

#         # res = collections.defaultdict(list)
#         # for user in u2b:
#         #     books = u2b[user]
#         #     if not books:
#         #         continue
#         #     count = collections.defaultdict(int)
#         #     for book in books:
#         #         for genre in g2b:
#         #             if book in g2b[genre]:
#         #                 count[genre] += 1
#         #     res[user] = [g for g in count if count[g] == max(count.values())]
#         # return res

#         res = defaultdict(list)
#         b2g = defaultdict(str)

#         for genre in g2b:
#             books = g2b[genre]
#             for book in books:
#                 b2g[book] = genre

#         for user in u2b:
#             books = u2b[user]
#             if books is None:
#                 continue
#             count = defaultdict(int)
#             for book in books:
#                 count[b2g[book]] += 1
#             res[user] = [g for g in count if count[g] == max(count.values())]
#         return res


# class Testf(unittest.TestCase):
#     def setUp(self) -> None:
#         self.object = Solution()

#     def test_3_users_3_books(self):
#         u2b = {
#             "abe": ["shining", "carrie", "happy"],
#             "bella": ["war"],
#             "catherine": ["war", "carrie", "happy"]
#         }

#         g2b = {
#             "horror": ["shining", "carrie"],
#             "comedy": ["happy"],
#             "fiction": ["war"]
#         }
#         expected = defaultdict(list)
#         expected["abe"] = ["horror"]
#         expected["bella"] = ["fiction"]
#         expected["catherine"] = ["fiction", "comedy", "horror"]

#         actual = self.object.f(len(u2b), u2b, len(g2b), g2b)

#         for user in expected:
#             if expected[user]:
#                 self.assertListEqual(
#                     sorted(expected[user]), sorted(actual[user]))


# if __name__ == "__main__":
#     unittest.main()


# class Solution:
#     def f(self, nU, u2b, nG, g2b):
#         res = defaultdict[list]
#         for user in u2b:
#             books = u2b[user]
#             count = defaultdict(int)
#             for book in books:
#                 if not books:
#                     continue
#                 for genre in g2b:
#                     if book in g2b[genre]:
#                         count[genre] += 1
#             res[user] = [g for g in count if count[g] == max(count.values())]
#         return res


# class TestF(unittest.TestCase):
#     def setUp(self):
#         self.object = Solution()

#     def test_3_users_3_genres(self):
#         u2b = {
#             "abe": [""]
#         }


# if __name__ == '__main__':
#     unittest.main()


# def u2g(self, ub, gb):
#     res = defaultdict(list)

#     for user in users:
#         books = ub[user]

#         count = collections.defaultdict(int)

#         for book in books:

#             for genre in gb:

#                 if book in gb[genre]:
#                     count[genre] += 1

#         res[user] = [g for g in genres if count[genre] == max(count.values())]
#     return res
