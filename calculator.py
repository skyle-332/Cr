class Calculator:
    def calculate(self, a, b, operation):
        operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }

        if operation not in operations:
            raise ValueError("Неизвестная операция")

        return operations[operation](a, b)

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b

calc = Calculator()

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ")

try:
    result = calc.calculate(a, b, op)
    print("Результат:", result)
except ValueError as e:
    print("Ошибка:", e)