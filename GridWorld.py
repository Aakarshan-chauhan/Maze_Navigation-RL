import matplotlib.pyplot as plt
import numpy as np



class Grid:
    def __init__(self, rows, cols, start):
        self.rows = rows
        self.cols = cols
        self.i = start[0]
        self.j = start[1]

    # rewards is a dictionary with key being a set of coordinates and a numerical reward associated with it
    # Actions will have the same key but a list of possible actions associated with it
    def set(self, rewards, actions):
        self.rewards = rewards
        self.actions = actions

    # to put agent into the state s
    def set_state(self, s):
        self.i = s[0]
        self.j = s[1]

    def current_state(self):
        return (self.i, self.j)

    # return a boolean if agent is in terminal state or not
    def is_terminal(self, s):
        return s not in self.actions

    def move(self, action):
        if action in self.actions[(self.i, self.j)]:
            if action == 'U':
                self.i -= 1
            elif action == 'D':
                self.i += 1
            elif action == 'R':
                self.j += 1
            elif action == 'L':
                self.j -= 1

        return self.rewards.get((self.i, self.j), 0)

    def undo_move(self, action):
        if action == 'U':
            self.i += 1
        elif action == 'D':
            self.i -= 1
        elif action == 'R':
            self.j -= 1
        elif action == 'L':
            self.j += 1

        assert(self.current_state() in self.all_states())

    def game_over(self):
        # return false if position is in actions dictionary
        # else return true
        return (self.i, self.j) not in self.actions

    def all_states(self):
        # returns all states possible

        return set(self.actions.keys()) | set(self.rewards.keys())


def standard_grid():
    # define a grid that shows the board and reward of each tile
    # and possible actions of each state
    # X means a wall and S means start
    # example
    # .  .  .  1
    # .  X  . -1
    # S  .  .  .
    g = Grid(3, 4, (2, 0))
    rewards = {(0, 3): 1, (1, 3): -1}
    actions = {
        (0, 0): ('D', 'R'),
        (0, 1): ('L', 'R'),
        (0, 2): ('L', 'D', 'R'),
        (1, 0): ('U', 'D'),
        (1, 2): ('U', 'D', 'R'),
        (2, 0): ('U', 'R'),
        (2, 1): ('L', 'R'),
        (2, 2): ('L', 'R', 'U'),
        (2, 3): ('L', 'U'),
    }

    g.set(rewards, actions)
    return g


def negative_grid(step_cost=-0.15):
    g = standard_grid()
    g.rewards.update({
        (0, 0): step_cost,
        (0, 1): step_cost,
        (0, 2): step_cost,
        (1, 0): step_cost,
        (1, 1): step_cost,
        (1, 2): step_cost,
        (2, 0): step_cost,
        (2, 1): step_cost,
        (2, 2): step_cost,
    })
    return g