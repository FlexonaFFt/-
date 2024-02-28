class StackMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if not self.stack:
            print("error")
            return
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        return self.stack.pop()

    def get_max(self):
        if not self.stack:
            print("None")
            return
        print(self.max_stack[-1])

# Считываем количество команд
print("Можете вводить команды: ")
n = int(input())

# Создаем экземпляр класса StackMax
stack_max = StackMax()

# Обрабатываем команды
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        stack_max.push(int(command[1]))
    elif command[0] == "pop":
        stack_max.pop()
    elif command[0] == "get_max":
        stack_max.get_max()