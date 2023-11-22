class VacuumCleaner:
    def __init__(self):
        self.location = (0, 0)  
        self.environment = [
            ['Dirty', 'Clean'],
            ['Clean', 'Dirty']
        ]

    def is_dirty(self):
        return self.environment[self.location[0]][self.location[1]] == 'Dirty'

    def clean(self):
        print(f"Cleaning {self.location}")
        self.environment[self.location[0]][self.location[1]] = 'Clean'

    def move_left(self):
        print("Moving left")
        self.location = (self.location[0], max(0, self.location[1] - 1))

    def move_right(self):
        print("Moving right")
        self.location = (self.location[0], min(1, self.location[1] + 1))

    def move_up(self):
        print("Moving up")
        self.location = (max(0, self.location[0] - 1), self.location[1])

    def move_down(self):
        print("Moving down")
        self.location = (min(1, self.location[0] + 1), self.location[1])

    def run(self):
        while any('Dirty' in row for row in self.environment):
            if self.is_dirty():
                self.clean()
            else:
                if self.location[1] == 0:
                    self.move_right()
                else:
                    self.move_left()
                self.clean()

        print("Environment is clean. Task completed.")

if __name__ == "__main__":
    vacuum_cleaner = VacuumCleaner()
    vacuum_cleaner.run()
