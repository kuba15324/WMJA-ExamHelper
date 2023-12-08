def print_matrix(matrix: list[list[int]]):
    print('  ', end=' ')
    for i in range(1, len(matrix[0])):
        print('f' + str(i), end=' ')
    print(' d')
    # print rows with row label as 'rN'
    for i in range(0, len(matrix)):
        print('r' + str(i + 1), end='  ')
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end='  ')
        print()
    print()


def print_different_decisions(row_index: int, different_rows: list[int]):
    print(f'P(T,r{row_index + 1}) = {{', end='')
    for i in range(0, len(different_rows)):
        print(f'r{different_rows[i] + 1}', end='')
        if i != len(different_rows) - 1:
            print(', ', end='')
    print('}')


def print_rows_with_different_values(row_index: int, column_index: int, rows: list[int]):
    print(f'P(T,r{row_index + 1},f{column_index + 1}) = {{', end='')
    for i in range(0, len(rows)):
        print(f'r{rows[i] + 1}', end='')
        if i != len(rows) - 1:
            print(', ', end='')
    print('}')


def print_rule(row_index: int, rule: list[int], matrix: list[list[int]]):
    print(f'Q(r{row_index + 1}) = {{', end='')
    for i in range(0, len(rule)):
        print(f'f{rule[i] + 1}', end='')
        if i != len(rule) - 1:
            print(', ', end='')
    print('}')
    for i in range(0, len(rule)):
        if i > 0:
            print(' and ', end='')
        print(f'f{rule[i] + 1}={matrix[row_index][rule[i]]}', end='')
    print(f' then d={matrix[row_index][len(matrix[row_index]) - 1]}')
