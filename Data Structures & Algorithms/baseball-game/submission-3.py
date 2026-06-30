class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0

        for op in operations:
            if op == "+":
                first = stack.pop()
                second = stack.pop()
                _sum = first + second
                stack.append(second)
                stack.append(first)
                stack.append(_sum)
                continue
            elif op == "D":
                score = stack.pop()
                doubled = score * 2
                stack.append(score)
                stack.append(doubled)
                continue
            elif op == "C":
                stack.pop()
                continue
            else:
                stack.append(int(op))
        while stack:
            result += stack.pop()

        return result