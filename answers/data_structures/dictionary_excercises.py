def counter(elements):
    """
    Given a list of elements, return a dictionary where 
    each key is an element, and the value is the integer number of times
    it appeared in the original list. 

    @param: elements (list)

    Test with:
    $ py.test tests/data_structures/test_dictionaries.py::DictExcercises::test_counter
    """
    counts = {}  # element -> int
    for e in elements:
        if e in counts:
            counts[e] += 1
        else:
            counts[e] = 1
    return counts