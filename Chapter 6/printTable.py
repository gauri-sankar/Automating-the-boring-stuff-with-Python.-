tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

for row in tableData:
    for field in row:
        print(field.rjust(10),end='')
    print()
