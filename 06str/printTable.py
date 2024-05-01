def print_table(table_data):
    col_widths = [0] * len(table_data)
    for col in range(len(col_widths)):
        col_widths[col] = max([len(c) for c in table_data[col]])
    # print(col_widths)

    for j in range(len(table_data[0])):
        for i in range(len(table_data)):
            print(table_data[i][j].rjust(col_widths[i]), end=' ')
        print()

    print('')


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogsddddddd', 'cats', 'mouse', 'goose']]

print_table(table_data)