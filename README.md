# 15-puzzle-solver
Solver for the classic 15 puzzle game (4x4 number game)

Algorithm used is BFS.
Data structures to improve speed:
Python set() data structure (hash table, O(1) lookup time on average)
Python deque() data structure (queue, popleft() function is O(1) versus O(n) for python list)

Instructions to Run:
Choose or create test cases at bottom of experiment_15puzzle.py, for example: Test_Case_1 = [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 12], [13, 14, 11, 15]]
Call solve method, for example: solver_object.solve(Test_Case_1, "Test_Case_1")
(by default 5 test cases will run)
Run experiment_15puzzle.py file to write shortest path solution to .txt file, and print action set list.

Python libraries used:
collections
time
