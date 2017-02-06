import unittest
import GraphAnalyser

class GraphAnalyserTest(unittest.TestCase):

    def test_combineChainWithNeighbors_combines(self):
        chain = ['a', 'b']
        neighbors = ['c', 'd']
        result = GraphAnalyser.combineChainWithNeighbors(chain, neighbors)
        self.assertEqual(result, [['a', 'b', 'c'], ['a', 'b', 'd']])

    def test_combineChainWithNeighbors_omits_repeated_items(self):
        chain = ['a', 'b']
        neighbors = ['b', 'c', 'd']
        result = GraphAnalyser.combineChainWithNeighbors(chain, neighbors)
        self.assertEqual(result, [['a', 'b', 'c'], ['a', 'b', 'd']])

    def test_findShortestPath_returns_none_when_there_is_no_path(self):
        a = 'a'
        b = 'b'
        connections = {
          b: [a],
        }
        getNeighbours = lambda x: []
        result = GraphAnalyser.findShortestPath(getNeighbours, a, b)
        self.assertEqual(result, None)

    def test_findShortestPath_works_for_same_item(self):
        a = 'a'
        getNeighbours = lambda x: []
        result = GraphAnalyser.findShortestPath(getNeighbours, a, a)
        self.assertEqual(result, ['a'])

    def test_findShortestPath_works_for_neighbors(self):
        a = 'a'
        b = 'b'
        connections = {
          a: [b],
        }
        getNeighbours = lambda x: connections[x]
        result = GraphAnalyser.findShortestPath(getNeighbours, a, b)
        self.assertEqual(result, ['a', 'b'])

    def test_findShortestPath_works_for_second_level_neighbors(self):
        a = 'a'
        b = 'b'
        c = 'c'
        connections = {
          a: [b],
          b: [c],
        }
        getNeighbours = lambda x: connections[x]
        result = GraphAnalyser.findShortestPath(getNeighbours, a, c)
        self.assertEqual(result, ['a', 'b', 'c'])

    def test_findShortestPath_works_for_third_level_neighbors(self):
        a = 'a'
        b = 'b'
        c = 'c'
        d = 'd'
        connections = {
          a: [b],
          b: [c],
          c: [d],
        }
        getNeighbours = lambda x: connections[x]
        result = GraphAnalyser.findShortestPath(getNeighbours, a, d)
        self.assertEqual(result, ['a', 'b', 'c', 'd'])

if __name__ == '__main__':
    unittest.main()
