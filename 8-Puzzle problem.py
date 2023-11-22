from heapq import heappop, heappush
from itertools import chain

class PuzzleNode:
    def __init__(self, state, parent=None, move=""):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0 if parent is None else parent.cost + 1

    def __lt__(self, other):
        return self.cost + self.heuristic() < other.cost + other.heuristic()

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))

    def __str__(self):
        return "\n".join(" ".join(str(cell) if cell != 0 else "_" for cell in row) for row in self.state)

    def find_blank(self):
        for i, row in enumerate(self.state):
            for j, cell in enumerate(row):
                if cell == 0:
                    return i, j

    def heuristic(self):
        goal_positions = {(i, j): i * 3 + j for i, row in enumerate(self.state) for j in range(len(row))}
        return sum(abs(i - goal_positions[cell] // 3) + abs(j - goal_positions[cell] % 3) for i, row in enumerate(self.state) for j, cell in enumerate(row) if cell != 0)

    def get_neighbors(self):
        i, j = self.find_blank()
        neighbors = []

        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_state = [list(row) for row in self.state]
                new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                neighbors.append(PuzzleNode(new_state, self, move=new_state[ni][nj]))

        return neighbors

def solve_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    goal_state = PuzzleNode([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    open_set = [initial_node]
    closed_set = set()

    while open_set:
        current_node = heappop(open_set)

        if current_node == goal_state:
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node)

        for neighbor in current_node.get_neighbors():
            if neighbor not in closed_set and neighbor not in open_set:
                heappush(open_set, neighbor)

if __name__ == "__main__":
    initial_puzzle = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]  
    solution_path = solve_puzzle(initial_puzzle)

    if solution_path:
        print("Solution found:")
        for step, node in enumerate(solution_path):
            print(f"Step {step + 1} (Move {node.move}):")
            print(node)
            print()
    else:
        print("No solution found.")
