"""Question five for an executable examination."""

from typing import List
from typing import Tuple

# TODO: Answer all of the sub-questions inside of question_five.py

# TOOD: Answer each sub-question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output

# Question 5a. {{{

# Instructions:
# Implement the requested function so that it operates in the specified fashion

# Function description:
# The function perform_subtraction should:
# --> Accept as input two floating-point values called input_one and input_two
# --> Subtract the value of the second input value from the first input value
# --> It should work correctly regardless of whether the numbers are positive or negative
# --> It should always perform the computation with floating point values, not integer values
# --> The following examples illustrate how this function should work:
#     Input: 1.0 and 1.0
#     Output: 0.0
#     Input: 2.0 and -2.0
#     Output: 4.0


def perform_subtraction(input_one: float, input_two: float) -> float:
    """Subtract the value stored in the second input from the value in the first input."""
    return 0


def question_five_a():
    """Run question five-a."""
    # Do not edit this function
    space = " "
    question_five_output_a = str(perform_subtraction(1.0, 1.0))
    question_five_output_a = question_five_output_a + space + str(perform_subtraction(2.0, -2.0))
    question_five_output_a = question_five_output_a + space + str(perform_subtraction(0.0, 2.0))
    return question_five_output_a


# }}}

# Question 5b. {{{

# Instructions:
# Implement the following function
# so that it behaves according to the function description

# Function description:
# The function get_maximum should:
# --> Accept as input two int values called input_one and input_two
# --> If the value in input_one is greater than or equal to input_two
#     then the function should return the value of input_one
# --> Otherwise, it should return the value of input_two

# Instructions:
# Implement the following function
# so that it behaves according to the function description

# Function description:
# The function create_tuple_of_value should:
# --> Accept as input a single int value
# --> Create a singleton tuple that contains the provided value
# --> Return the singleton tuple that contains the provided value

# For instance, here is an example that illustrates how to use these functions:
# Function calls: create_tuple_of_value(get_maximum(2, 10))
# Output: (10,)


def get_maximum(input_one: int, input_two: int) -> int:
    """Return the maximum value of two input values."""
    return input_two


def create_tuple_of_value(input_one: int) -> Tuple[int]:
    """Create a singleton list that contains the specified value."""
    return (0)


def question_five_b():
    """Run question five-b."""
    # Do not edit this function
    separator = " / "
    question_five_output_b = str(create_tuple_of_value(get_maximum(2, 10)))
    question_five_output_b = question_five_output_b + separator + str(create_tuple_of_value(get_maximum(9, 3)))
    question_five_output_b = question_five_output_b + separator + str(create_tuple_of_value(get_maximum(3, 3)))
    return question_five_output_b

# }}}

# Question 5c. {{{

# Instructions:
# Fix the defect(s) in the following function called get_minimum
# Implement the required functionality in the function called duplicate

# Function description for get_minimum:
# The function get_minimum should:
# --> Accept as input two int values called input_one and input_two
# --> If the value in input_one is less than or equal to input_two
#     then the function should return the value of input_one
# --> Otherwise, it should return the value of input_two

# Function description for duplicate:
# The function duplicate should:
# --> Accept as input an integer value and a duplicate count
# --> Create as output a list of integer values that contains the input number
#     that has been duplicated the specified number of times

# For instance, here are some examples of function calls and their output:
# Function calls: duplicate(get_minimum(12, 10), 5)
# Output: [10, 10, 10, 10, 10]


def get_minimum(input_one: int, input_two: int) -> int:
    """Return the minimum value of two input values."""
    if input_one < input_two:
        return input_one
    return input_two


def duplicate(input_one: int, duplicate_count: int) -> List[int]:
    """Duplicate the specified value the specified number of times."""
    return []


def question_five_c():
    """Run question five-b."""
    # Do not edit this function
    separator = " / "
    question_five_output_b = str(duplicate(get_minimum(12, 10), 5))
    question_five_output_b = question_five_output_b + separator + str(duplicate(get_minimum(3, 9), 5))
    question_five_output_b = question_five_output_b + separator + str(duplicate(get_minimum(2, 2), 5))
    return question_five_output_b

# }}}

# Do not edit any of the source code below this line


def run_question_five():
    """Run all of the subquestions in question five."""
    # call the function for question five-a
    output = question_five_a()
    print(output)
    # call the function for question five-b
    output = question_five_b()
    print(output)
    # call the function for question five-c
    output = question_five_c()
    print(output)


if __name__ == "__main__":
    run_question_five()
