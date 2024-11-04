# Instructions

Simulate a bank account supporting opening/closing, withdrawals, and deposits of money.
Watch out for concurrent transactions!

A bank account can be accessed in multiple ways.
Clients can make deposits and withdrawals using the internet, mobile phones, etc.
Shops can charge against the account.

Create an account that can be accessed from multiple threads/processes (terminology depends on your programming language).

It should be possible to close an account; operations against a closed account must fail.

`Borrowed from exercism.io`

# Installation

Linux/MacOS

## pytest

```
$ python3 -m pip install pytest pytest-cache pytest-subtests pytest-pylint
```

# Executing Tests

From the root of the repo, run the following:

```
python3 -m pytest -o markers=task ./src/python/bank_account/bank_account_test.py
```
