from vacuum import *
import random

directions = ['north', 'south', 'east', 'west']
last_move = None
last_state = None
moves_in_direction = 0
error_check = 0
direction_sequence = 0  # Track which phase of the pattern we're in

# Single movement
def reflex_agent(dirty):
    if dirty:
        action = 'clean'
    else:
        action = 'south'
    return action

# Random movement
def random_agent(dirty):
    if dirty:
        action = 'clean'
    else:
        action = random.choice(directions)
    return action

# Remembers what it has done
def state_agent(dirty):
    global last_move, last_state, moves_in_direction, error_check

    # If current position is dirty, reset error counter and clean
    if dirty:
        action = 'clean'
        last_state = action
        error_check = 0
        return action

    # Increment error counter when moving in clean areas
    error_check += 1

    # Switch to random movement if error threshold reached
    if error_check >= 4:
        action = random.choice(directions)
        last_move = action
        moves_in_direction = 0
        # Optional: Reset error_check after some random moves
        if random.random() < 0.1:  # 10% chance to reset error counter
            error_check = 0
        return action

    # First move starts southward
    if last_move is None:
        action = 'south'
        last_move = action
        moves_in_direction = 1
        return action

    # If we just cleaned, continue in last direction
    if last_state == 'clean':
        last_state = None
        return last_move

    # Movement pattern: move in current direction until blocked,
    # then change direction in a systematic way
    if last_move == 'south':
        moves_in_direction += 1
        if moves_in_direction > 2:  # After moving south twice
            action = 'east'
            last_move = action
            moves_in_direction = 0
            return action
        return 'south'

    elif last_move == 'east':
        action = 'north'
        last_move = action
        moves_in_direction = 1
        return action

    elif last_move == 'north':
        moves_in_direction += 1
        if moves_in_direction > 2:  # After moving north twice
            action = 'west'
            last_move = action
            moves_in_direction = 0
            return action
        return 'north'

    else:
        action = 'south'
        last_move = action
        moves_in_direction = 1
        return action

# Resets the global variables
def state_agent_reset():
    global last_move, last_state, moves_in_direction, error_check
    last_state = None
    last_move = None
    moves_in_direction = 0
    error_check = 0

#run(20, 5000, random_agent)
#print(many_runs(20, 50000, 10, random_agent))

#run(20, 50000, state_agent, state_agent_reset)
print(many_runs(20, 50000, 10, state_agent, state_agent_reset))