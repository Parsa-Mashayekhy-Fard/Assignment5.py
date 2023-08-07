def print_chessboard(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                print("#", end="")
            else:
                print("*", end="")
        print()

rows = 8  # You can change the number of rows and columns as needed
cols = 8
print_chessboard(rows, cols)
