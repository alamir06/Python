# treasure map 
line1=["⬜","⬜", "⬜"]
line2=["⬜","⬜", "⬜"]
line3=["⬜","⬜", "⬜"]
treasure_map = [line1, line2, line3]
print("Head to the treasure! X marks the spot!")
input_position = input("Enter the position to place the treasure (row,col): ") #e.g b2
letters = ["a", "b", "c"]
row=input_position[0].lower()
row_index = letters.index(row)
col=input_position[1]
col_index = int(col) - 1
treasure_map[row_index][col_index] = "X"
print(f"{line1},\n {line2},\n {line3}")

# This code creates a simple treasure map and allows the user to place a treasure marker at a specified position.
