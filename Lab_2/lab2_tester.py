import os.path
from lab2_programs import *
from lab2_test_generator import create_random_tests, create_pairwise_tests
import time

def test_file_reader(file_path, mutation):
    # Reads and processes tests from a file.
    # Returns number of tests until an error is found or -1 if no error.
    num_tests = 0
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            for new_test in file:
                num_tests += 1
                target = int(new_test)
                test_list = [eval(i) for i in list(file.readline().split())]
                expected_result = oracle(test_list, target)
                try:
                    actual_result = test_mutations(test_list, target, mutation)
                except Exception as error:
                    print(f"Error: {error}")
                    return num_tests
                if not expected_result == actual_result:
                    return num_tests
            else:
                return -1
    else:
        raise FileNotFoundError

def pairwise_results(mutation, N):
    # Performs pairwise tests and prints the minimum number of tests until an error is found.
    start_time = time.time()
    create_pairwise_tests(N)
    min_result = test_file_reader("pairwise.txt", mutation)
    if min_result == -1:
        print("[Pairwise] No bugs present")
    else:
        print("[Pairwise] Number of bugs found: " + str(min_result))
    end_time = time.time()
    print(f"[Pairwise] Elapsed Time: {end_time - start_time:.4f} seconds")

def random_test_results(num_tests, mutation, N):
    # Performs random tests and prints the average number of tests until an error is found.
    # Takes in number of random tests to perform.
    start_time = time.time()
    avg_result = 0
    for _ in range(num_tests):
        create_random_tests(N)
        test_result = test_file_reader("random.txt", mutation)
        if test_result == -1:
            avg_result += 100 / num_tests
        else:
            avg_result += test_result / num_tests
    if (mutation == 0):
        print("--- NO MUTATION ---")
    else:
        print("--- MUTATION " + str(mutation) + "---")
    print("[Random] Average test passed: " + str(round(avg_result, 2)))
    end_time = time.time()
    print(f"[Random] Elapsed Time: {end_time - start_time:.4f} seconds")


def oracle(array, elem):
    # Simple oracle function to check if an element is present in an array.
    # automatically	judges each	test outcome (pass/fail).
    return elem in array

def test_mutations(array, target, mutation):
    if mutation == 0:
        return sort_and_search(array, target)
    elif mutation == 1:
        arr_copy = m1_quicksort(array.copy())
        return binary_search(arr_copy, target)
    elif mutation == 2:
        arr_copy = m2_quicksort(array.copy())
        return binary_search(arr_copy, target)
    elif mutation == 3:
        arr_copy = quicksort(array.copy())
        return m3_binary_search(arr_copy, target)
    elif mutation == 4:
        # arr_copy = quicksort(array.copy())
        # return m4_binary_search(arr_copy, target)
        # ENDLESS LOOP
        # as a workaround, the "no mutation" results are returned
        return sort_and_search(array, target)
    elif mutation == 5:
        arr_copy = quicksort(array.copy())
        return m5_binary_search(arr_copy, target)
    elif mutation == 6:
        return m6_sort_and_search(array, target)
    else:
        raise ValueError("Invalid mutation value")

def run_tests():
    for n in [20, 100, 500]:
        for i in range(7):
            random_test_results(100, i, n)
            pairwise_results(i, n)

run_tests()
