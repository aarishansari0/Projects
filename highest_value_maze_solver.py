

#start values
d=[[1,9,1],[1,4,5],[5,1,2]]
ans=d[0][0]
i,j=0,0
x,y=i,j
temp= []
visited=[]
nodes=[]
dic_nodes={
}

# check if the box is present
def box_present(h,w):
	if h<len(d) and h>=0 and w<len(d[x]) and w>=0 and [h,w] not in visited:
		return True
	else:
		return False	

#Go back to the last node
def last_node():
	for index in range(len(dic_nodes)):
		temp=(dic_nodes[str(nodes[-index])])
		print()
		for a in temp:
			if a not in visited:
				nodes.remove(a)
				dic_nodes[str(nodes[-index])].remove(a)
				return d[a[0]][a[1]], a
	

#add a node to the list + dic
def add_node(a):
	nodes.append(a)
	if str(a) in dic_nodes:
		temp=dic_nodes[str(a)]
		
		temp.append(a)

		dic_nodes[str(a)]=temp
	else:
		dic_nodes[str(a)]=[a]


	
# get valid adj boxes
def adj():
	max=-10000
	best_adj= []
	count=0
	x,y=i,j
	adj_present=False
	adjacents=[]
	
	def is_present(a,b):
		nonlocal max, count, best_adj, adjacents,adj_present
		if box_present(a,b) and d[a][b]>max:
			best_adj=[a,b]
			max=d[a][b]
			count+=1
			adjacents.append([a,b])
			adj_present=True
			return True
		else:
			return False
	
	x+=1
	if is_present(x,y):
		is_present(x,y)	
	
	x-=2
	if is_present(x,y):
		is_present(x,y)
	
	x+=1
	y+=1
	if is_present(x,y):
		is_present(x,y)
	
	y-=2
	if is_present(x,y):
		is_present(x,y)
	
	y+=1
	
		
	if count>1:
		temp=adjacents
		temp.remove(best_adj)
		for var in temp:
			add_node(var)
	if adj_present== False:
		max, best_adj = last_node()	
	visited.append(best_adj)
	return max, best_adj
		

#main code
current_pos=[]

while i != len(d)-1 and j!= len(d)-1:
	temp, current_pos= adj()
	ans+=temp
	i,j=current_pos[0],current_pos[1]
ans+=d[len(d)-1][len(d)-1]
print(ans)