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
		else :
			if  start[i]!=start[s]-1 and start[i]<start[s]:
				print('cycle')	
				exit()
	finish[s]=time
	time=time+1					
dfs(s)
print("ORDER  START  FINISH")
print("Order : ",order)
print("Start times : ",start)
print("Finish times : ",finish)
print("tree edges : ",tree)
print("acyclic")





	




