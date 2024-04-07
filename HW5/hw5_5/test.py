from graph import *
import unittest

class TestIsCycle(unittest.TestCase):

    def setUp(self):
        self.graph1 = Graph({0: [1, 2], 1: [3], 2: [4], 3: [], 4: []})
        self.graph2 = Graph({0: [1], 1: [2, 3], 2: [], 3: []})
        self.graph3 = Graph({0: [1], 1: [2], 2: [3], 3: []})
        self.graph4 = Graph({0: [1], 1: [2], 2: [3], 3: [0]})

    def test_is_cycle_true(self):
        self.assertTrue(self.graph4.is_cycle())

    def test_is_cycle_false(self):
        self.assertFalse(self.graph2.is_cycle())

    def test_is_cycle_empty_graph(self):
        empty_graph = Graph({})
        self.assertFalse(empty_graph.is_cycle())

    def test_is_cycle_single_node(self):
        single_node_graph = Graph({0: []})
        self.assertFalse(single_node_graph.is_cycle())

    def test_is_cycle_disconnected_graph(self):
        disconnected_graph = Graph({0: [1], 1: [2, 3], 2: [], 3: []})
        self.assertFalse(disconnected_graph.is_cycle())

if __name__ == '__main__':
    unittest.main()
