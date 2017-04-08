import os
import json 
import cPickle as pickle

class InvalidJSONException(Exception):
    pass

def get_second_line_of_file(filepath):
    """
    Do not edit / change value of the file. 

    @param: filepath
    @return: line from file with newlines removed
    """
    return None

def get_dictionary_from_json(filepath):
    """
    @param: filepath (string)
    @return: python dictionary from contents of JSON file 

    Raise InvalidJSONException if file does not contain valid JSON
    """
    return None

def load_pickle_as_json_string(filepath):
    """
    @param: filepath (string)
    @return: string of JSON from object pickled inside filepath
    """
    return None

