G=[]
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
def DFS(s):           
    visited = [False for i in range(len(G))]  
    stack = []   
    stack.append(s)  
    while (len(stack)):   
        s = stack[-1]
        stack.pop() 
        if (not visited[s]):  
            print(s) 
            visited[s] = True
        for i in range(len(G[s])-1,-1,-1):  
            if (not visited[G[s][i]]):  
                stack.append(G[s][i])  
s=int(input("Enter the starting edge for DFS: "))
print("Following is Depth First Traversal")  
DFS(s) 