import random
import numpy as np

class QLearn:
    def __init__(self, actions, epsilon, alpha, gamma):
        self.q = {}
        self.epsilon = epsilon  # exploration constant
        self.alpha = alpha      # discount constant
        self.gamma = gamma      # discount factor
        self.actions = actions

    def getQ(self, state, action):
        return self.q.get((state, action), 0.0)

    def learnQ(self, state, action, reward, value):
         #TODO update Q Value function
        self.q[(state, action)] = random.random()


    def chooseAction(self, state, return_q=False):
        #TODO :choose the next action
        action = random.choice(self.actions)
        return action


    def learn(self, state1, action1, reward, state2):
        maxqnew = max([self.getQ(state2, a) for a in self.actions])
        self.learnQ(state1, action1, reward, reward + self.gamma*maxqnew)

    def saveQ(self, filename):
        np.save(filename, self.q)

    def loadQ(self, filename):
        self.q = np.load(filename).item()
