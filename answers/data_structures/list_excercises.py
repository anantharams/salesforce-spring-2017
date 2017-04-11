
def combine_lists(list1, list2, list3):
    """
    @param: list1 (list)
    @param: list2 (list)
    @param: list3 (list)

    @return: combined list with elements from all three lists 
    """
    return list1 + list2 + list3

def evens(n):
    """
    Return a list of all integers greater than 0 and up 
    to (and including) `n` that are even.

    @param: n (positive, numeric)

    Test with:
    $ py.test tests/data_strctures/list_excercises.py::SyntaxExcercises::test_evens
    """
    elements = []
    for i in range(n + 1):
        if i % 2 == 0 and i > 1:
            elements.append(i)
    return elements

def begin_and_end(elements, item):
    """
    @param: elements (list of length at least 2)
    @param: item 
    @return: elements but with item inserted to be both the second and last element. 

    HINT: list length should grow by two
    """
    elements.insert(1, item)
    elements.append(item)
    return elements

def csv_line(elements, sep):
    """
    Given a list of elements make a string that is each object's 
    string representation, separated by the `sep` string. 

        >>> print csv_line([0, None, 'apple'], ",")
        0,None,apple

    HINT: You may need to convert elements to strings. 

    BONUS POINTS: Do this in a single line! Look up the `join()` function.

    Test with:
    $ py.test tests/test_ds.py::DataStructureExcercises::test_csv_line
    """
    return sep.join([str(e) for e in elements])

