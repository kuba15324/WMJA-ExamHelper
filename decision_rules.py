import print_helper


class DecisionRules:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def calculate(self):
        print('########## Decision Rules ##########')
        for row_index in range(0, len(self.matrix)):
            if row_index > 0:
                print()
            # get rows with different last value
            rows_with_different_decisions = self.get_rows_with_different_decision(row_index)
            print_helper.print_different_decisions(row_index, rows_with_different_decisions)
            # for each column except last, get rows with different values from different_rows
            rows_with_different_values = self.get_rows_with_different_values(row_index, rows_with_different_decisions)
            print(f'---------- iteration: 0 ----------')
            for i in range(0, len(rows_with_different_values)):
                print_helper.print_rows_with_different_values(row_index, i, rows_with_different_values[i])
            # form decision rule
            rule = self.form_rule(row_index, rows_with_different_values)
            print(f'-------- rule for row: r{row_index + 1} --------')
            print_helper.print_rule(row_index, rule, self.matrix)
        print('####################################')

    # get rows with different last value
    def get_rows_with_different_decision(self, row_index: int) -> list[int]:
        decision: int = self.matrix[row_index][len(self.matrix[row_index]) - 1]
        rows_with_different_decisions: list[int] = []
        for row_index2 in range(0, len(self.matrix)):
            if self.matrix[row_index2][len(self.matrix[row_index2]) - 1] != decision:
                rows_with_different_decisions.append(row_index2)
        return rows_with_different_decisions

    # get indexes of rows with different values in given column
    def get_rows_with_different_values(self, row_index: int, available_rows: list[int]) -> list[list[int]]:
        # list of lists of indexes of rows with different values in columns
        lst: list[list[int]] = []
        for column_index in range(0, len(self.matrix[0]) - 1):
            value = self.matrix[row_index][column_index]
            column_list: list[int] = []
            for row_index2 in range(0, len(self.matrix)):
                if available_rows.__contains__(row_index2) and self.matrix[row_index2][column_index] != value:
                    column_list.append(row_index2)
            lst.append(column_list)
        return lst

    # form decision rule for given row
    def form_rule(self, row_index: int, rows_with_different_values: list[list[int]], index: int = 0) -> list[int]:
        if all(len(column) == 0 for column in rows_with_different_values):
            return []
        print(f'---------- iteration: {index + 1} ----------')
        # select column with most different values
        best_column = max(rows_with_different_values, key=len).copy()
        rule = [rows_with_different_values.index(best_column)]
        # remove best_column values from every column
        for column_index in range(0, len(rows_with_different_values)):
            for value in best_column:
                if value in rows_with_different_values[column_index]:
                    rows_with_different_values[column_index].remove(value)
                # print column
            print_helper.print_rows_with_different_values(row_index, column_index, rows_with_different_values[column_index])
        # form rule recursively
        return rule + self.form_rule(row_index, rows_with_different_values, index + 1)
