from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False

        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False

        if 3 - self.missionaries < 3 - self.cannibals and 3 - self.missionaries > 0:
            return False

        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return self.missionaries == other.missionaries and \
               self.cannibals == other.cannibals and \
               self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __str__(self):
        return f"M: {self.missionaries}, C: {self.cannibals}, B: {self.boat}"

def get_successors(state):
    successors = []
    actions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for action in actions:
        new_state = State(state.missionaries - action[0] * state.boat,
                          state.cannibals - action[1] * state.boat,
                          1 - state.boat)

        if new_state.is_valid():
            successors.append(new_state)

    return successors

def breadth_first_search():
    initial_state = State(3, 3, 1)
    goal_state = State(0, 0, 0)

    visited = set()
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            return construct_path(initial_state, current_state)

        visited.add(current_state)

        successors = get_successors(current_state)
        for successor in successors:
            if successor not in visited:
                queue.append(successor)

    return None

def construct_path(initial_state, goal_state):
    path = []
    current_state = goal_state

    while current_state != initial_state:
        path.append(current_state)
        current_state = path[-1]

    return path[::-1]

def print_solution(path):
    for i, state in enumerate(path):
        print(f"Step {i + 1}: {state}")

if __name__ == "__main__":
    solution_path = breadth_first_search()

    if solution_path:
        print("Solution found:")
        print_solution(solution_path)
    else:
        print("No solution found.")
