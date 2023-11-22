from itertools import product
from copy import deepcopy

class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

def is_valid_assignment(assignment, variable, value):
    for neighbor in assignment:
        if (neighbor, value) in assignment or (value, neighbor) in assignment:
            return False
    return True

def backtracking_search(csp):
    return backtrack({}, csp)

def backtrack(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment

    var = select_unassigned_variable(assignment, csp)
    for value in order_domain_values(var, assignment, csp):
        if is_valid_assignment(assignment, var, value):
            assignment[var] = value
            inferences = {}
            if consistent(assignment, csp):
                inferences = forward_checking(assignment, csp, var, value)
                if inferences is not None:
                    result = backtrack(assignment, csp)
                    if result is not None:
                        return result
            assignment.pop(var)
            undo_forward_checking(csp, inferences)

    return None

def consistent(assignment, csp):
    for constraint in csp.constraints:
        if constraint[0] in assignment and constraint[1] in assignment:
            if assignment[constraint[0]] == assignment[constraint[1]]:
                return False
    return True

def forward_checking(assignment, csp, var, value):
    inferences = {}
    for neighbor in csp.variables:
        if neighbor not in assignment and (var, neighbor) in csp.constraints:
            if value in csp.domains[neighbor]:
                csp.domains[neighbor].remove(value)
                if not csp.domains[neighbor]:
                    return None
                inferences[neighbor] = deepcopy(csp.domains[neighbor])
    return inferences

def undo_forward_checking(csp, inferences):
    for neighbor, values in inferences.items():
        csp.domains[neighbor] = values

def select_unassigned_variable(assignment, csp):
    unassigned = [var for var in csp.variables if var not in assignment]
    return min(unassigned, key=lambda var: len(csp.domains[var]))

def order_domain_values(var, assignment, csp):
    return csp.domains[var]

def map_coloring_csp():
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {var: ['R', 'G', 'B'] for var in variables}
    constraints = [('WA', 'NT'), ('WA', 'SA'), ('NT', 'SA'), ('NT', 'Q'), ('SA', 'Q'),
                   ('SA', 'NSW'), ('SA', 'V'), ('Q', 'NSW'), ('NSW', 'V')]
    csp = CSP(variables, domains, constraints)

    return csp

def print_assignment(assignment):
    for var, color in assignment.items():
        print(f"{var}: {color}")

if __name__ == "__main__":
    csp = map_coloring_csp()
    assignment = backtracking_search(csp)

    if assignment is not None:
        print("Map Coloring Solution:")
        print_assignment(assignment)
    else:
        print("No solution found.")
