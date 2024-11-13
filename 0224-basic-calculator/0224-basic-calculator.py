class Solution:
    def calculate(self, s: str) -> int:
        numbers = deque()
        operators = deque()
        number = deque()
        for c in f"({s})":
            if c == ' ':
                if len(number):
                    numbers.append(int(''.join(number)))
                    number = deque()
                continue
            elif c == '+':
                if len(number):
                    numbers.append(int(''.join(number)))
                    number = deque()
                operators.append(c)
            elif c == '-':
                if len(number):
                    numbers.append(int(''.join(number)))
                    number = deque()
                operators.append(c)
            elif c == '(':
                operators.append(c)
                numbers.append(c)
            elif c == ')':
                if len(number):
                    numbers.append(int(''.join(number)))
                    number = deque()
                # print(f"op={operators}, numbers={numbers}")
                while operators[-1] != '(':
                    # print(f"op={operators}, numbers={numbers}")
                    right_operand = numbers.pop()
                    op = operators.pop()
                    if numbers[-1] == '(':
                        if op == '-':
                            # print(f"inverting sign of {right_operand}")
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
                # print(f"e op={operators}, numbers={numbers}")
                operators.pop()
                last_n = numbers.pop()
                numbers.pop()
                numbers.append(last_n)
                # print(f"end, op={operators}, numbers={numbers}")
                # operations_to_be_done = deque()
                # numbers_to_be_used = deque()
                # while len(operators) and operators[-1] != '(':
                #     operations_to_be_done.appendleft(operators.pop())
                # while len(numbers) and numbers[-1] != '(':
                #     numbers_to_be_used.appendleft(numbers.pop())
                # if len(operations_to_be_done) == len(numbers_to_be_used):
                #     numbers_to_be_used.appendleft(-numbers_to_be_used.popleft())
                #     operations_to_be_done.popleft()
                # while len(operations_to_be_done):
                #     op = operations_to_be_done.popleft()
                #     left_operand = numbers_to_be_used.popleft()
                #     right_operand = numbers_to_be_used.popleft()
                #     if op == '-':
                #         numbers_to_be_used.appendleft(left_operand - right_operand)
                #     else:
                #         numbers_to_be_used.appendleft(left_operand + right_operand)
                # # remove (
                # operators.pop()
                # numbers.pop()
                # #

                # numbers.append(numbers_to_be_used[0])
            else:
                number.append(c)
        # print(numbers, operators)
        return numbers[0]