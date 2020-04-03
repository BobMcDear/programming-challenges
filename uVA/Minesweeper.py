# The output fields
global output_fields 
output_fields = []

# Receives the fields(The inputs)
def get_fields():
	while True:
		rows, columns = map(int, input().split())

		# If lines and columns are 0, then exit the function
		if (rows and columns) == 0:
			return


		# Arrays start at 0
		rows, columns = rows - 1, columns - 1

		# The field
		field = []

		for i in range(rows + 1):
			# Add the new line to the field
			field.append(input())

		# Generate the output to the current field
		described_map(field, rows, columns)

# Generates the output to a field and add it to output_fields
def described_map(field, rows, columns):
	# The output
	output = []

	# Returns the index of squares adjacent to a square
	def adjacent_squares(index, rows, columns):
		# The adjacent squares 
		adjacents = []

		# You can go 1 index to any side or don't move
		moves = (-1, 0, +1)

		for i in moves:
			for j in moves:
				# The adjacent square's row
				adjacent_row = i + index[0]

				# The adjacent square's column
				adjacent_column = j + index[1]

				# If the row is bigger than 0 and smaller than the number of rows and the column is bigger than 0 and smaller than the number of columns, add the square to adjacents
				if 0 <= adjacent_row <= rows and 0 <= adjacent_column <= columns:
					adjacents.append([adjacent_row, adjacent_column])


		# We also counted the square itself(When i and j both equal to 0).So remove it from res
		adjacents.remove(index)

		return adjacents

	# The number of adjacent mines to a square
	def adjacent_mines(index, rows, columns, field):
		# The answer
		adjacent_mn = 0

		# The adjacent squares
		adjacent_sq = adjacent_squares(index, rows, columns)

		for i in adjacent_sq:
			# If the current square is a mine, ad 1 to adjacent_mn
			if field[i[0]][i[1]] == "*":
				adjacent_mn += 1

		return str(adjacent_mn)

	for i in range(rows + 1):
		# The new line in the output
		new_line = ''
		for j in range(columns + 1):
			if field[i][j] == "*":
				new_line += "*"
				continue

			new_line += adjacent_mines([i, j], rows, columns, field)

		output.append(new_line)

	output_fields.append(output)


def main():
	get_fields()

	for i in range(len(output_fields)):
		print("Field #" + str(i + 1) +":")

		for j in output_fields[i]:
			print(j)


		if i != len(output_fields) - 1:
			print("")

main()