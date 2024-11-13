class Solution:
    def calculate(self, s: str) -> int:
        numbers = []
        operators = []
        number = []
        for c in f"({s})":
            if c == ' ':
                if len(number):
                    numbers.append(int(''.join(number)))
                    number = []
                continue
            elif c == '+':
                if len(number):
                    numbers.append(int(''.join(number)))
                    number = []
                operators.append(c)
            elif c == '-':
                if len(number):
                    numbers.append(int(''.join(number)))
                    number = []
                operators.append(c)
            elif c == '(':
                operators.append(c)
                numbers.append(c)
            elif c == ')':
                if len(number):
                    numbers.append(int(''.join(number)))
                    number = []
                while operators[-1] != '(':
                    right_operand = numbers.pop()
                    op = operators.pop()
                    if numbers[-1] == '(':
                        if op == '-':
                            numbers.append(-right_operand)
                        else:
                            numbers.append(right_operand)
                    else:
                        left_operand = numbers.pop()
                        if operators[-1] != '(':
                            left_operand_sign = operators[-1]
                            if left_operand_sign == '-':
                                left_operand = -left_operand
                                operators.pop()
                                operators.append('+')
                        if op == '-':
                            numbers.append(left_operand - right_operand)
                        else:
                            numbers.append(left_operand + right_operand)
                operators.pop()
                last_n = numbers.pop()
                numbers.pop()
                numbers.append(last_n)
            else:
                number.append(c)
        return numbers[0]