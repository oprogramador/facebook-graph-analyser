import unittest
import GraphAnalyser

class GraphAnalyserTest(unittest.TestCase):

    def test_findShortestPath_returns_zero_for_neighbors(self):
        a = 'a'
        getNeighbours = lambda x: []
        result = GraphAnalyser.findShortestPath(getNeighbours, a, a)
        self.assertEqual(result, 0)

    def test_findShortestPath_returns_one_for_neighbors(self):
        a = 'a'
        b = 'b'
        connections = {
          a: [b],
        }
        getNeighbours = lambda x: connections[x]
        result = GraphAnalyser.findShortestPath(getNeighbours, a, b)
        self.assertEqual(result, 1)

    @unittest.skip('')
    def test_findShortestPath_returns_two_for_second_level_neighbors(self):
        a = 'a'
        b = 'b'
        c = 'c'
        connections = {
          a: [b],
          b: [c],
        }
        getNeighbours = lambda x: connections[x]
        result = GraphAnalyser.findShortestPath(getNeighbours, a, c)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
