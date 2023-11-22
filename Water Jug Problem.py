class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target_amount):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target_amount = target_amount
        self.visited_states = set()

    def is_valid_state(self, state):
        jug1_amount, jug2_amount = state
        return 0 <= jug1_amount <= self.jug1_capacity and 0 <= jug2_amount <= self.jug2_capacity

    def is_goal_state(self, state):
        return state[0] == self.target_amount or state[1] == self.target_amount

    def get_successors(self, state):
        jug1_amount, jug2_amount = state

        successors = []

        successors.append((self.jug1_capacity, jug2_amount))

        successors.append((jug1_amount, self.jug2_capacity))

        successors.append((0, jug2_amount))

        successors.append((jug1_amount, 0))

        pour_to_jug2 = min(jug1_amount, self.jug2_capacity - jug2_amount)
        successors.append((jug1_amount - pour_to_jug2, jug2_amount + pour_to_jug2))

        pour_to_jug1 = min(jug2_amount, self.jug1_capacity - jug1_amount)
        successors.append((jug1_amount + pour_to_jug1, jug2_amount - pour_to_jug1))

        return [successor for successor in successors if self.is_valid_state(successor)]

    def depth_first_search(self, current_state, path):
        if current_state in self.visited_states:
            return False

        self.visited_states.add(current_state)
        path.append(current_state)

        if self.is_goal_state(current_state):
            return True

        for successor in self.get_successors(current_state):
            if self.depth_first_search(successor, path):
                return True

        path.pop()
        return False

    def find_solution(self):
        initial_state = (0, 0)
        path = []

        if self.depth_first_search(initial_state, path):
            return path
        else:
            return None

if __name__ == "__main__":
    jug_problem = WaterJugProblem(4, 3, 2)
    solution_path = jug_problem.find_solution()

    if solution_path:
        print("Solution found:")
        for step, state in enumerate(solution_path):
            print(f"Step {step + 1}: Jug 1: {state[0]}, Jug 2: {state[1]}")
    else:
        print("No solution found.")
