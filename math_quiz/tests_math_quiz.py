import unittest
from math_quiz import Random_Integer, Operator_Selector, Solver


class TestMathGame(unittest.TestCase):

    def test_Random_Integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Random_Integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Operator_Selector(self):
        # test if the output is within range of expected values
        for _ in range(1000):  # Test a large number of random values
            random_operator = Operator_Selector()
            self.assertTrue(random_operator=='+' or random_operator=='*' or random_operator=='-')

    def test_Solver(self):
            # test the solver for some problems, feel free to add more
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 0, '+', '5 + 0', 5),
                (5, 2, '-', '5 - 2', 3),
                (5, 0, '-', '5 - 0', 5),
                (5, 2, '*', '5 * 2', 10),
                (5, 0, '*', '5 * 0', 0)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                PROBLEM, ANSWER = Solver(num1, num2, operator)
                self.assertTrue(PROBLEM==expected_problem and ANSWER==expected_answer)
                

if __name__ == "__main__":
    unittest.main()
