class Graph:
	def __init__(self,G):
		self.adjlist = [x[:] for x in G]
		self.numvert = len(G)

	def calcRev(self):
		self.revadjlist = [[] for x in range(self.numvert)]
		for u in range(self.numvert):
			for v in self.adjlist[u]:
				self.revadjlist[v].append(u)

	def revDFSrec(self,s):
		self.revVisited[s] = True

		for v in self.revadjlist[s]:
			if not self.revVisited[v]:
				self.revDFSrec(v)

		self.stack.append(s)

	def revDFS(self):
		self.revVisited = [False for x in range(self.numvert)]
		self.calcRev()

		for s in range(self.numvert):
			if not self.revVisited[s]:
				self.revDFSrec(s)

	def DFSscc(self,s,count):
		self.visited[s] = True
		self.comp[s] = count

		for v in self.adjlist[s]:
			if not self.visited[v]:
				self.DFSscc(v,count)

	def countSCC(self):
		self.visited = [False for x in range(self.numvert)]
		self.stack = []
		self.revDFS()
		self.comp = [-1 for x in range(self.numvert)]
		count = 0

		for vert in self.stack[::-1]:
			if not self.visited[vert]:
				self.DFSscc(vert,count)
				count += 1

		print(count)


def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 
    file=open('input1.txt')   
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for node in line.split(' '):
            if first:
                first=False
                continue
            adjacentVertices.append(int(node))
        G.append(adjacentVertices)
    file.close()


    graph = Graph(G)
    graph.countSCC()

if __name__ == '__main__':
    main()