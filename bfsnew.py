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
queue=deque()
s=int(input('Enter source vertex'))
queue.append([s,0])
visited.append(s)
while queue:
	p=queue.popleft()
	print(p[0],p[1])
	dis=p[1]+1
	for j in range(len(G[p[0]])):
		if G[p[0]][j] not in visited:
			queue.append([G[p[0]][j],dis])
			visited.append(G[p[0]][j])