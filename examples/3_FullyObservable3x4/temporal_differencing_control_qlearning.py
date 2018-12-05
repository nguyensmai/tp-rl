#!/usr/bin/env python

#MIT License
#Copyright (c) 2017 Massimiliano Patacchiola
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#In this example I will use the class gridworld to generate a 3x4 world
#in which the cleaning robot will move. Using the Q-learning algorithm I
#will estimate the state-action matrix.

import numpy as np
from gridworld import GridWorld


def update_state_action(state_action_matrix, visit_counter_matrix, observation, new_observation, 
                        action, reward, alpha, gamma):
    '''Return the updated utility matrix

    @param state_action_matrix the matrix before the update
    @param observation the state obsrved at t
    @param new_observation the state observed at t+1
    @param action the action at t
    @param new_action the action at t+1
    @param reward the reward observed after the action
    @param alpha the ste size (learning rate)
    @param gamma the discount factor
    @return the updated state action matrix
    '''
    
    #TODO INSTRUCTIONS: write the code to update the state-action function : state_action_matrix
    col = observation[1] + (observation[0]*4)
    new_col = new_observation[1] + (new_observation[0]*4)
    estimate = reward + gamma* np.nanmax(state_action_matrix[:,new_col])
    delta= estimate - state_action_matrix[action,col]
    state_action_matrix[action,col]+=alpha*delta
    return state_action_matrix

def update_visit_counter(visit_counter_matrix, observation, action):
    '''Update the visit counter
   
    Counting how many times a state-action pair has been 
    visited. This information can be used during the update.
    @param visit_counter_matrix a matrix initialised with zeros
    @param observation the state observed
    @param action the action taken
    '''
    col = observation[1] + (observation[0]*4)
    visit_counter_matrix[action ,col] += 1.0
    return visit_counter_matrix

def update_policy(policy_matrix, state_action_matrix, observation):
    '''Return the updated policy matrix (q-learning)

    @param policy_matrix the matrix before the update
    @param state_action_matrix the state-action matrix
    @param observation the state obsrved at t
    @return the updated state action matrix
    '''
    #TODO INSTRUCTIONS: write the code to update the policy  : policy_matrix
    col = observation[1] + (observation[0]*4)
    policy_matrix[observation[0],observation[1]] = int(np.argmax(state_action_matrix[:,col]));
    return policy_matrix
 
def choose_action(policy_matrix, observation, epsilon=0.1):
    #TODO INSTRUCTIONS: write the code to choose an action from the policy.
    #Be Careful, the action returned must be an integer
    #option 1: take the action from the action matrix
    #option 2: take the action using epsilon-greedy
    if(np.random.random(1)<epsilon):
        action = np.random.randint(0,3);
    else:
        action= int(policy_matrix[observation[0],observation[1]]);
        
    return action

def print_policy(policy_matrix):
    '''Print the policy using specific symbol.

    * terminal state
    ^ > v < up, right, down, left
    # obstacle
    '''
    counter = 0
    shape = policy_matrix.shape
    policy_string = ""
    for row in range(shape[0]):
        for col in range(shape[1]):
            if(policy_matrix[row,col] == -1): policy_string += " *  "            
            elif(policy_matrix[row,col] == 0): policy_string += " ^  "
            elif(policy_matrix[row,col] == 1): policy_string += " >  "
            elif(policy_matrix[row,col] == 2): policy_string += " v  "           
            elif(policy_matrix[row,col] == 3): policy_string += " <  "
            elif(np.isnan(policy_matrix[row,col])): policy_string += " #  "
            counter += 1
        policy_string += '\n'
    print(policy_string)

def return_decayed_value(starting_value, global_step, decay_step):
        """Returns the decayed value.

        decayed_value = starting_value * decay_rate ^ (global_step / decay_steps)
        @param starting_value the value before decaying
        @param global_step the global step to use for decay (positive integer)
        @param decay_step the step at which the value is decayed
        """
        decayed_value = starting_value * np.power(0.1, (global_step/decay_step))
        return decayed_value


def main():

    env = GridWorld(3, 4)

    #Random policy
    policy_matrix = np.random.randint(low=0, high=4, size=(3, 4)).astype(np.float32)
    policy_matrix[1,1] = np.NaN #NaN for the obstacle at (1,1)
    policy_matrix[0,3] = policy_matrix[1,3] = -1 #No action for the terminal states
    print("Policy Matrix:")
    print(policy_matrix)
    print_policy(policy_matrix)

    #Adversarial exploration policy
    exploratory_policy_matrix = np.array([[1,      1, 1, -1],
                                          [0, np.NaN, 0, -1],
                                          [0,      1, 0,  3]])

    print("Exploratory Policy Matrix:")
    print(exploratory_policy_matrix)
    print_policy(exploratory_policy_matrix)

 
    state_action_matrix = np.zeros((4,12))
    visit_counter_matrix = np.zeros((4,12))
    gamma = 0.999
    alpha = 0.001 #constant step size
    tot_epoch = 5000000
    print_epoch = 1000

    for epoch in range(tot_epoch):
        #Reset and return the first observation
        observation = env.reset(exploring_starts=True)
        epsilon = return_decayed_value(0.1, epoch, decay_step=50000)
        is_starting = True
        for step in range(1000):
            ###1. Take an action and get new state/observation and reward
            action = choose_action(exploratory_policy_matrix, observation, epsilon=0.00)
            if(is_starting): 
                action = np.random.randint(0, 4)
                is_starting = False  
            #Move one step in the environment and get obs and reward
            new_observation, reward, done = env.step(action)

            ###3. Updating the Q-value-function (state-action matrix)
            #Updating the state-action matrix
            state_action_matrix = update_state_action(state_action_matrix, visit_counter_matrix, observation, new_observation, 
                                                      action, reward, alpha, gamma)
            ###4. Updating the policy
            policy_matrix = update_policy(policy_matrix, state_action_matrix, observation)
            #Increment the visit counter
            visit_counter_matrix = update_visit_counter(visit_counter_matrix, observation, action)
            observation = new_observation
            if done: break

        if(epoch % print_epoch == 0):
            print("")
            print("Epsilon: " + str(epsilon))
            print("State-Action matrix after " + str(epoch+1) + " iterations:") 
            print(state_action_matrix)
            print("Policy matrix after " + str(epoch+1) + " iterations:") 
            print_policy(policy_matrix)

    #Time to check the utility matrix obtained
    print("State-Action matrix after " + str(tot_epoch) + " iterations:")
    print(state_action_matrix)
    print("Policy matrix after " + str(tot_epoch) + " iterations:")
    print_policy(policy_matrix)


if __name__ == "__main__":
    main()
