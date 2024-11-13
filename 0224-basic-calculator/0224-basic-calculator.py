class Solution:
    _plus = "+"
    _minus = '-'
    _open = '('
    _close = ')'
    _space = ' '

    def calculate(self, s: str) -> int:
        numbers = []
        operators = []
        number = []
        for c in f"({s})":
            if c == self._space:
                if len(number):
                    numbers.append(int(''.join(number)))
                    number = []
                continue
            elif c == self._plus:
                if len(number):
                    numbers.append(int(''.join(number)))
                    number = []
                operators.append(c)
            elif c == self._minus:
                if len(number):
                    numbers.append(int(''.join(number)))
                    number = []
                operators.append(c)
            elif c == self._open:
                operators.append(c)
                numbers.append(c)
            elif c == self._close:
                if len(number):
                    numbers.append(int(''.join(number)))
                    number = []
                while operators[-1] != self._open:
                    right_operand = numbers.pop()
                    op = operators.pop()
                    if numbers[-1] == self._open:
                        if op == self._minus:
                            numbers.append(-right_operand)
                        else:
                            numbers.append(right_operand)
                    else:
                        left_operand = numbers.pop()
                        if operators[-1] != self._open:
                            left_operand_sign = operators[-1]
                            if left_operand_sign == self._minus:
                                left_operand = -left_operand
                                operators.pop()
                                operators.append(self._plus)
                        if op == self._minus:
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