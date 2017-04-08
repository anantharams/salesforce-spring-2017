"""
INSTRUCTIONS:

Complete these excercises one by one. 
Check each as you go with the provided "Test with" statement. 

Happy coding!

Test ALL with:
$ py.test tests/test_syntax.py::SyntaxExcercises
"""

def crazy_cases(color, number, name):
    """
    @param: color (string)
    @param: number (numeric)
    @param: name (string)
    @return: 
        if the color is 'blue' return 1
        otherwise if number is 14, return 'purple'
        otherwise if name is 'joe', return 2
        otherwise return 9

    Test with:
    $ py.test tests/test_syntax.py::SyntaxExcercises::test_crazy_cases
    """
    return None


def add_then_multiply(a, b, c):
    """
    @param: a (numeric)
    @param: b (numeric)
    @param: c (numeric)
    @return: the product of c and a plus b
    """
    return None


def n_mod_m_to_the_p(n, m, p):
    """
    @param: n (numeric)
    @param: m (numeric)
    @param: p (numeric)
    @return: 
        remainder of n divided by m, this to the `p`th power

    Test with:
    $ py.test tests/test_syntax.py::SyntaxExcercises::test_n_mod_m_to_the_p
    """
    return None

def clamp(value, hi, lo):
    """
    We want to make sure our value is in the range [lo, hi]

    If value is less than, lo, return lo. If value is greater than hi, return hi, 
    otherwise return value:

    @param: value (numeric)
    @param: hi (numeric)
    @param: lo (numeric)
    @returns: numeric

    Test with:
    $ py.test tests/test_syntax.py::SyntaxExcercises::test_clamp
    """
    return None

def exponentiate_hard(power):
    """
    Compute 2^power

    Do NOT use the ** operator 
    Do NOT use math.pow() 
    Do NOT use the multiplication operator (*) or multiplication assigment operator (*=)
    Do NOT use a simple equals sign (=)

    :)

    HINT: You don't need to use the number 2, either! (Only 0 & 1...)

    @param: power (positive integer)
    @returns: 2 ^ power (positive integer)

    Test with:
    $ py.test tests/test_syntax.py::SyntaxExcercises::test_exponentiate_hard
    """
    return None 

