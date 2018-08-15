# Lab 4
## Backtracking: Constraint Satisfaction Problem

<img src="https://img.shields.io/badge/language-Python3-brightgreen.svg"/>
<img src="https://img.shields.io/badge/VS Code-1.10.2-blue.svg"/>  

### Contents
* [Seating Arrangement](#seat)
___


## Seating Arrangement
There is a classroom which is in the form of a grid of size `m×n`. 

Post Effervescence the students of the classroom have developed some complicated friends and enemies. Either two students are friends or they are enemies. 

Before the Artificial Intelligence class, the students need to be seated. If two enemies sit next to each other, front and back, or diagonally opposite, there may emerge a fight, which will be very exciting for the class, but must be avoided. 

Your task is toprint such a seating arrangement.

### Input:
The first line has `t`, the number of test cases. 

Each test case has `m` and `n` as the first line of input.

Thereafter there are `m×n` lines of input. In each line the first string gives the roll number of the student,followed by an integer a indicating the number of friends that the student has, followed by `a` roll
numbers (string) of the friends of `a`. 

The inputs are given in ascending order.

### Output:
For each test case `m` rows of `n` roll numbers. If no arrangement is possible, print "`not
possible`"

### Problems:
1. Solve the problem using backtracking by filling up the grid in a row-major format of preference, and students preferred in the ascending order of roll numbers.
  
2. Solve the problem using backtracking and Minimum Remaining Values heuristic. In case of a
tie prefer the seats in a row-major format, and students preferred in the ascending order of roll
numbers.

3. Solve the problem using backtracking and Minimum Remaining Values heuristic. In case of a
tie use the degree heuristic. In case there is still a tie, prefer the seats in a row-major format, and
students preferred in the ascending order of roll numbers.

4. Solve the problem using backtracking and Minimum Remaining Values heuristic. In case of a
tie use the degree heuristic and least constraining value heuristic. In case there is still a tie, prefer
the seats in a row-major format, and students preferred in the ascending order of roll numbers.

5. Add arc consistency to the solution of question 4.

### Final solution:  
```
 python seating_arrangement.py
```
### Heuristics used:
* **Minimum Remaining Values(MRV):**<br>
Most constrained variable(student) is selected on the basis of the number of remaining seats.

* **Degree Heuristic:**<br>
The variable(student) that applies the most constraints on other variables will have the least number of friends.

* **Roll-No:**<br>
Students are selected based on the ascending order of roll numbers.