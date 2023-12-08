import print_helper


class Test:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def calculate(self):
        print('########## Test / Reduct ##########')
        all_different_rows = self.get_rows_with_different_decision()
        print_all_different_decisions(all_different_rows)
        column_row_pairs: list[list[list[int]]] = []
        print(f'---------- iteration: 0 ----------')
        for column_index in range(0, len(self.matrix[0]) - 1):
            row_pair = self.get_rows_with_different_value(column_index, all_different_rows)
            print_rows_with_different_values(column_index, row_pair)
            column_row_pairs.append(row_pair)
        iteration = 0
        test: list[int] = []
        while any(len(pairs) > 0 for pairs in column_row_pairs):
            iteration += 1
            print(f'---------- iteration: {iteration} ----------')
            best_column = max(column_row_pairs, key=len).copy()
            test.append(column_row_pairs.index(best_column))
            for column_row_pair in column_row_pairs:
                for row_pair in best_column:
                    if row_pair in column_row_pair:
                        column_row_pair.remove(row_pair)
            for column_index in range(0, len(column_row_pairs)):
                print_rows_with_different_values(column_index, column_row_pairs[column_index])
        print('------------- result: ------------')
        print_test(test)
        print('###########################')

    def get_rows_with_different_decision(self) -> list[list[int]]:
        all_row_pairs: list[list[int]] = []
        for row_index in range(0, len(self.matrix)):
            decision: int = self.matrix[row_index][len(self.matrix[row_index]) - 1]
            rows_with_different_decisions: list[int] = []
            for row_index2 in range(row_index + 1, len(self.matrix)):
                if self.matrix[row_index2][len(self.matrix[row_index2]) - 1] != decision:
                    rows_with_different_decisions.append(row_index2)
            for pair in rows_with_different_decisions:
                all_row_pairs.append([row_index, pair])
        return all_row_pairs

    def get_rows_with_different_value(self, column_index: int, available_rows: list[list[int]]) -> list[list[int]]:
        pairs: list[list[int]] = []
        for row_index in range(0, len(self.matrix)):
            value = self.matrix[row_index][column_index]
            row_list: list[int] = []
            for row_index2 in range(row_index + 1, len(self.matrix)):
                if (available_rows.__contains__([row_index, row_index2])
                        and self.matrix[row_index2][column_index] != value):
                    row_list.append(row_index2)
            for pair in row_list:
                pairs.append([row_index, pair])
        return pairs


def print_all_different_decisions(different_rows: list[list[int]]):
    print(f'{len(different_rows)}: P(T) = {{', end='')
    for i in range(0, len(different_rows)):
        print(f'{{r{different_rows[i][0] + 1},r{different_rows[i][1] + 1}}}', end='')
        if i != len(different_rows) - 1:
            print(',', end='')
    print('}')


def print_rows_with_different_values(column_index: int, rows: list[list[int]]):
    print(f'{len(rows)}: P(T,f{column_index + 1}) = {{', end='')
    for i in range(0, len(rows)):
        print(f'{{r{rows[i][0] + 1},r{rows[i][1] + 1}}}', end='')
        if i != len(rows) - 1:
            print(',', end='')
    print('}')

def print_test(test: list[int]):
    print('Q = {', end='')
    for i in range(0, len(test)):
        print(f'f{test[i] + 1}', end='')
        if i != len(test) - 1:
            print(',', end='')
    print('}')
