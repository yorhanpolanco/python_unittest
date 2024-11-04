# Instructions

1. Evaluate a given number from 0 to n
2. If it is divisible by both 3 and 5, return `fizzbuzz`.
3. If the number is divisible by 3, return `fizz`.
4. If the number is divisible by 5, return `buzz`.
5. If the number is 0, return the word `zero`.
6. Else, return the number

# Installation

Linux/MacOS

## pytest

```
$ python3 -m pip install pytest pytest-cache pytest-subtests pytest-pylint
```

# Executing Tests

From the root of the repo, run the following:

```
python3 -m pytest -o markers=task ./src/python/fizz_buzz/fizz_buzz_test.py
```
