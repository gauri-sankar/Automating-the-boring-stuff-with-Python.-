#! python3
#printTable.py - To print the values in a list of string list in the form of a table that is right justified.
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
maxlength = 0
def printTable(table,maxlength=0):
    colWidth = [0]*len(table)
    for row in table:
        maxlength = max(max(len(row[i])  for i in range(len(row))),maxlength)#find the longest column in the row
        for field in row:
            print(field.rjust(maxlength+1),end='')
        print()
printTable(tableData)
