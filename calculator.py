class Calculator:
    """Класс для выполнения базовых арифметических операций."""

    def add(self, a: float, b: float) -> float:
        """
        Сложение двух чисел.

        Args:
            a (float): Первое число.
            b (float): Второе число.

        Returns:
            float: Сумма a и b.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Вычитание второго числа из первого.

        Args:
            a (float): Первое число.
            b (float): Второе число.

        Returns:
            float: Результат вычитания b из a.
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Умножение двух чисел.

        Args:
            a (float): Первое число.
            b (float): Второе число.

        Returns:
            float: Произведение a и b.
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Деление первого числа на второе.

        Args:
            a (float): Делимое.
            b (float): Делитель.

        Returns:
            float: Результат деления a на b.

        Raises:
            ValueError: Если b равно 0.
        """
        if b == 0:
            raise ValueError("Деление на ноль невозможно.")
        return a / b
