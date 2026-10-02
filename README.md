# Algorithm Challenge

A small algorithm challenge I completed as part of a company admission process.

Although I wasn't accepted, I enjoyed solving the challenge and wanted to keep the algorithm and the experience in my GitHub repository rather than letting the work disappear.

# Challenge Description
The program processes multiple independent tests.

## 1. Enter the number of tests
First, enter how many tests you want to run.

For example:
```
3
```
>[!NOTE]
>The maximum number of tests is 100.

## 2. Enter the number of numbers for each test
For each test, enter how many numbers will be provided.

For example:
```
4
```
>[!NOTE]
>The maximum number of numbers in a test is 100.

## 3. Enter the numbers
Enter the specified amount of numbers, separated by spaces.

For example:
```
99 45 -34 -76
```
>[!NOTE]
>The accepted range for each number is from -100 to 100.

## 4. Repeat for each test
Continue entering the number of values and the values themselves until all tests have been completed.

## 5. Get the results
The program prints the result of each test separately.

If the number of values entered does not match the number specified for that test, the result is:
```
-1
```
# Calculation Rules
For every number:

- Positive numbers are ignored.

- Zero is ignored.

- Negative numbers are raised to the fourth power.

- If a test contains multiple negative numbers, their fourth powers are added together.

### For example:
```
-98 97
```
### The calculation is:
```
(-98)^4 = 92236816
97 → ignored
```
### Result:
```
92236816
```
### Another example:
```
99 45 -34 -76
```
### The calculation is:
```
99  → ignored
45  → ignored
(-34)^4 + (-76)^4
```
### Result:
```
34698512
```
### Example Input / Output
Example input:
```
3
2
-98 97
4
99 45 -34 -76
3
86 54
```
Example output:
```
92236816
34698512
-1
```
The third test returns -1 because 3 numbers were expected, but only 2 numbers were provided.

## Implementation Notes
This challenge was intentionally implemented without using:

- Lists

- Tuples

- Dictionaries

- Global variables

- for/while loop

- Generative AI

The goal was to solve the problem with different methods.

## Why I Keep This Repository
This project is not here because the application resulted in a job.

I applied because I wanted to challenge myself and test my algorithm skills. The challenge was fun to solve, and I decided that the solution itself was worth keeping.
