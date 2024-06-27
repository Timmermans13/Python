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

### Overall
Old cov:

Francis:

![](https://github.com/Timmermans13/Python/blob/master/.images/pow-cov-res-old.png)
![](https://github.com/Timmermans13/Python/blob/master/.images/balance_parenthesis_old_cov_res.png)

New cov:

Francis:

![](https://github.com/Timmermans13/Python/blob/master/.images/pow-cov-res-new.png)
![](https://github.com/Timmermans13/Python/blob/master/.images/balance_parenthesis_new_cov_res.png)

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

Francis: I have made coverage measurements of two functions and 
I have addedone test case for each function to improve the coverage.



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

## Statement of individual contributions

Stan: I have made coverage measurements of two functions and 
I have added one test case for each function to improve the coverage.
