# Lab 2 - Mutation Testing
## Introduction
This repository contains a Python program for conducting mutation testing on a set of algorithms including quicksort and binary search. Mutation testing involves injecting errors into the original code and analyzing how well the test suite detects these injected errors.

## How to Run
1. Navigate to the Lab_2 directory in your terminal.
cd /path/to/Lab_2

2. Run the tester by executing the following command:
python lab2_tester.py

## Program Overview
The main testing script (lab2_tester.py) orchestrates the mutation testing process. The mutations are applied to the original quicksort and binary search algorithms, and various test scenarios are executed to evaluate the effectiveness of the test suite.

## Test Scenarios
### Random Tests:

- Random arrays are generated, and the test suite checks if the algorithms behave correctly with these inputs.
- Results include the average number of tests passed and the elapsed time.

### Pairwise Tests:
- Test cases are systematically created to cover various combinations of inputs.
- Results include the minimum number of tests executed until an error is found and the elapsed time.

## Mutations
Six different mutations are applied to the original code, and each mutation is tested separately to identify any introduced errors.

- Mutation 1: Mutating Quicksort Base Case
- Mutation 2: Mutate Pivot Selection
- Mutation 3: Mutate Binary Search Comparison
- Mutation 4: Mutate Binary Search Adjustment
- Mutation 5: Mutate Binary Search Exit Condition
- Mutation 6: Integration Error - Reverse Sorted Array

## Interpreting Results
- If the testing process finds no bugs, it prints "No bugs present."
- If bugs are found, it provides information on the number of bugs and additional details about each mutation's impact.

## Contributors
  [Egill Friðriksson]
  [egillf@kth.se]
