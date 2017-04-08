import unittest
import tests

if not tests.USE_ANSWERS:
    from excercises.syntax import clamp, add_then_multiply, crazy_cases, \
        n_mod_m_to_the_p, exponentiate_hard
else:
    from answers.syntax import clamp, add_then_multiply, crazy_cases, \
        n_mod_m_to_the_p, exponentiate_hard


class SyntaxExcercises(unittest.TestCase):
    def test_clamp(self):
        hi = 10
        lo = 0
        self.assertEqual(clamp(5, hi, lo), 5)
        self.assertEqual(clamp(11, hi, lo), hi)
        self.assertEqual(clamp(-2, hi, lo), lo)
        self.assertEqual(clamp(0, hi, lo), 0)
        
    def test_add_then_multiply(self):
        self.assertEqual(add_then_multiply(3, 4, 2), 14)
        self.assertEqual(add_then_multiply(0, 0, 2), 0)
        self.assertEqual(add_then_multiply(1, 1, 1), 2)
        self.assertEqual(add_then_multiply(1, 1, -1), -2)
        self.assertEqual(add_then_multiply(3, 4, -2), -14)
        self.assertEqual(add_then_multiply(1, -1, 1), 0)
        self.assertEqual(add_then_multiply(1.3829384, -13948203, 13847), -193140747791.45197)

    def test_crazy_cases(self):
        self.assertEqual(crazy_cases('blue', 13, 'shirley'), 1)
        self.assertEqual(crazy_cases('blue', 14, 'shirley'), 1)
        self.assertEqual(crazy_cases('orange', 14, 'joe'), 'purple')
        self.assertEqual(crazy_cases('orange', -1, 'joe'), 2)
        self.assertEqual(crazy_cases('1', -1, '1'), 9)

    def test_n_mod_m_to_the_p(self):
        self.assertEqual(n_mod_m_to_the_p(10, 3, 2), 1)
        self.assertEqual(n_mod_m_to_the_p(7, 5, 3), 8)
        self.assertEqual(n_mod_m_to_the_p(0, 1, 1), 0)
        self.assertEqual(n_mod_m_to_the_p(123, 34, 3.345), 26474.242394701043)

    def test_exponentiate_hard(self):
        self.assertEqual(exponentiate_hard(0), 1)
        self.assertEqual(exponentiate_hard(1), 2)
        self.assertEqual(exponentiate_hard(2), 4)
        self.assertEqual(exponentiate_hard(3), 8)
        self.assertEqual(exponentiate_hard(4), 16)
        self.assertEqual(exponentiate_hard(5), 32)
        self.assertEqual(exponentiate_hard(32), 4294967296)


