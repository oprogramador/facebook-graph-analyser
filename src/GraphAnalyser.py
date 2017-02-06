def combineChainWithNeighbors(chain, neighbors):
    return map(lambda last: chain + [last], neighbors)

def findShortestPath(getNeighbours, start, end):
    if start is end:
        return [start]
    chains = combineChainWithNeighbors([start], getNeighbours(start))
    while True:
        newChains = []
        for chain in chains:
            item  = chain[-1]
            if item is end:
                return chain
            neighbors = getNeighbours(item)
            newChains += combineChainWithNeighbors(chain, neighbors)
        chains = newChains
