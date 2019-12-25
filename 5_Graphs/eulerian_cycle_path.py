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
    def has_eulerian_cycle(adj_list):
        odd = 0
        for node in adj_list:
            if len(adj_list[node]) % 2 != 0:
                odd += 1
        return odd == 0

    @staticmethod
    def has_eulerian_path(adj_list):
        odd = 0
        for node in adj_list:
            if len(adj_list[node]) % 2 != 0:
                odd += 1
        if odd == 0 or odd == 2:
            return True
        return False


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        edges_1 = [[1, 5], [1, 2], [1, 4], [1, 3], [5, 2], [2, 3], [2, 4], [3, 4], [3, 6], [4, 6]]
        self.a_list_with_cycle = self.solution.create_adj_list(edges_1)

        edges_2 = [[1, 5], [1, 2], [1, 4], [1, 3], [5, 2], [2, 3], [2, 4], [3, 4]]
        self.a_list_with_path = self.solution.create_adj_list(edges_2)

        edges_3 = [[1, 2], [1, 4], [1, 3], [2, 3], [2, 4], [3, 4]]
        self.a_list_with_no_cycle_or_path = self.solution.create_adj_list(edges_3)

    def test_has_eulerian_cycle(self):
        self.assertTrue(self.solution.has_eulerian_cycle(self.a_list_with_cycle))
        self.assertFalse(self.solution.has_eulerian_cycle(self.a_list_with_path))
        self.assertFalse(self.solution.has_eulerian_cycle(self.a_list_with_no_cycle_or_path))

    def test_has_eulerian_path(self):
        self.assertTrue(self.solution.has_eulerian_path(self.a_list_with_cycle))
        self.assertTrue(self.solution.has_eulerian_path(self.a_list_with_path))
        self.assertFalse(self.solution.has_eulerian_path(self.a_list_with_no_cycle_or_path))

    # def tearDown(self):
    #     self.solution.dispose()


if __name__ == '__main__':
    unittest.main()
