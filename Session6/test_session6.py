import pytest
import random
import string
import session6
import os
import inspect
import re
import math
from math import isclose



README_CONTENT_CHECK_FOR = [
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'jack',
    'queen',
    'king',
	'ace',
	'spades',
	'clubs',
	'hearts',
	'diamonds',
    'poker',
    'flush',
    'straight',
    'pair',
    'royal',
    'hand',
    'cards',
    'full House',
    'lambda',
    'zip',
    'map'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    #readme_words = [word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 400, "Make your README.md file interesting! Add atleast 400 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
        
def test_docstrings_function():
	"""
	Test case to see if docstrings are used
	"""
	functions = inspect.getmembers(session6, inspect.isfunction)
	for func in functions:
		assert func[1].__doc__
        
def test_function_annotations():
    """
    Test case to if annotations are used
    """
    functions = inspect.getmembers(session6, inspect.isfunction)
    for func in functions:
        assert func[1].__annotations__
