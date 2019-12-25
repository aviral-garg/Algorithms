import unittest
from collections import defaultdict


class Solution:

    # setup
    @staticmethod
    def create_adj_list(edges):
        adj_list = defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        return adj_list

    @staticmethod
    def search(adj_list, target):
        visited = [-1] * (len(adj_list) + 1)
        for node in adj_list:
            print(visited)
            if visited[node] == -1:
                print(node)
                visited[node] = 1
                if node == target:
                    return True

        return False


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        edges_1 = [[1, 5], [1, 2], [1, 4], [1, 3], [5, 2], [2, 3], [2, 4], [3, 4], [3, 6], [4, 6]]
        self.a_list_1 = self.solution.create_adj_list(edges_1)

        edges_2 = [[1, 5], [1, 2], [1, 4], [1, 3], [5, 2], [2, 3], [2, 4], [3, 4]]
        self.a_list_2 = self.solution.create_adj_list(edges_2)

        edges_3 = [[1, 2], [1, 4], [1, 3], [2, 3], [2, 4], [3, 4]]
        self.a_list_3 = self.solution.create_adj_list(edges_3)

    def test_search(self):
        self.assertTrue(self.solution.search(self.a_list_1, 1))
        self.assertTrue(self.solution.search(self.a_list_1, 2))
        self.assertTrue(self.solution.search(self.a_list_1, 3))
        self.assertTrue(self.solution.search(self.a_list_1, 4))
        self.assertTrue(self.solution.search(self.a_list_1, 5))
        self.assertTrue(self.solution.search(self.a_list_1, 6))
        self.assertFalse(self.solution.search(self.a_list_1, 7))
        self.assertFalse(self.solution.search(self.a_list_1, 0))

    # def tearDown(self):
    #     self.solution.dispose()


if __name__ == '__main__':
    unittest.main()
