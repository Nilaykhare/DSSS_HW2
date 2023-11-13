import unittest
from math_quiz import randomInterger, randomOperation, operationOutput


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomInterger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # TODO
        for _ in range(10):
            operation = randomOperation()
            self.assertTrue(operation in ['+', '-', '*'])
        

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
            ]

            for test_case in test_cases:
                print("###################")
                print(test_case)
                num1, num2, operator, expected_problem, expected_answer = test_case
                self.assertTrue(operationOutput(num1, num2, operator)[1]==expected_answer)
                
if __name__ == "__main__":
    unittest.main()
