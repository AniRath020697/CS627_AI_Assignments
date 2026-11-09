# Import libraries.

import random



# num_successors determines how many successor game states each game state will have.
# A successor game state is a game state reachable after one valid action from a given game state.
# In practice, this is not chosen by an agent, but determined from the number of valid possible game states.
num_successors = 2



# Create the outline for each game state.

class GameState:
    # Initialize a game state with a value and list to store possible next game states.
    def __init__(self, value=None, successors = None, total_score = 0):
        self.value = value
        self.successors = successors if successors is not None else []
        self.total_score = total_score
        self.times_visited = 0

    
    def __repr__(self):
        if self.successors:
            children_str = "({})".format(", ".join(str(s.value) for s in self.successors))
            return "[value chosen={}, children={}]".format(self.value, children_str)
        return "[value={} (leaf)]".format(self.value)


# Helper functions for a minimax game tree.


# Check if a game state in a given tree already has some successors.
def is_leaf_gamestate(cur_gamestate):     
    if cur_gamestate.successors == []:
        return True
    else:
        return False


# Print a MCTS
def print_mcts_tree(cur_gamestate):
    
    cur_level_gamestates = [[cur_gamestate]]
    i = 1
    
    # Keep printing while more data is present.
    while cur_level_gamestates:
        # Build and print one level at a time, and keep track of next set of game states to print.
        print("Level {}:".format(i))
        next_level_gamestates = []
        level_str = ""
        
        for group in cur_level_gamestates:
            # Organize all successors of a given game state in a group.
            for gs in group:
                score_str = "{}/{}".format(gs.total_score, gs.times_visited) if gs.times_visited > 0 else "unvisited"
                level_str += "  [score={}, visits={}]".format(score_str, gs.times_visited)
                # Store the next set of game states to be printed.
                # The next set of game states are the successors of the current level's game states.
                if gs.successors:
                    next_level_gamestates.append(gs.successors)
        print(level_str)
        # Line up the next set of game states to be printed.
        cur_level_gamestates = next_level_gamestates
        i += 1



# Given a gamestate, find actions possible from that gamestate.
def find_possible_actions(cur_gamestate):
    
    # Number of actions is often discovered from assessing a game state, not manually specified.
    # Here, the number of actions is fixed to reduce complexity.
    num_actions = 3
    actions_list = []
    for i in range(1 + num_actions + 1):
        cur_action = "Move {}".format(i)
        actions_list.append(cur_action)
    return actions_list



# Perform a given action on the current gamestate and return the new resulting gamestate.
def create_successor_gamestate(cur_gamestate, given_action):
    
    # A placeholder is used here to reduce complexity. 
    # Otherwise, would perform given_action on cur_gamestate.
    return GameState()


# Function to check whether a game state is a terminal game state (win, loss or draw). 
# Will typically use knowledge of the game.
# Here, randomness is used as a placeholder to reduce complexity.
def is_game_over(cur_gamestate):
    return random.choice([True, False])




# Return the specific result (win, loss) for a given agent. 
# Will typically use knowledge of the game, but a placeholder is used here to reduce complexity.
def check_result(cur_gamestate, agent = "AgentDoe"):
    return random.choice(["Win", "Loss", "Draw"])




# Check whether a gamestate has been fully expanded.
# Here, a gamestate is fully expanded when all successor game states have been
# added to the game tree.
def is_expanded(cur_gamestate):
    if len(cur_gamestate.successors) >=  len(find_possible_actions(cur_gamestate)):
        return True
    else:
        return False
