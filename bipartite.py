from collections import deque
G = [] 

file=open('input.txt','r')
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

print(G)

visited = []
red = []
blue = []
queue = deque()
s=int(input("enter source"))
queue.append([s,0])
red.append(s)
visited.append(s)
while queue:
	p = queue.popleft()
	curr = p[0]
	dis = p[1]
	print(curr,dis)
	dis = dis + 1
	for j in range(len(G[curr])):
		if curr in red and G[curr][j] in red:
			print("Condition 1")
			print("red : ",red)
			print("blue : ",blue)
			print("Not Bipartite")
			exit()
		elif curr in blue and G[curr][j] in blue:
			print("Condition 2")
			print("red : ",red)
			print("blue : ",blue)
			print("Not Bipartite")
			exit()
		elif G[curr][j] not in visited:
			queue.append([G[curr][j],dis])
			visited.append(G[curr][j])
			if curr in red:
				print("Condition 3")
				if G[curr][j] in blue:
					continue
				else:
					blue.append(G[curr][j])
			elif curr in blue:
				print("Condition 4")
				if G[curr][j] in red:
					continue
				else:
					red.append(G[curr][j])





print("red : ",red)
print("blue : ",blue)

print("Bipartite")