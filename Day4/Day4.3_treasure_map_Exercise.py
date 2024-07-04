
row1 = ['🧁', '🧁', '🧁']
row2 = ['🧁', '🧁', '🧁']
row3 = ['🧁', '🧁', '🧁']

map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = input('Where do you want to put the treasure?  ')
map_column = (int(position[1])-1)
map_row = (int(position[0])-1)

# print(f'Position column: {map_column}')
# print(f'Position row: {map_row}')
map[map_column][map_row] = '🌲'
print(f'{row1}\n{row2}\n{row3}')