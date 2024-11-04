# Attune Interview

## NodeJS

Visit the following to install NodeJS

https://github.com/nvm-sh/nvm

## Run the following to install the dependencies

`npm install --include=dev`

### Executing Tests

From the root of the repo, run the following:

`npm run hello_world`

`npm run fizz_buzz`

`npm run bank_account`

## Python

### pytest

```
$ python3 -m pip install pytest pytest-cache pytest-subtests pytest-pylint
```

### Executing Tests

From the root of the repo, run the following:

`python3 -m pytest -o markers=task ./src/python/hello_world/hello_world_test.py`

`python3 -m pytest -o markers=task ./src/python/fizz_buzz/fizz_buzz_test.py`

`python3 -m pytest -o markers=task ./src/python/bank_account/bank_account_test.py`
