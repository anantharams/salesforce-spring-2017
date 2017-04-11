
def similar(first, second):
    """
    Return a list of elements that are in BOTH first and second lists

    @param: first (list)
    @param: second (list)

    Test with:
    $ py.test tests/test_ds.py::DataStructureExcercises::test_similar
    """    
    return list(set(first).intersection(set(second)))

def contained(big_list, small_list):
    """
    Return a boolean whether or not small_list is a subset of big_list

    @param: big_list (list)
    @param: small_list (list)
    @return: boolean 
    """
    return set(small_list) <= set(big_list)

def copy_and_change_set(original_set, element):
    """
    Return a new set with the element added. Do NOT modify the original set. 
    """
    new_set = set(original_set)
    new_set.add(element)
    return new_set