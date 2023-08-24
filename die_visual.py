from die import Die
import pygal
""""创建投骰子的需求"""
dies = 2
die1 = Die()
die2 = Die(10)
"""掷骰子，并储存结果"""
results = []
for roll_num in range(1000):
    result = die1.roll() +  die2.roll()
    results.append(result)

"""分析结果"""
frequencies = []

max_result = die1.num_slides + die2.num_slides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()
hist.title = "Result of roiing one D6 1000 times."
hist.x_labels = list(range(dies,max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequncy pf Result"
hist.add('D6+D6',frequencies)
hist.render_to_file('die_visual.svg')
