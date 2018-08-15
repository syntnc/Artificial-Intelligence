# Lab 5
## Searching

<img src="https://img.shields.io/badge/language-Python3-brightgreen.svg"/>
<img src="https://img.shields.io/badge/VS Code-1.10.2-blue.svg"/>  

### Contents
* [Gem Finding](#gem)
* [Sliding Board](#slide)
___


## Gem Finding
Consider a grid map of size `m × n`. 

The origin (0, 0) is taken as the top-left corner. The X axis is the vertical axis, the Y axis is the horizontal axis. A cell 0 denotes obstacle-free region, -1 denotes obstacles, and 1 denotes a gem. 

*Given a source, the aim of the agent is to go to the gem.*

The step cost is the time. The agent moves 1 block distance per second (or √2 time for diagonal moves). The order of preference of actions is: E, SE, S, SW, W, NW, N, NE, where N, E, S, W stand for North, East, South and West respectively. 

The priority queue should be implemented such that, in case of a tie, a node that is inserted first should be removed first. Print the path from the source to the gem.

Print only -1 if no path exists.

### Input:
The input is `t`, the number of test cases, followed by (for every test case) `m` and `n`. 

The next `m` lines of `n` integers each denote the grid map. The next line contains the source indicated by two integers `Sx` `Sy`.

### Output:
The output is the path.

### Problems:
1. Solve the problem using a flat `m x n` map.
   ```
    python find_gem.py < input/Q1_input.txt
   ```
  
2. Solve (1) with the difference that the map is circular in both X and Y axis, and moving right of the last column places the robot on the 1st column, and similarly with the rows.
   ```
    python find_gem_circular.py < input/Q2_input.txt
   ```

3. Solve (1) with the constraint that the robot can only move in the direction in which it is facing. If the robot wants to change its direction, it must invoke the action turn, which turns the robot by 45 degrees clockwise or anticlockwise. <br>The turning action has a cost of 5. <br>The robot is initially facing positive the Y axis (looking E).
   ```
    python find_gem_turn.py < input/Q3_input.txt
   ```

4. Solve (1) to find the path to the gem using iterative lengthening.
   ```
    python find_gem_iterative.py < input/Q4_input.txt
   ```
___

## Sliding Board
Consider a `n × n` size board (1 ≤ `n` ≤ 10), wherein every cell has a number written on it. 

The rows and columns are cyclic. So you can slide any row/column any number of blocks or any number of times.

As an example in the board given below, we slide the middle row one block each repeatedly, and the results are given in the following figures.

| Initial | Move 1 | Move 2 | Move 3 |
|-|-|-|-|
| <pre>4   8   5<br>2   6   13<br>1   10  18</pre> | <pre>4   8   5<br>13  2   6<br>1   10  18</pre> | <pre>4   8   5<br>6   13  2<br>1   10  18</pre> | <pre>4   8   5<br>2   6   13<br>1   10  18</pre> |

A unit move in this game is sliding any 1 row (or 1 one column) any number of times. So the motions made above is one single move of the game. 

Given a source configuration and a goal configuration, print the moves that result in the goal configuration from a source configuration using Iterative Deepening. 

* **Primary criterion:** Moving rows is preferred to moving columns  
* **Secondary criterion:** An earlier row/column is preferred to a later one
* **Tertiary criterion:** Sliding lesser rightward/downward is preferred to sliding more

### Input:
The first line of input is `t`, the number of test cases. 

For every test case, the first line of input is `n`, the size of the game. <br>The next `n` lines with `n` integers each is the source configuration. <br>The next `n` lines with `n` integers each is the goal configuration.

### Output:
The output is variable number of lines, each line indicating the board configuration of a move printed in a row major format.

```
 python sliding_board.py < input/Q5_input.txt
```

**Note:** *Compare each output with the corresponding output files in `output` directory.*