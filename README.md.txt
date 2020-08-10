To write a Qualean class by combining the aspects of Boolean and Quantum concepts. We can assign only 2 boolean values ...... True/False.
We need to include one more state ------- Maybe. 
We assign the values 1, 0 & -1 to True, False and Maybe.

(1) __and__ function: The "and" operator verifies and proceeds further if and only if all the conditions are true.
(2) __or__ function: The "or" operator verifies and proceeds further if any of the conditions is true.
(3) __repr__ function: This function is used to return the object as a string instead of a null value.
(4) __str__ function: This function is used to return any given value in the form of a string. 
(5) __add__ function: This method gives the sum of the given numbers.
(6) __eq__ function: This method is used to check the equality (==) of the conditions.
(7) __float__ function: It is a built-in Python function that converts a number or a string to a float value
(8) __ge__ function: This method checks if one condition is greater than or equal to the other.
(9) __gt__ function: This method checks if one condition is greater than  the other.
(10) __le__ function: This method checks if one condition is lesser than or equal to the other.
(11) __lt__ function: This method checks if one condition is lesser than  the other.
(12) __invertsign__ function: 
(13) __mul__ function: This function returns the product of the given inputs.
(14) __sqrt__ function: This function returns the square root of the given input.
(15) __bool__ function: This function returns the True or False value of a given condition.

Test Cases:

def test_readme_exists: To verify if a README file exists along with .py files.
def test_readme_contents: To verify if the README file contains more than 500 words.
def test_readme_proper_description: To verify if all the functionalities in session4.py file are covered.
def test_readme_file_for_formatting: To verify the formatting of README file.
def test_indentations: To check for any unwanted indents or spaces in the class/program
test_function_name_had_cap_letter: To check for any unwanted capital letters used in naming the functions.
def test_Qualean_float(): To verify if the repr function returns a float.
def test_Qualean_bool(): To verify if the bool function returns the state of the number whether TRUE, FALSE or MAYBE.
def test_Qualean_ge(): To verify if the greater than or equal to function evaluates the conditions.
def test_Qualean_gt(): To verify if the greater than function evaluates the conditions.
def test_Qualean_le(): To verify if the less than or equal to function evaluates the conditions.
def test_Qualean_lt(): To verify if the lesser than function evaluates the conditions.
def test_Qualean_sqrt(): To verify if the square root function returns the sqrt value of positive numbers and (-1).sqrt value for negative numbers.
def test_Qualean_invertsign(): To verify if the function changes the sign of the given number.
def test_Qualean_add(): To verify the numerical addition of the given numbers.
def test_Qualean_hundred(): To verify if the given number added a hundred times is equal to the number multiplied by 100.
