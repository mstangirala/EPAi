import math
import sys
import random
from decimal import Decimal


class Qualean:

    def __init__(self, number):
        if not number in [-1, 0, 1]:

            raise ValueError('Please provide either -1, 0 or 1')

    def __new__(cls, value):
        if value == 'TRUE':
            value = 1
        elif value == 'FALSE':
            value = 0
        elif value == 'MAYBE':
            value = -1
        return super(Qualean, cls).__new__(cls, value // (abs(value)
                or 1))

    def __repr__(self):
        if self > 0:
            return 'TRUE'
        elif self == 0:
            return 'FALSE'
        return 'MAYBE'

    def __str__(self):
        return repr(self)

    def __bool__(self):
        if self > 0:
            return True
        elif self == 0:
            return False
        else:
            raise ValueError("invalid literal for bool(): '%s'" % self)

    def __or__(self, other):
        if isinstance(other, Qualean):
            return _ttable[(self, other)][1]
        else:
            try:
                return _ttable[(self, Qualean(bool(other)))][1]
            except:
                return NotImplemented

    def __add__(self, other):
        decimal.getcontext().prec = 10
        if isinstance(other, Qualean):
            return self.number + other.number
        return NotImplemented

    def __and__(self, other):
        if isinstance(other, Qualean):
            return _ttable[(self, other)][0]
        else:
            try:
                return _ttable[(self, Qualean(bool(other)))][0]
            except:
                return NotImplemented

    def __mul__(self, other):
        decimal.getcontext().prec = 10
        if isinstance(other, Qualean):
            return self.number * other.number
        return NotImplemented

    def __sqrt__(self):
        if self == 0:
            return self
        elif self > 0:
            return self ** 0.5
        return -self ** 0.5

    def __invertsign__(self):
        return _ttable[self]

    def __gt__(self, other):
        if isinstance(other, Qualean):
            return self.number > other.number
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Qualean):
            return self.number >= other.number
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Qualean):
            return self.number < other.number
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Qualean):
            return self.number <= other.number
        return self

    def __float__(self):
        return float(self.number)

    def __eq__(self, other):
        if isinstance(other, Qualean):
            return self.number == other.number
        return NotImplemented

    def __getattr__(self, name):
        if name in ('_n', 'flip'):

      # So you can do x._n == x.flip; the inverse of x
      # In Python 'not' is strictly boolean so we can't write `not x`
      # Same applies to keywords 'and' and 'or'.

            return _ttable[self]
        else:
            raise AttributeError


(TRUE, FALSE, MAYBE) = (Qualean(1), Qualean(0), Qualean(-1))

_ttable = {  #    A: -> flip_A
             #     (A, B): -> (A_and_B, A_or_B, A_xor_B)
    TRUE: FALSE,
    FALSE: TRUE,
    MAYBE: MAYBE,
    (MAYBE, MAYBE): (MAYBE, MAYBE, MAYBE),
    (MAYBE, FALSE): (FALSE, MAYBE, MAYBE),
    (MAYBE, TRUE): (MAYBE, TRUE, MAYBE),
    (FALSE, MAYBE): (FALSE, MAYBE, MAYBE),
    (FALSE, FALSE): (FALSE, FALSE, FALSE),
    (FALSE, TRUE): (FALSE, TRUE, TRUE),
    (TRUE, MAYBE): (MAYBE, TRUE, MAYBE),
    (TRUE, FALSE): (FALSE, TRUE, TRUE),
    (TRUE, TRUE): (TRUE, TRUE, FALSE),
    }

values = ('FALSE', 'TRUE ', 'MAYBE')

print ("\nQualean logical inverse, '~'")
for a in values:
    expr = '~%s' % a
    print('  %s = %s' % (expr, eval(expr)))

for (op, ophelp) in (('&', 'and'), ('|', 'or'), ('^', 'exclusive-or')):
    print ("\nQualean logical %s, '%s'" % (ophelp, op))
    for a in values:
        for b in values:
            expr = '%s %s %s' % (a, op, b)
            print ('  %s = %s' % (expr, eval(expr)))