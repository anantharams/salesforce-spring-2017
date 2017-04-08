import unittest
import tests
import json

if not tests.USE_ANSWERS:
    from excercises.files import get_second_line_of_file, get_dictionary_from_json, load_pickle_as_json_string, \
        InvalidJSONException
else:
    from answers.files import get_second_line_of_file, get_dictionary_from_json, load_pickle_as_json_string, \
        InvalidJSONException

class ExceptionExcercises(unittest.TestCase):
    
    def test_get_second_line_of_file(self):
        self.assertEqual(get_second_line_of_file("files/notes.txt"), "Super important notes")
        self.assertEqual(get_second_line_of_file("files/example.yaml"), "date   : 2001-01-23")

    def test_get_dictionary_from_json(self):
        d = {"classname" : "Python",
        "number_students" : 25,
        "topics" : [
            "Syntax",
            "OOP",
            "Data Structures"]}

        self.assertEqual(get_dictionary_from_json("files/example.json"), d)
        self.assertRaises(InvalidJSONException, get_dictionary_from_json, "files/notes.txt")


    def test_load_pickle_as_json_string(self):
        d = {
             "firstName": "John", "lastName": "Smith", "age": 25,
             "address" : {
                 "streetAddress": "21 2nd Street",
                 "city": "New York",
                 "state": "NY",
                 "postalCode": "10021"
             },
             "phoneNumber": [
                 { "type": "home", "number": "212 555-1234" },
                 { "type": "fax", "number": "646 555-4567" }
             ]
        }
        jstring = json.dumps(d)
        self.assertEqual(load_pickle_as_json_string("files/contact_info.pkl"), jstring)

