class WeightedGraph:

    def __init__(self, G):
      self.adjacencyList= [x[:] for x in G]
      self.numVert = len(G)

    def dijkstra(self, s):
        import math
        import heapq

        self.distance = [math.inf for x in range(self.numVert)] # assigning infinity as distance to every vertex
        self.distance[s] = 0

        self.dist_node = []
        for i in range(self.numVert):
            self.dist_node.append((self.distance[i], i)) #distance of every node from the source vertex --> dist_node[distance of node i from source , node i]
        heapq.heapify(self.dist_node)

        #print(self.distance);
        while len(self.dist_node):
            temp, u = heapq.heappop(self.dist_node)

            if temp != self.distance[u]:
                continue

            for v, weight in self.adjacencyList[u]:
                if self.distance[u] + weight<self.distance[v]:
                    self.distance[v] = self.distance[u] + weight
                    heapq.heappush(self.dist_node, (self.distance[v], v))

def main():
    G = []
    file=open('inputw.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for edge in line.split(' '):
            if first:
                first=False
                continue
            node,weight = edge.split(',')
            adjacentVertices.append((int(node),int(weight)))
        G.append(adjacentVertices)
    file.close()

    g = WeightedGraph(G)
    g.dijkstra(0)
    print(g.distance)

if __name__ == '__main__' :
        main()