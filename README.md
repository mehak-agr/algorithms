# Algorithms
Given below are some of the many interesting problems out there on multiple competitive sites along with their algorithmic and code solutions.

Question 1:\
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land).\
A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.\
Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.\

Answer:\
Algorithm \
Step 1: Initialize a list of zeroes for keeping track of visited squares.\
Step 2: Iterate over the 2 * n edge squares. For each square \
  Case 1: Water square\
    Ignore.\
  Case 2: Land square is visited \
    Ignore.\
  Case 3: Land square is not visited\
    Perform a breadth first search, marking each new square as visited.\
Step 3: Subtract the sum of squares of A (Total number of land squares) and B (Total number of visited Land squares) to get the final answer.\

Question 2:\
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.\

Answer:\

