
# Import libraries.
import random
import math
from ai_montecarlo_program import *

random.seed(64)

# Use a UCT selection policy to choose how to go through a game tree initially.

def select_using_selection_policy(cur_gamestate, exploration_parameter):
    all_successors = cur_gamestate.successors

    if not all_successors:
        return None

    # Select any successor that has not been visited first (pure exploration)
    for successor in all_successors:
        if successor.times_visited == 0:
            return successor

    parent_visits = cur_gamestate.times_visited

    best_score = float("-inf")
    best_successor = None

    for successor in all_successors:
        # Calculate the first UCT term (exploitation)
        avg_value = successor.total_score / successor.times_visited

        # Calculate the second UCT term (exploration)
        exploration_term = exploration_parameter * math.sqrt(
            math.log(parent_visits) / successor.times_visited
        )

        # Calculate the total UCT score
        uct_score = avg_value + exploration_term

        # Update best_score and best_successor
        if uct_score > best_score:
            best_score = uct_score
            best_successor = successor

    return best_successor

print("A UCT selection policy will be used.")


# Use a playout policy to play a game from an expanded gamestate to a terminal gamestate.
# A random playout policy is used here.

def play_using_playout_policy(cur_gamestate):

    new_temporary_gamestate = GameState(cur_gamestate.value, cur_gamestate.successors)
    game_over = False

    while game_over == False:
        next_possible_actions = find_possible_actions(new_temporary_gamestate)
        action_to_play = random.choice(next_possible_actions)
        new_temporary_gamestate = create_successor_gamestate(
            new_temporary_gamestate, action_to_play
        )
        game_over = is_game_over(new_temporary_gamestate)

    game_result = check_result(new_temporary_gamestate)
    return game_result

print("A random playout policy will be used.")


# Perform a Monte Carlo tree search given a gamestate which represents the top of the game tree.

def run_mcts(gametree_top, num_iterations):
    for count in range(num_iterations):
        cur_gamestate = gametree_top
        path = [gametree_top]

        # Select portions of the tree to explore.
        while is_expanded(cur_gamestate) and is_leaf_gamestate(cur_gamestate) == False:
            cur_gamestate = select_using_selection_policy(
                cur_gamestate, c
            )
            path.append(cur_gamestate)

        # Expand if the game state is an intermediate game state.
        possible_actions = find_possible_actions(cur_gamestate)
        new_expanded_gamestate = create_successor_gamestate(
            cur_gamestate, random.choice(possible_actions)
        )
        cur_gamestate.successors.append(new_expanded_gamestate)
        path.append(new_expanded_gamestate)

        # Simulate a game from the newly expanded game state.
        gameplay_result = play_using_playout_policy(cur_gamestate)
        numeric_result = 1 if gameplay_result == "Win" else 0

        # Send the result back up the game tree.
        for previous_gamestate in reversed(path):
            previous_gamestate.times_visited += 1
            previous_gamestate.total_score += numeric_result


if __name__ == "__main__":

    c = float(input("Exploration parameter:"))
    gametree_head = GameState()
    run_mcts(gametree_head, num_iterations=20)

    print("\nGame tree (newly created):\n")
    print_mcts_tree(gametree_head)
