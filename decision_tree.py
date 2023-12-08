class DecisionTree:
    def __init__(self, matrix: list[list[int]]):
        self.matrix: list[list[int]] = []
        for row_index in range(0, len(matrix)):
            row = [row_index]
            for item in matrix[row_index]:
                row.append(int(item))
            self.matrix.append(row)

    def calculate(self):
        print(f'########## Decision Tree ##########')
        process_matrix(self.matrix)
        print(f'####################################')


def process_matrix(matrix: list[list[int]]):
    print_matrix(matrix)
    if len(matrix) < 0:
        return
    if count_different_decisions(matrix) == 0:
        print(f'Decision: {matrix[0][len(matrix[0]) - 1]}  <---- Leaf')
        return
    max_decisions: dict[int, int] = {}
    for column_index in range(0, len(matrix[0]) - 2):
        if row_has_same_value(column_index, matrix):
            continue
        sub_matrix0 = filter_matrix(column_index, 0, matrix)
        sub_matrix1 = filter_matrix(column_index, 1, matrix)
        print(f'f{column_index + 1}=0')
        print_matrix(sub_matrix0)
        decisions0 = count_different_decisions(sub_matrix0)
        print(f'|P(f{column_index + 1},0)| = {decisions0}')
        print(f'f{column_index + 1}=1')
        print_matrix(sub_matrix1)
        decisions1 = count_different_decisions(sub_matrix1)
        print(f'|P(f{column_index + 1},1)| = {decisions1}')
        max_decisions[column_index] = max(decisions0, decisions1)
        print(f'Q(f{column_index + 1}) = max({decisions0}, {decisions1}) = {max_decisions[column_index]}')
    print('------------------------------------')
    best_index = list(max_decisions.keys())[list(max_decisions.values()).index(min(max_decisions.values()))]
    print(f'Q(f) = min({list(max_decisions.values())}) = {min(max_decisions.values())} (f{best_index + 1})  <---- Root')
    print()
    sub_matrix0 = filter_matrix(best_index, 0, matrix)
    sub_matrix1 = filter_matrix(best_index, 1, matrix)
    print(f'if f{best_index + 1}=0 then:')
    process_matrix(sub_matrix0)
    print(f'if f{best_index + 1}=1 then:')
    process_matrix(sub_matrix1)


# return rows that has given value in given column
def filter_matrix(column_index: int, value: int, matrix: list[list[int]]) -> list[list[int]]:
    sub_matrix: list[list[int]] = []
    for row_index in range(0, len(matrix)):
        if matrix[row_index][column_index + 1] == value:
            sub_matrix.append(matrix[row_index])
    return sub_matrix


# count pairs of rows with different decisions
def count_different_decisions(matrix: list[list[int]]) -> int:
    if len(matrix) < 2:
        return 0
    counter = 0
    for row_index in range(0, len(matrix) - 1):
        for row_index2 in range(row_index + 1, len(matrix)):
            if matrix[row_index][len(matrix[row_index]) - 1] != matrix[row_index2][len(matrix[row_index2]) - 1]:
                counter += 1
    return counter


def row_has_same_value(column_index: int, matrix: list[list[int]]) -> bool:
    value = matrix[0][column_index + 1]
    for row_index in range(1, len(matrix)):
        if matrix[row_index][column_index + 1] != value:
            return False
    return True


def print_matrix(matrix: list[list[int]]):
    if len(matrix) == 0:
        return
    print('   ', end='')
    for column_index in range(0, len(matrix[0]) - 2):
        print(f'f{column_index + 1} ', end='')
    print(' d')
    for row_index in range(0, len(matrix)):
        print(f'r{matrix[row_index][0] + 1} ', end='')
        for column_index1 in range(1, len(matrix[row_index])):
            print(f' {matrix[row_index][column_index1]} ', end='')
        print()
