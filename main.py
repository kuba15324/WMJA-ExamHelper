import print_helper
from decision_rules import DecisionRules
from decision_tree import DecisionTree
from test import Test


class ExamHelper:

    def __init__(self, filename: str):
        self.matrix: list[list[int]] = []
        self.read_input_matrix(filename)
        print_helper.print_matrix(self.matrix)
        Test(self.matrix).calculate()
        print()
        DecisionRules(self.matrix).calculate()
        print()
        DecisionTree(self.matrix).calculate()

    def read_input_matrix(self, filename: str):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.matrix = [line.replace('\n', '').split(',') for line in lines]


if __name__ == '__main__':
    helper = ExamHelper('input_table.csv')

