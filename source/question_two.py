"""Question two for an executable examination."""

from typing import Any, Callable, Iterator, Tuple, Union

# TODO: Answer all of the sub-questions inside of question_two.py

# TOOD: Answer each sub-question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output

# Question 2a. {{{

# Instructions:
# Repair the source code lines in this function
# so that it operates in the specified fashion.

# Function description:
# The function calculate_quadratic_equation_roots should:
# --> Compute the "roots" of a quadratic equation
# --> Return two roots even if they are the same number
# --> Perform the computation so that it accepts three inputs
#     that are of type float and returns the two roots as a float
# --> Return the root called x_one first and the root called x_two second
# --> Package both of the returned roots in a tuple using the notation (x_one, x_two)
# --> For instance,
#     -- the inputs of 1, 2, and 1 should return the output of (-1.0, -1.0)


def calculate_quadratic_equation_roots(a: float, b: float, c: float) -> Tuple[float, float]:
    """Calculate roots of quadratic equation."""
    D = (b * b - 4 * a * c) * 0.5
    x_one = (-b + D) / (2 ** a)
    x_two = (-b - D) / (2 ** a)
    return (x_two, x_one)


def question_two_a():
    """Run question two-a."""
    # Do not edit this function
    question_two_output_a = str(calculate_quadratic_equation_roots(1, 2, 1))
    return question_two_output_a

# }}}

# Question 2b. {{{

# Instructions:
# Provide an implementation of the following function so
# that it meets the following function description

# Function description:
# The function compute_fibonacci_with_generator should:
# --> Accept as input a variable called number of type int
# --> Incrementally compute and return the numbers in the fibonacci sequence
# --> Use a "generator function" approach to incrementally produce the values

# For instance, here are some input and output examples for these functions:
# Input: 5, Output: 1 1 2 3 5
# Input: 6, Output: 1 1 2 3 5 8

# Note that the function compute_fibonacci_with_generator will be provided
# as input to the create_iterator_values function and you do not need to
# revise in any way the create_iterator_values function


def compute_fibonacci_with_generator(number: int) -> Iterator[int]:
    """Compute the numbers in the fibonacci sequence using a generator."""
    yield number


def create_iterator_values(generator_to_call: Callable[[int], Iterator[int]], request_value: int) -> str:
    """Consume and prepare for display the values produced by a generator's iterator."""
    display_string = ""
    for value in generator_to_call(request_value):
        display_string = display_string + f"{value} "
    return display_string[:-1]


def question_two_b():
    """Run question two-b."""
    # Do not edit this function
    separator = " / "
    question_two_output_b = str(create_iterator_values(compute_fibonacci_with_generator, 5))
    question_two_output_b = question_two_output_b + separator + str(create_iterator_values(compute_fibonacci_with_generator, 6))
    question_two_output_b = question_two_output_b + separator + str(create_iterator_values(compute_fibonacci_with_generator, 10))
    return question_two_output_b

# }}}

# Question 2c. {{{

# Instructions:
# Implement functions to produce the requested output

# Function description:
# The function convert_to_str should:
# --> Accept as input a value of any data type
# --> Convert the value to the type of string (i.e., str)
# --> Return the converted value
# --> For instance, if the function receives 5 as
#     an input it returns the value of "5"

# Function description:
# The function determine_if_str should:
# --> Accept as input a value of any data type
# --> Determine whether or not the provided value is a string
# --> If the value is a string, it should return True
# --> Otherwise, it should return False
# --> For instance, if the function receives 5 as
#     an input it returns False
# --> For instance, if the function receives "5" as
#     an input it returns True

# TODO: Please note that the initial version of these two
# functions called convert_to_str and determine_if_str
# will cause this program to crash, most likely on the line
# with the comment on it that states "type: ignore".

# TODO: If you do not correctly fix the determine_if_str function
# this will cause this program to crash with a type check error
# and then potentially cause other checks for this question to fail


def convert_to_str(value: Any) -> str:
    """Convert the provided value to a string."""
    return ""


def determine_if_str(value) -> bool:
    """Determine whether or not a provided value is a string."""
    return True


def replay_value(value: Union[str, int], replay_count: int) -> Union[str, int]:
    """Replay a string or an int a specified number of times."""
    if determine_if_str(value):
        replayed_value = ""
        for _ in range(replay_count):
            replayed_value = replayed_value + value  # type: ignore
        return replayed_value
    else:
        replayed_value = ""
        value_as_string = convert_to_str(value)
        for _ in range(replay_count):
            replayed_value = replayed_value + value_as_string
        return replayed_value


def question_two_c():
    """Run question two-c."""
    # Do not edit this function
    space = " "
    question_two_output_c = str(replay_value(5, 5))
    question_two_output_c = question_two_output_c + space + str(replay_value("a", 5))
    question_two_output_c = question_two_output_c + space + str(replay_value(19, 5))
    question_two_output_c = question_two_output_c + space + str(replay_value("ab", 5))
    return question_two_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_two():
    """Run all of the subquestions in question two."""
    # call the function for question two-a
    output = question_two_a()
    print(output)
    # call the function for question two-b
    output = question_two_b()
    print(output)
    # call the function for question two-c
    output = question_two_c()
    print(output)


if __name__ == "__main__":
    run_question_two()
