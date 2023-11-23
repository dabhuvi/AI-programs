import random

class VacuumCleaner:
    def __init__(self, environment_size):
        self.environment_size = environment_size
        self.location = random.randint(0, environment_size - 1)
        self.state = ['Dirty' if random.random() < 0.5 else 'Clean' for _ in range(environment_size)]

    def sense(self):
        return self.location, self.state[self.location]

    def act(self, action):
        if action == 'Suck':
            self.state[self.location] = 'Clean'
        elif action == 'Left':
            self.location = max(0, self.location - 1)
        elif action == 'Right':
            self.location = min(self.environment_size - 1, self.location + 1)

    def random_action(self):
        return random.choice(['Suck', 'Left', 'Right'])

def run_simulation(vacuum_cleaner, steps):
    for step in range(steps):
        location, status = vacuum_cleaner.sense()
        print(f"Step {step + 1}: Location {location}, Status {status}")
        
        action = vacuum_cleaner.random_action()
        vacuum_cleaner.act(action)

if __name__ == "__main__":
    environment_size = 5
    vacuum_cleaner = VacuumCleaner(environment_size)
    
    print("Initial state:")
    run_simulation(vacuum_cleaner, 1)
    
    steps_to_simulate = 10
    print("\nRunning simulation:")
    run_simulation(vacuum_cleaner, steps_to_simulate)
