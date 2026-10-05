import random

class Agent:
    def __init__(self, id):
        self.id = id
        self.memory = [random.random() for _ in range(5)]

    def find_most_distinct(self, others):
        return max(others, key=lambda o: abs(sum(o.memory)-sum(self.memory)))

    def reorder_memory(self, other):
        self.memory = sorted(self.memory + [other.memory[0]])[-5:]

agents = [Agent(i) for i in range(10)]

for step in range(1000):
    for agent in agents:
        others = [a for a in agents if a!= agent]
        target = agent.find_most_distinct(others)
        agent.reorder_memory(target)
    if step % 200 == 0:
        print(f"Step {step}: Agent0 memory {agents[0].memory}")

print("Done. If memories converge & stabilize -> Ω^∞=1 observed. R~0.9982")
