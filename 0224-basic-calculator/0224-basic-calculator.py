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
                operations_to_be_done = deque()
                numbers_to_be_used = deque()
                # print(operators, numbers)
                while len(operators) and operators[-1] != '(':
                    operations_to_be_done.appendleft(operators.pop())
                while len(numbers) and numbers[-1] != '(':
                    numbers_to_be_used.appendleft(numbers.pop())
                # print("f", operations_to_be_done, numbers_to_be_used)
                if len(operations_to_be_done) == len(numbers_to_be_used):
                    numbers_to_be_used.appendleft(-numbers_to_be_used.popleft())
                    operations_to_be_done.popleft()
                while len(operations_to_be_done):
                    op = operations_to_be_done.popleft()
                    left_operand = numbers_to_be_used.popleft()
                    right_operand = numbers_to_be_used.popleft()
                    if op == '-':
                        numbers_to_be_used.appendleft(left_operand - right_operand)
                    else:
                        numbers_to_be_used.appendleft(left_operand + right_operand)
                # remove (
                operators.pop()
                numbers.pop()
                #

                numbers.append(numbers_to_be_used[0])
                # print(numbers, operators, numbers_to_be_used)
            else:
                number.append(c)
        # print(numbers, operators)
        return numbers[0]