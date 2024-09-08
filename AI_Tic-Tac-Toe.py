

#game board
board = [' ']*9

#change turns
def change(x_o):
	if x_o=="x":
		x_o=="o"
	if x_o=="o":
		x_o=="x"

#insert move
def insert_move(x_o,pos):
	board[pos]=x_o

#empty spaces
def empty_spaces():
	empty_boxes=[]
	for i in len(board):
		if board[i] == ' ':
			empty_boxes.append(i)
	return empty_boxes
			
#checks win
def has_won(x_o):
	winning_seq = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
	for i in winning_seq:
		if board[i[0]]==board[i[1]]==board[i[2]]==x_o:
			return True
	return False

#checks if board is full
def board_full():
	if ' ' not in board:
		return True
	return False

#player move
def player_move():
	while True:
		try:
			move = int(input("enter move: "))-1
			if board[move]==' ' and move > 0:
				board[move] = 'x'
				break
			else:
				print("enter a balid number(0-8): ")
		except:
			print("enter a number ")

#AI move
def ai_move():
    best_score = -1000
    best_move = 0
    for key in range(9):
        if board[key] == ' ':
            board[key] = 'o'
            score = minimax(False)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
    insert_move('o', best_move)

#minimax
def minimax(is_o_turn):
    if has_won('o'):
        return 10
    elif has_won('x'):
        return -10
    elif board_full():
        return 0

    if is_o_turn:
        best_score = -1000
        for key in range(9):
            if board[key] == ' ':
                board[key] = 'o'
                score = minimax(False)
                board[key] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for key in range(9):
            if board[key] == ' ':
                board[key] = 'x'
                score = minimax(True)
                board[key] = ' '
                best_score = min(score, best_score)
        return best_score

def print_board():
	for i in range(3):
		print(f'|{board[3*i]}|{board[3*i+1]}|{board[3*i+2]}|')

def main():
    print('Welcome to Tic Tac Toe!')
    print('You play as X and the AI plays as O.')
    print_board()
    while True:
        player_move()
        if has_won('x'):
            print_board()
            print('Congratulations, you won!')
            break
        elif board_full():
            print_board()
            print('It\'s a tie!')
            break
        
        ai_move()
        print_board()
        if has_won('o'):
            print_board()
            print('Sorry, the AI won!')
            break

main()


