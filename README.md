# Report for Assignment 1

## Project chosen

Name: Python

URL: <https://github.com/geekcomputers/Python>

Number of lines of code and the tool used to count it: <31429>

![](https://github.com/Timmermans13/Python/blob/master/.images/NLOC.png)

Programming language: Python

## Coverage measurement

### Existing tool

<Coverage.py>

### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Francis>

BinaryExponentiation

<https://github.com/Timmermans13/Python/blob/master/power_of_n.py>

![](https://github.com/Timmermans13/Python/blob/master/pow-cov-old-instr.png)

is_balanced

<https://github.com/Timmermans13/Python/blob/master/balance_parenthesis.py>

![](https://github.com/Timmermans13/Python/blob/master/.images/balance_parenthesis_old_cov_inst.png)

<Tim>

linear search

<https://github.com/Timmermans13/Python/blob/master/linear search.py>

![](https://github.com/Timmermans13/Python/blob/master/linsearchold.png)

num-py

<https://github.com/Timmermans13/Python/blob/master/num-py.py>

![](https://github.com/Timmermans13/Python/blob/master/numpyold.png)

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Francis >

<Test 1: pow-test-one>

<https://github.com/Timmermans13/Python/blob/Francis-Branch/power_of_n.py>

![](https://github.com/Timmermans13/Python/blob/master/.images/pow-cov-instr-old.png)

![](https://github.com/Timmermans13/Python/blob/master/.images/pow-cov-instr-new.png)

<The test I have provided tests the with the branch where n is equal to 0 (pow-case-1). This was the only branch that was not covered, hence improving the branch coverage to 100%>

<Test 2: bal_case-two-test>

<https://github.com/Timmermans13/Python/blob/Francis-Branch/balance_parenthesis.py>

![](https://github.com/Timmermans13/Python/blob/master/.images/balance_parenthesis_old_cov_inst.png)

![](https://github.com/Timmermans13/Python/blob/master/.images/balance_parenthesis_new_cov_inst.png)

<The test I have provided tests the with the branch where the string empty (bal-case-2). This was the only branch that was not covered, hence improving the branch coverage to 100%>

<Tim>

<Test 1: linear search>

<https://github.com/Timmermans13/Python/blob/master/linear search.py>

![](https://github.com/Timmermans13/Python/blob/master/linsearchold.png)

![](https://github.com/Timmermans13/Python/blob/master/linsearchnew.png)

<The test I have provided tests the function when the letter is not in the array. For this I chose the letter Z. with makeing the new secont test the branch coverage is improved to 100%>

<Test 2: num-py>

<https://github.com/Timmermans13/Python/blob/master/num-py.py>

![](https://github.com/Timmermans13/Python/blob/master/numpyold.png)

![](https://github.com/Timmermans13/Python/blob/master/numpynew.png)

<The test I have provided tests the function when the array is not equal that means both the print statements get hit and the coverage is 100%>

<Connor>

Pre-test coverage

![](old_cov.png)

Pre-test branches

![](old_branches.png)

Post-test coverage

![](new_cov.png)

Post-test branches

![](new_branches.png)

Code added: track.py, test.py
Code modified: pongpong.py, ball.py, paddle.py

### Overall

Old cov:

Francis:

![](https://github.com/Timmermans13/Python/blob/master/.images/pow-cov-res-old.png)
![](https://github.com/Timmermans13/Python/blob/master/.images/balance_parenthesis_old_cov_res.png)

Tim:

![](https://github.com/Timmermans13/Python/blob/master/oldstatlin.png)
![](https://github.com/Timmermans13/Python/blob/master/oldstatnum.png)

New cov:

Francis:

![](https://github.com/Timmermans13/Python/blob/master/.images/pow-cov-res-new.png)
![](https://github.com/Timmermans13/Python/blob/master/.images/balance_parenthesis_new_cov_res.png)

Tim:

![](https://github.com/Timmermans13/Python/blob/master/newstatlin.png)
![](https://github.com/Timmermans13/Python/blob/master/newstatnum.png)

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

Francis: I have made coverage measurements of two functions and
I have addedone test case for each function to improve the coverage.

Tim: I have done the coverage measurements of two functio and added test cases for the improvement of the coverage.

## Stan

Test 1: industrial_developed_hangman

Pre-test coverage

![](https://raw.githubusercontent.com/Timmermans13/Python/stan/Industrial_developed_hangman/cov_before.png)

Pre-test function branches that were hit

![](https://raw.githubusercontent.com/Timmermans13/Python/stan/Industrial_developed_hangman/testres_before.png)

Post-test branches hit

![](https://raw.githubusercontent.com/Timmermans13/Python/stan/Industrial_developed_hangman/testres_after.png)

Post-test coverage

![](https://raw.githubusercontent.com/Timmermans13/Python/stan/Industrial_developed_hangman/cov_after.png)

Test 2: TIC_TAC_TOE

Pre-test coverage
![](https://raw.githubusercontent.com/Timmermans13/Python/master/TIC_TAC_TOE/coverage%20before.png)

Pre-test function branches that were hit
![](https://raw.githubusercontent.com/Timmermans13/Python/master/TIC_TAC_TOE/branch_coverage_before_test.png)

Post-test branches that were hit
![](https://raw.githubusercontent.com/Timmermans13/Python/master/TIC_TAC_TOE/branch_coverage_after_test.png)

Post-test coverage
![](https://raw.githubusercontent.com/Timmermans13/Python/master/TIC_TAC_TOE/overage%20after%20test.png.)

## Statement of individual contributions

Stan: I have made coverage measurements of two functions and
I have added one test case for each function to improve the coverage.
