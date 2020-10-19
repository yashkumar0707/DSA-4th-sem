from collections import deque
G=[]
file=open('input.txt','r')
for line in file:
	line=line.strip()
	adjacentVertices=[]
	first=True
	for node in line.split(' '):
		if first:
			first=False
			continue
		adjacentVertices.append(int(node))
	G.append(adjacentVertices)
file.close()
print(G)		
visited=[]
red=[]
blue=[]
queue=deque()
s=int(input('Enter source vertex'))
red.append(s)
queue.append([s,0])
visited.append(s)
while queue:
	p=queue.popleft()
	print(p[0],p[1])
	dis=p[1]+1
	for j in range(len(G[p[0]])):
		if p[0] in red and G[p[0]][j] in red:
			print("NOT BIPARTITE")
			exit()
		if p[0] in blue and G[p[0]][j] in blue:
			print("NOT BIPARTITE")
			exit()
		if G[p[0]][j] not in visited:
			queue.append([G[p[0]][j],dis])
			visited.append(G[p[0]][j])
			if p[0] in red :
				if G[p[0]][j] in blue:
					continue
				else:	
					blue.append(G[p[0]][j])
			elif p[0] in blue:
				if G[p[0]][j] in red:
					continue
				else:	
					red.append(G[p[0]][j])

print(" Bi partite")				
