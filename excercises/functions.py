
def cycle_colors(colors):
    """
    Return a generator that continually cycles through colors in this order. 

    For example, if colors was ['red', 'violet', 'blue']:

        'red' 
        'violet' 
        'blue'

            then back to start...

        'red'
        'violet' 
        'blue'

        ...forever 

    @return: generator 

    Test with:
    $ py.test tests/test_functions.py::FunctionExcercises::test_cycle_colors
    """
    counter = 0
    while True:
        index = counter % len(colors)
        yield colors[index]
        counter += 1


# OR
#while True:
#    for color in colors:
#        yeld color

def power_list_factory():
    """
    Return a function. 

    This function should take an integer power as a first argment, 
    and then as many positional numeric arguments after as the caller would like to provide.

    Compute each number raised to a power `pow`, then sum. The function
    you return should compute and return that sum.  

    Test with:
    $ py.test tests/test_functions.py::FunctionExcercises::test_power_list_factory
    """
    def func (p, *ar):
        return sum([x**p for x in ar])
    return func


def dict_updater_factory():
    """
    Return a function. 

    This function should take a variable number of dictionaries
    as arguments. Combine all the dictionaries keys and values together for one 
    master dictionary. In case of conflicts of keys, always use the value 
    farthest from the start of the list of provided arguments. 

        >>> func = dict_updater_factory()
        >>> d1, d2 = {'a' : 1, 'b' : 2}, {'b' : 10, 'c' : 3}
        >>> print func(d1, d2)
        {'a' : 1, 'b' : 10, 'c' : 3}

    Test with:
    $ py.test tests/test_functions.py::FunctionExcercises::test_dict_updater_factory
    """
    return None



















