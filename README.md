*The following contents are potential solutions for solving a grid (or a maze) by using Reinforcement Learning.
The game consists of a grid( default: 3 x 4) which has one cell where the agent will win and one cell where it will loose.
There can be multiple walls set in the grid which the agent would avoid. The goal of the agent is to start at a position and reach the win cell.*

# The grid can be of two types:
  1. Standard grid: A normal grid. Doesnt promote shortest path to the win.
  
  2. Negative grid: Each cell has a -0.1 reward which helps the agent to prioritize the shortest path.
  
We are going to use *Bellman's Equations* to solve this grid.
# A Bellman Equations can be solved by various methods:
  1. Dynamic Programming:  - Policy Iteration
                           - Value Iteration
  2. Monte Carlo
  
  3. Temporal Difference: - SARSA
                          - Q-Learning
                          
# A Reinforcement Learning problem can be broken down into two sub parts:


  1. Prediction Problem: Calculate Values or Returns when a policy(set of actions for a particular state) is already given.

  2. Control Problem: Find the optimal policy ("best" set of actions for each state) and corresponding value function.


