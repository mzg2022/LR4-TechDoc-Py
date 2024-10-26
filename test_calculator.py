import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Тесты для класса Calculator."""

    def setUp(self):
        """Создает экземпляр калькулятора для тестов."""
        self.calc = Calculator()

    def test_add(self):
        """Тест для метода сложения."""
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self):
        """Тест для метода вычитания."""
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        """Тест для метода умножения."""
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        """Тест для метода деления."""
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_divide_by_zero(self):
        """Тест для деления на ноль."""
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

if __name__ == '__main__':
    unittest.main()
