import GraphAnalyser
import FacebookConnector
import sys

print GraphAnalyser.findShortestPath(FacebookConnector.getFriends, sys.argv[1], sys.argv[2])
