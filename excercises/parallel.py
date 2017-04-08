from multiprocessing.dummy import Pool as ThreadPool 

def square_numbers(numbers, nthreads):
    """
    @param: numbers (list of numerics)
    @param: nthreads (positive integer)
    @return: list of squares of numbers using `nthreads` threads

    HINT: Use threads and a ThreadPool
    """
    return None