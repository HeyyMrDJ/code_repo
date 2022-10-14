# Getting Started
**Overwrite the file named words.txt in the root directory**

## Refactored using tips suggested
**Using the tips suggested (listed below) I was able to refactor and reduce the script down to 8 lines of code and a 115% increase in speed of execution**

Suggestions:
- Using sets to eliminate repeated characters
- Perform logic when reading line by line instead of dumping data into lists. 
```
python3 ./app1/refactor.py
The longest word without repeated characters: agile
```
## My original script
This is my original script with minimal changes for a working script
```
python3 main.py
agile
```


## Slightly refactored
This is my slightly refactored version using the same thought process as my original, but provides cleaner and more testable code
```
python3 ./app1/new_main.py
The longest word is: agile
```
## Nox output (testing, linting, etc)
```
collected 5 items                                                                                                                                           

tests/new_main_test.py::test_check_longest PASSED     [ 20%]
tests/new_main_test.py::test_check_repeating PASSED   [ 40%]
tests/new_main_test.py::test_format_lines PASSED      [ 60%]
tests/new_main_test.py::test_check_contents PASSED    [ 80%]
tests/new_main_test.py::test_main PASSED              [100%]

====== 5 passed in 0.03s ============================
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
app1/__init__.py             0      0   100%
app1/new_main.py            38      1    97%   61
app1/refactor.py             0      0   100%
tests/__init__.py            0      0   100%
tests/new_main_test.py      42      0   100%
tests/test_refactor.py       0      0   100%
------------------------------------------------------
TOTAL                       80      1    99%
nox > Session coverage was successful.
nox > Ran multiple sessions:
nox > * pytest: success
nox > * lint: success
nox > * flake8: success
nox > * black: success
nox > * coverage: success
