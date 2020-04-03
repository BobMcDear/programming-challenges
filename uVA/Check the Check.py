# The outputs for all the boards
global output
output = []

# Takes the input boards
def take_input():
	# The new board
	board = []

	for i in range(8):
		# The new line in the board
		line = input()

		# Add the line to the board
		board.append(line)

	# It generates the output for the current board
	checked_king(board)

# Generates the output to a board
def checked_king(board):
	# Finds the index of the white and black queen
	def king_index(board):
		# The index of the white king
		white_king_index = []

		# The index of the black king
		black_king_index = []

		for i in range(8):
			for j in range(8):
				if board[i][j] == "K":
					white_king_index = [i, j]

				if board[i][j] == "k":
					black_king_index = [i, j]

		return (white_king_index, black_king_index)

	# Checks whether a list of positions is valid or not(Indexes less than 0 or greater than 7).If there are any, remove them
	def isValid(pos_list):
		def isOk(pos_list):
			for i in pos_list:
				if ((i[0] or i[1]) < 0) or ((i[0] or i[1]) > 7):
					return False
			return True


		while not isOk(pos_list):
			for i in pos_list:
				if ((i[0] or i[1]) < 0) or ((i[0] or i[1]) > 7):
					pos_list.remove(i)

		return pos_list

	# Sees if a king is being threatened by the other player's pieces
	def isBeingThreatened(board, king_index, color):
		king_row, king_column = king_index[0], king_index[1]

		# If it's a white king, then the opponent's pieces are small letters.But if it's black, then the opponent's pieces are uppercase letters,And also the pawns directions are different
		if color == "Black":
			opponent_pieces = ["P", "K", "B", "R", "Q", "K"]
			# Check for pawns
			if king_index in [[king_index[0] + 1, king_index[1] - 1], [king_index[0] + 1, king_index[1] + 1]]:
				return True

		else:
			opponent_pieces = ["p", "k", "b", "r", "q", "k"]
			# Check for pawns
			if king_index in [[king_index[0] - 1, king_index[1] - 1], [king_index[0] - 1, king_index[1] + 1]]:
				return True

		# Check for rooks and queens
		# Go to left, right, up, down
		left = right = king_index[1]
		up = down = king_index[0]

		for i in range(7):
			left -= 1
			right += 1
			up -= 1
			down += 1

			# Check all of the indices and if any is a rook or a bishop, return true(Also if one gets out of the board or there is another piece on it, set the value to 999)
			if left < 0 or left > 7 or (board[king_row][left] != (opponent_pieces[3] and opponent_pieces[4] and ".")):
				left = 999
			if right < 0 or right > 7 or (board[king_row][right] != (opponent_pieces[3] and opponent_pieces[4] and ".")):
				right = 999
			if up < 0 or up > 7 or (board[up][king_column] != (opponent_pieces[3] and opponent_pieces[4] and ".")):
				up = 999
			if down < 0 or down > 7 or (board[down][king_column] != (opponent_pieces[3] and opponent_pieces[4] and ".")):
				down = 999

			if left != 999 and board[king_row][left] == (opponent_pieces[3] or opponent_pieces[4]):
				return True

			if right != 999 and board[king_row][right] == (opponent_pieces[3] or opponent_pieces[4]):
				return True

			if up != 999 and board[up][king_column] == (opponent_pieces[3] or opponent_pieces[4]):
				return True

			if down != 999 and board[down][king_column] == (opponent_pieces[3] or opponent_pieces[4]):
				return True






		# Checks for bishops and queens
		# Left-up, right_up, left_down and right-down diagonals
		l_u = r_u = l_d = r_d = king_index

		for i in range(1, 7):
			if l_u != 999:
				l_u = [l_u[0] - 1, l_u[1] - 1]

			if r_u != 999:
				r_u = [r_u[0] - 1, r_u[1] + 1]
			
			if l_d != 999:
				l_d = [l_d[0] + 1, l_d[1] - 1]

			if r_d != 999:
				r_d = [r_d[0] + 1, r_d[1] + 1]

			if l_u != 999 and ((l_u[0] or l_u[1]) < 0 or (l_u[0] or l_u[1]) > 7):
				l_u = 999
			if r_u != 999 and (((r_u[0] or r_u[1]) < 0) or (r_u[0] or r_u[1]) > 7):
				r_u = 999
			if l_d!=999 and ((l_d[0] or l_d[1]) < 0 or (l_d[0] or l_d[1]) > 7):
				l_d = 999
			if r_d !=999 and((r_d[0] or r_d[1]) < 0 or (r_d[0] or r_d[1]) > 7):
				r_d = 999

			if l_u != 999 and (board[l_u[0]][l_u[1]] != ("." and opponent_pieces[2] and opponent_pieces[4])):
				l_u = 999

			try:
				if r_u != 999 and (board[r_u[0]][r_u[1]] != ("." and opponent_pieces[2] and opponent_pieces[4])):
					r_u = 999
			except:
				print(r_u)

			if l_d != 999 and (board[l_d[0]][l_d[1]] != ("." and opponent_pieces[2] and opponent_pieces[4])):
				l_d = 999

			if r_d != 999 and (board[r_d[0]][r_d[1]] != ("." and opponent_pieces[2] and opponent_pieces[4])):
				r_d = 999

			diagonals = [l_u,r_u,l_d,r_d]
			
			while True:
				try:
					diagonals.remove(999)

				except:
					break



			diagonals = isValid(diagonals)

			for i in diagonals:
				if board[i[0]][i[1]] in (opponent_pieces[2] or opponent_pieces[4]):
					return True

			


		# Checks for knights
		# The moves that a knight can make
		knight_moves = [(-1, -2), (-2, -1), (-2, +1), (-1, +2), (+2, -1), (+1, -2), (+1, +2), (+2, +1)]

		# The positions that the knight can be in
		knight_positions = []

		for i in knight_moves:
			# A new position the knight might be in
			new_pos_knight = [king_index[0] + i[0], king_index[1] + i[1]]

			knight_positions.append(new_pos_knight)

		# Check if all the positions are valid
		knight_positions = isValid(knight_positions)		
		print("knight ",knight_positions)
		for i in knight_positions:
			if board[i[0]][i[1]] == opponent_pieces[1]:
				return True

		return False

	
	# The index of the kings
	kings_index = king_index(board)

	# The position of the white and black kings
	white_king_index, black_king_index = kings_index[0], kings_index[1]

	# Is white king threatened or not
	white_king_threatened = isBeingThreatened(board, white_king_index, "White")

	# Is black king being threatened or not
	black_king_threatened = isBeingThreatened(board, black_king_index, "Black")

	if black_king_threatened:
		output.append("black king is in check.")
		return

	if white_king_threatened:
		output.append("white king is in check.")
		return 

	output.append("no king is in check.")
	return


board = ["rnbqk.nr","ppp..ppp","....p...","...p....",".bPP....",".....N..","PP..PPPP","RNBQKB.R"]
checked_king(board)
print(output)