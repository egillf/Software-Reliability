import numpy as np
import random

# Function to create random tests
def create_random_tests(N):
    with open("random.txt", "w") as f:
        num_elements = 0
        for num_tests in range(100):
            # Generate a random list of integers between -500 and 500
            rand_list = np.random.randint(-500, 500, N).tolist()

            # Determine the target element based on whether num_tests is even or odd
            if num_tests % 2 == 0:
                i = np.random.randint(0, N)
                target = rand_list[i]
            else:
                target = np.random.randint(-750, 750)

            # Check if the target element is in the generated list
            if target in rand_list:
                num_elements += 1

            # Write the target and the random list to the file
            f.write(str(target) + "\n")
            f.write(" ".join(map(str, rand_list)) + "\n")

# Function to create pairwise tests
def create_pairwise_tests(N):
    with open("pairwise.txt", "w") as f:
        random.seed(96)

        # Example lists for pairwise testing
        example_lists = [
            np.random.randint(-500, 500, N).tolist(),  # Random list from -500 to 500
            list(range(-10, 10)),  # List -10 to 10, increment by 1
            [50 * x for x in range(-10, 10)],  # List -500 to 500, increment by 50
            [-x for x in range(-10, 10)],  # List 10 to -10, increment by 1
            [x * 50 for x in range(10, -11, -1)],  # List 500 to -500, increment by 50
            [50 * x for x in range(-10, 10, 2)] * 2,  # List -500 to 400, twice (10 total values)
            [0] * N,  # List of only zeroes
            [500] * N,  # List of only 500s
            [-500] * N,  # List of only -500s
        ]

        # Values to be used as test cases
        test_values = [-1000, -500, -10, -1, 0, 10, 14, 500, 501]

        # Iterate through test values and example lists, writing them to the file
        for values in test_values:
            for array in example_lists:
                f.write(str(values) + "\n")
                f.write(" ".join(map(str, array)) + "\n")
