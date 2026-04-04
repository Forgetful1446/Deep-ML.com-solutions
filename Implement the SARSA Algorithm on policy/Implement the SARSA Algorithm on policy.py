def sarsa_update(transitions, initial_states, alpha, gamma, max_steps):
    """
    Perform SARSA updates on the given environment transitions.
    Args:
        transitions (dict): mapping (state, action) -> (reward, next_state)
        initial_states (list): list of starting states to simulate episodes from
        alpha (float): learning rate
        gamma (float): discount factor
        max_steps (int): maximum steps allowed per episode
    Returns:
        dict: final Q-table as a dictionary {(state, action): value}
    """
    # Your code here
    Q = {k: 0.0 for k in transitions}

    for initial_state in initial_states:
        state = initial_state
        
        actions = [a for (s, a) in transitions if s == state]
        action = max(actions, key=lambda a: Q[(state, a)])
        
        step = 0
        
        while state != 'terminal' and step < max_steps:
            reward, next_state = transitions[(state, action)]
            
            next_actions = [a for (s, a) in transitions if s == next_state]
            
            if len(next_actions) > 0:
                next_action = max(next_actions, key=lambda a: Q[(next_state, a)])
                target = reward + gamma * Q[(next_state, next_action)]
            else:
                next_action = None
                target = reward
            
            Q[(state, action)] = Q[(state, action)] + alpha * (target - Q[(state, action)])
            
            state = next_state
            action = next_action

            step += 1

    return Q
