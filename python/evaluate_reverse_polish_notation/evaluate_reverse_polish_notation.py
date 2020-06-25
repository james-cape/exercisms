class Solution:
    def get_answer(self, tokens):
        operators = {
            '+': self.add_solution,
            '-': self.sub_solution,
            '*': self.mul_solution,
            '/': self.div_solution
        }
        results_stack = []  # Stack

        for token in tokens:
            if token not in operators:
                results_stack.append(token)
            else:
                last_element = results_stack.pop()
                second_to_last_element = results_stack.pop()
                result = operators[token](second_to_last_element, last_element)
                results_stack.append(result)
        return int(round(float(results_stack[0]), 0))

    def add_solution(self, operand_1, operand_2):
        return str(float(operand_1) + float(operand_2))

    def sub_solution(self, operand_1, operand_2):
        return str(float(operand_1) - float(operand_2))

    def mul_solution(self, operand_1, operand_2):
        return str(float(operand_1) * float(operand_2))

    def div_solution(self, operand_1, operand_2):
        return str(int(float(operand_1) / float(operand_2)))



#   tokens = ["2", "1", "+", "3", "*"]
#   2 [2]
#   1 [2, 1]
#   + [3]
#   3 [9]