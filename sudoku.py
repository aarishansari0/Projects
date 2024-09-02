
#declaration and initialization

a =[[3,0,6,5,0,8,4,0,0],
[5,2,0,0,0,0,0,0,0],
[0,8,7,0,0,0,0,3,1],
[0,0,3,0,1,0,0,8,0],
[9,0,0,8,6,3,0,0,5],
[0,5,0,0,9,0,6,0,0],
[1,3,0,0,0,0,2,5,0],
[6,9,2,0,0,0,0,7,4],
[7,4,5,2,8,6,3,1,0]]

spaces =[]

#making the functions
#the empty spaces
def empty_spaces(spaces, board):
	for i in range(9):
		for j in range(9):
			if a[i][j]== 0:
				new_elem = [i,j]
				spaces.append(new_elem)
#

#checking rows and columns
def row_col(spaces, a):
	for r in spaces:
		x,y=r[0],r[1]
		poss=[1,2,3,4,5,6,7,8,9]
		for i in range(9):
			if a[i][y] in poss:
				poss.remove(a[i][y])
			if a[x][i] in poss:
				poss.remove(a[x][i])
		
		#checking the boxes
		nx = x-(x%3)
		ny= y-(y%3)
		for i in range(3):
			for j in range(3):
				if a[nx+i][ny+j] in poss:
					poss.remove(a[nx+i][ny+j])

		#putting value
		if len(poss) == 1:
			a[x][y]= poss[0]
			spaces.remove(r)

	#printing board
	for rows in a:
		print(rows)
	print("\n")
#	
			
empty_spaces(spaces,a)
i=0
over=0
while over==0 and i<=81:
	row_col(spaces,a)
	i+=1
	over=1
	for rows in a:
		if 0 in rows:
			over=0