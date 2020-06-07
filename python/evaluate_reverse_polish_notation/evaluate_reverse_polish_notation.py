class Solution:
    def get_answer(self, tokens):
        operators = ['+', '-', '*', '/']
        index = 2

        while len(tokens) >= 3:
            if tokens[index] in operators:
                new_element = self.calculate(tokens[index-2], tokens[index-1], tokens[index])
                if index >= 3:
                    tokens = tokens[:index-2] + [new_element] + tokens[index+1:]
                else:
                    tokens = [new_element] + tokens[index+1:]
                index = index - 2
            index += 1
        return int(round(float(tokens[0]), 0))

    def calculate(self, operand_1, operand_2, operator):
        if operator == '+':
            return str(float(operand_1) + float(operand_2))
        elif operator == '-':
            return str(float(operand_1) - float(operand_2))
        elif operator == '*':
            return str(float(operand_1) * float(operand_2))
        elif operator == '/':
            return str(int(float(operand_1) / float(operand_2)))


# class Solution:
#     def get_answer(self, tokens):
#         operators = ['+', '-', '*', '/']
#         index = 2

#         while len(tokens) >= 3:
#             if tokens[index] in operators:
#                 new_element = self.calculate(tokens[index-2], tokens[index-1], tokens[index])
#                 if index >= 3:
#                     tokens = tokens[:index-2] + [new_element] + tokens[index+1:]
#                 else:
#                     tokens = [new_element] + tokens[index+1:]
#                 index = index - 2
#             index += 1
#         return int(round(float(tokens[0]), 0))

#     def calculate(self, operand_1, operand_2, operator):
#         if operator == '+':
#             return str(float(operand_1) + float(operand_2))
#         elif operator == '-':
#             return str(float(operand_1) - float(operand_2))
#         elif operator == '*':
#             return str(float(operand_1) * float(operand_2))
#         elif operator == '/':
#             return str(int(float(operand_1) / float(operand_2)))