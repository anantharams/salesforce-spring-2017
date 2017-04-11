def counter(elements):
    """
    Given a list of elements, return a dictionary where 
    each key is an element, and the value is the integer number of times
    it appeared in the original list. 

    @param: elements (list)

    Test with:
    $ py.test tests/test_ds.py::DataStructureExcercises::test_counter
    """
    counts = {}
    for e in elements:
        if e in counts:
            counts[e] += 1
        else:
            counts[e] = 1
    return counts