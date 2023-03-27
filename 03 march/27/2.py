class MinStack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, value: int) -> None:
        return self.stack.append(value)

    def pop(self) -> None:
        if self.stack:
            self.stack.remove(self.stack[0])
        return self.stack

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def get_min(self) -> int:
        if self.stack:
            return min(self.stack)


new_stack = MinStack()
    # ["MinStack", "push", "push", "push", "getMin", "pop", "top", "get_min"])
print(new_stack.stack)
print(new_stack.push(-2))
print(new_stack.pop())
print(new_stack.top())
print(new_stack.get_min())

# Вихід
# [null,null,null,null,-3,null,0,-2]

# Пояснення
# MinStack minStack = New MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# minStack.getMin()  # повертає -3
# minStack.pop()
# minStack.top()  # повертає 0
# minStack.getMin()  # повертає -2
