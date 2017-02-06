def combineChainWithNeighbors(chain, neighbors):
    neighborsWithoutRepetitions = list(set(neighbors) - set(chain))
    return map(lambda last: chain + [last], neighborsWithoutRepetitions)

def findShortestPath(getNeighbours, start, end):
    if start == end:
        return [start]
    chains = combineChainWithNeighbors([start], getNeighbours(start))
    while True:
        newChains = []
        isAnyNeighbor = False
        for chain in chains:
            item  = chain[-1]
            if item == end:
                return chain
            neighbors = getNeighbours(item)
            if len(neighbors) > 0:
                isAnyNeighbor = True
            newChains += combineChainWithNeighbors(chain, neighbors)
        if not isAnyNeighbor:
            return None
        chains = newChains
