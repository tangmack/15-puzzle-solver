# 15-puzzle-solver
Solver for the classic 15 puzzle game (4x4 number game)

Algorithm used is BFS. <br />
Data structures to improve speed: <br />
Python set() data structure (hash table, O(1) lookup time on average) <br />
Python deque() data structure (queue, popleft() function is O(1) versus O(n) for python list) <br />

Instructions to Run: <br />

Run experiment_15puzzle.py <br />
Script experiment_15puzzle.py  will write the shortest path solution to each test case to a .txt file. <br />
The action set list will be printed to console. <br />
5 default test cases are included, each written to a .txt file. The 5th test case writes to nodePath.txt <br />


Python libraries used: <br />
collections <br />
time <br />
