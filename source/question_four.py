"""Question four for an executable examination."""

from typing import Callable
from typing import List
from typing import Tuple

# TODO: Answer all of the sub-questions inside of question_four.py

# TOOD: Answer each sub-question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output

# Question 4a. {{{

# Instructions:
# Repair the instructions in these functions
# so that they operate in the specified fashion

# Function description:

# The function plus should:
# --> Accept as input two int values called number_one and number_two
#     and add those two numbers together and return their sum

# The higher-order function called reduce should:
# --> Accept as input a callable function that accepts two ints and returns an int as output
# --> Accept as input a list of int values called sequence
# --> Accept as input a starting point for an iterative process of applying the callable function

# For instance, here are some examples of the input and output for this function:
# Input: plus, [1, 2, 3, 4], 0
# Output: 10
# Justification:
# --> The function starts the result at the initial value of 0
# --> Then the function uses plus for the running result that starts at 0
#     and stores the value of using plus with the current value of result and the current value
#     as it iterates through the provided sequence of int values
# --> After incrementally calling plus for every value inside of the input list
#     it will return the computed result of 10
# --> Ultimately, it performs the following addition:
#     0 + 1 + 2 + 3 + 4 = 10
# --> Notably, it starts the application of the plus function with the values of 0 and 1
#     which will result in the output of 1 that is used in the next iterative applications of plus


def plus(number_one: int, number_two: int) -> int:
    """Perform the addition of the two provided numbers."""
    return number_one + number_two


def reduce(function_to_call: Callable[[int, int], int], sequence: List[int], initial: int) -> int:
    """Apply a function to a sequence of values with the additional input as a starting point."""
    result = 0
    for value in sequence:
        result = function_to_call(result, value)
    return function_to_call(initial, initial)


def question_four_a():
    """Run question four-a."""
    # Do not edit this function
    separator = " / "
    question_four_output_a = str(reduce(plus, [1, 2, 3, 4], 0))
    question_four_output_a = question_four_output_a + separator + str(reduce(plus, [1, 2, 3, 4], 1))
    question_four_output_a = question_four_output_a + separator + str(reduce(plus, [1, 2, 3, 4], 2))
    return question_four_output_a

# }}}

# Question 4b. {{{

# Instructions:
# Provide an implementation of the following function
# so that it behaves in the fashion described below

# Function description:
# The function is_factor should:
# --> Intuitively, answer the question "is the value of input_one a factor of input_two"?
# --> Or, ask the question as "does the value of input_one evenly divide input_two with a remainder of 0?"
# --> It must accept as input two int values called input_one and input_two
# --> It must determine whether or not input_two is evenly divided by input_one, which would
#     then mean that it should return True to indicate that input_one is a factor of input_two
# --> For instance, if input_two is equal to 10 and input_one is
#     equal to 5 then this function would return True
# --> Alternatively, if value_one is equal to 3 and value_two is
#     equal to 10 then this function would return False


def is_factor(input_one: int, input_two: int) -> bool:
    """Determine whether or not input variable a is a factor of input variable b."""
    return False


def question_four_b():
    """Run question four-b."""
    # Do not edit this function
    space = " "
    question_four_output_b = str(is_factor(2, 10))
    question_four_output_b = question_four_output_b + space + str(is_factor(3, 10))
    question_four_output_b = question_four_output_b + space + str(is_factor(3, 9))
    return question_four_output_b

# }}}

# Question 4c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function exponentiate_and_add_list should:
# --> Accept as input a list of int values
# --> For each value (called current_value) in the list, take these steps:
#     1) perform the computation of current_value to the power of the value in the power variable
#     2) add the result of the computation stated in the previous step to the running total
# --> Produce as output a tuple of values that follows this format:
#     (the input list of int values, the power to which the input list's values should be raised, the final total)
# --> For instance, the function would produce the following outputs for the given inputs:
#     Inputs: List: [1, 10], Power: 1
#     Output: ([1, 10], 1, 11)
#     Explanation: 1^1 + 10^1 = 11
#                  The input list is [1, 10]
#                  The input value of power is 1
#     Note: the notation 1^1 means "1 to the power of 1"
#     Note: the aforementioned notation is not what you would use to
#     perform exponentiation in the Python programming language


def exponentiate_and_add_list(input_list: List[int], power: int) -> Tuple[List[int], int, int]:
    """Exponentiate all of the int values in a list to a given power and then add each result together."""
    return ([0], 0, 0)


def question_four_c():
    """Run question four-c."""
    # Do not edit this function
    space = " "
    question_four_output_c = str(exponentiate_and_add_list([1, 10], 1))
    question_four_output_c = question_four_output_c + space + str(exponentiate_and_add_list([2, 10, 1], 1))
    question_four_output_c = question_four_output_c + space + str(exponentiate_and_add_list([3, 10], 2))
    return question_four_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_four():
    """Run all of the subquestions in question four."""
    # call the function for question four-a
    output = question_four_a()
    print(output)
    # call the function for question four-b
    output = question_four_b()
    print(output)
    # call the function for question four-c
    output = question_four_c()
    print(output)


if __name__ == "__main__":
    run_question_four()
