"""Question three for an executable examination."""

from typing import List
from typing import Tuple


# Question 3a. {{{

# Instructions:
# Implement a function so that it operates in the specified fashion

# Function description:
# The function compute_mean should:
# --> Accept as input a list of int values and produce a float that
#     is the arithmetic mean (i.e., the average) of the values
# --> Determine how many values are in the provided input list
# --> Return a tuple that contains two values of the following format:
#     (The arithmetic mean of the input values, the number of input values)
# --> The following examples illustrate the inputs and outputs of this function:
#     Input: [0, 0, 0]
#     Output: (0.0, 3)
#     Input: [1, 1, 1, 1]
#     Output: (1.0, 4)
# Note that you may implement any appropriate approach for computing the
# arithmetic mean (even by using functions built-in to the Python language)


def compute_mean(numbers: List[int]) -> Tuple[float, int]:
    """Compute the mean of a list of int numbers and return it as a float along with the length of the list."""
    return (0.0, 0)


def question_three_a():
    """Run question three-a."""
    # Do not edit this function
    separator = " / "
    question_two_output_a = str((compute_mean([1, 1, 1, 1])))
    question_two_output_a = question_two_output_a + separator + str((compute_mean([0, 0, 0])))
    question_two_output_a = question_two_output_a + separator + str((compute_mean([10, 10, 7, 7])))
    question_two_output_a = question_two_output_a + separator + str((compute_mean([1, 2, 3, 4])))
    question_two_output_a = question_two_output_a + separator + str((compute_mean([1, 2, 3, 4, 0])))
    return question_two_output_a

# }}}

# Question 3b. {{{

# Instructions:
# Implement the following function so that it performs the specified behavior

# Function description:
# The function convert_list should:
# --> Accept as input a variable called input_list that contains a list of strings
# --> Use a for loop or a while loop to iterate through each element in the input_list
# --> Convert each value in the input_list from a string to an int
# --> Return a list of all the converted int values
# --> For instance, when the function receives the input ['5', '7', '9', '11']
#     if will produce the output [5, 7, 9, 11]


def convert_list(input_list: List[str]) -> List[int]:
    """Convert a list of strings to a list of int values."""
    return [0]


def question_three_b():
    """Run question three-b."""
    # Do not edit this function
    question_tree_output_b = convert_list(['19', '2', '19', '2'])
    return question_tree_output_b

# }}}

# Question 3c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function create_unique_list should:
# --> Accept as input a list of int values
# --> Create a list out of the list of int values, ensuring
#     that the created list does not contain any duplicate values
# --> Compute the difference in size between the input list
#     and the unique list that was created from the input list
# --> Return a tuple of data of the following format:
#     (the list derived from the input list, the computed difference in sizes between the lists)

# --> For instance, if the function receives [5, 7, 9, 11] as
#     an input it returns ([5, 7, 9, 11], 0) as the output

# --> For instance, if the function receives [0, 0, 0] as
#     an input it returns ([0], 2) as the output

# Note that as you consider how to implement create_unique_list you may
# want to explore the use of a set discrete structure. However, if you
# adopt this approach you need to remember that, while a set ensures that its
# values are unique it also does not guarantee a predictable ordering of its values.
# You need to make sure that your implementations produces output that exactly
# matches what is required for this question, specifically ensuring order of values


def create_unique_list(input_list: List[int]) -> Tuple[List[int], int]:
    """Create a set-like list of int values out of a list of int values."""
    return []


def question_three_c():
    """Run question three-c."""
    # Do not edit this function
    separator = " / "
    question_three_output_c = str(create_unique_list([5, 7, 9, 11]))
    question_three_output_c = question_three_output_c + separator + str((create_unique_list([0, 0, 0])))
    question_three_output_c = question_three_output_c + separator + str((create_unique_list([1, 1, 1])))
    question_three_output_c = question_three_output_c + separator + str((create_unique_list([2, -2, 2])))
    return question_three_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_three():
    """Run all of the subquestions in question three."""
    # call the function for question three-a
    output = question_three_a()
    print(output)
    # call the function for question three-b
    output = question_three_b()
    print(output)
    # call the function for question three-c
    output = question_three_c()
    print(output)


if __name__ == "__main__":
    run_question_three()
