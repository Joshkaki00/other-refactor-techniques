# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

# Steak class
class Steak:
    def __init__(self, time, temperature, pressure, desired_state):
        self.time = time
        self.temperature = temperature
        self.pressure = pressure
        self.desired_state = desired_state

    def get_cooking_progress(self):
        return self.time * self.temperature * self.pressure * COOKED_CONSTANT

    def is_well_done(self):
        return (self.desired_state == 'well-done' and
                self.get_cooking_progress() >= WELL_DONE)

    def is_medium(self):
        return (self.desired_state == 'medium' and
                self.get_cooking_progress() >= MEDIUM)

    def is_cooking_criteria_satisfied(self):
        return self.is_well_done() or self.is_medium()

steak = Steak(
    time=30,          # [min]
    temperature=103,  # [celsius]
    pressure=20,      # [psi]
    desired_state='well-done',
)

if steak.is_cooking_criteria_satisfied():
    print('cooking is done.')
else:
    print('ongoing cooking.')
