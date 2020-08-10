import pytest
import random
import string
import session4
import os
import inspect
import re
import math
from decimal import Decimal
from numbers import Real

README_CONTENT_CHECK_FOR = [
    'qualean',
    'isclose',
    'float',
    'eq',
    'add',
    'eq',
    'invertsign',
    'ValueError',
    'math',
    'isclose',
    'repr',
    'sqrt',
    'str',
    'bool',
    'mul',
    'and',
    'or',
    'lt',
    'le'
    'error',
    'gt',
    'ge'
]



def test_readme_exists():
  assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
  readme = open("README.md", "r")
  readme_words = readme.read().split()
  readme.close()
  assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
  READMELOOKSGOOD = True
  f = open("README.md", "r")
  content = f.read()
  f.close()
  for c in README_CONTENT_CHECK_FOR:
    if c not in content:
      READMELOOKSGOOD = False
      pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
  f = open("README.md", "r")
  content = f.read()
  f.close()
  assert content.count("#") >= 10

def test_indentations():
  ''' Returns pass if used four spaces for each level of syntactically \
  significant indenting.'''
  lines = inspect.getsource(session4)
  spaces = re.findall('\n +.', lines)
  for space in spaces:
    assert len(space) % 4 == 2, "Your script contains misplaced indentations"
    assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
  functions = inspect.getmembers(session4, inspect.isfunction)
  for function in functions:
    assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_Qualean_float():
  q = session4.Qualean(1)
  assert q.__repr__() == float(q)


def test_Qualean_bool():
  q = session4.Qualean(1)
  assert q.__bool__() == bool(q)

def test_Qualean_ge():
  q1 = session4.Qualean(1)
  q2 = session4.Qualean(0)
  assert (q1__ge__(q2)) == (q1.number % q2.number >= 0)

def test_Qualean_gt():
  q1 = session4.Qualean(1)
  q2 = session4.Qualean(0)
  assert (q1__ge__(q2)) == (q1.number % q2.number > 0)

def test_Qualean_lt():
  q1 = session4.Qualean(1)
  q2 = session4.Qualean(0)
  assert (q1__ge__(q2)) == (q1.number % q2.number < 0)

def test_Qualean_le():
  q1 = session4.Qualean(1)
  q2 = session4.Qualean(0)
  assert (q1__ge__(q2)) == (q1.number % q2.number <= 0)

def test_Qualean_sqrt():
  q = abs(session4.Qualean(1))
  assert __sqrt__q() == q.number**0.5

def test_Qualean_invertsign():
  q = session4.Qualean(1)
  assert __invertsign__q() == -(q.number)

def test_Qualean_add():
  q1 = session4.Qualean(1)
  q2 = session4.Qualean(0)
  assert (q1__add__(q2)) == (q1.number + q2.number)

def test_Qualean_and():
  q1 = session4.Qualean(1)
  q2 = session4.Qualean(0)
  assert (q1__and__(q2)) == bool(q1.number and q2.number)

def test_Qualean_mul():
  q1 = session4.Qualean(1)
  q2 = session4.Qualean(0)
  assert (q1__mul__(q2)) == q1.number*q2.number

def test_Qualean_hundred():
  num = 0
  q = session4.Qualean(1)
  while q < 100:
    num += q
  assert num = q.number*100


def test_Qualean_repr():
  q = session4.Qualean(1)
  assert q.__repr__() == f'Qualean Number({q.number})'

def test_Qualean_str():
  q = session4.Qualean(1)
  assert q.__str__() == f'value({q.number})'
