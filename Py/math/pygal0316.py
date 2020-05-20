from random import randint
import pygal
class Die():
    """A class representing a single die."""
    
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
        
    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)


# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
hist = pygal.Bar()

# !!!!!!
hist.force_uri_protocol = 'http'

hist.title = "Results of rolling one D6 1000 times."
# x轴数据的标签
hist.x_labels = ['1', '2', '3', '4', '5', '6']

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 'D6'是数据的标签，根据这个可以区分不同的数据
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')