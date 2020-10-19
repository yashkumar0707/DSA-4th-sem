G=[]
file=open('input.txt','r')
for line in file:
	line=line.strip()
	adjacentVertices=[]
	first =True
	for node in line.split(' '):
		if first:
			first=False
			continue
		adjacentVertices.append(int(node))
	G.append(adjacentVertices)
file.close()
print(G)
visited=[-1 for i in range (len(G))]
order=[]
tree=[]
back=[]
start=[-1 for i in range(len(G))]
finish=[-1 for i in range(len(G))]
time=0
s=int(input('Enter your source vertex'))
def dfs(s):
	global time
	visited[s]=1
	order.append(s)
	start[s]=time
	time=time+1
	for i in G[s]:
		if visited[i]==-1:
			tree.append([s,i])
			dfs(i)
	finish[s]=time
	time=time+1					
dfs(s)
print("ORDER  START  FINISH")
for i in order:
	print(order[i],"     ",start[i],"      ",finish[i])
print("tree edges are : " ,tree)
for i in range(len(G)):
	for j in G[i]:
		if [j]+[i] not in back:
			back.append([i]+[j])
for i in range(len(tree)):
	back.remove(tree[i])
for i in range(len(tree)):
	if ([tree[i][1],tree[i][0]]) in back :
		back.remove([tree[i][1],tree[i][0]])
print(back)		

	


