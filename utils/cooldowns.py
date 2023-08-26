
# Manage cooldowns to ensure Instagram's rate limits aren't exceeded

import time

# Record the last time an action was performed
last_action_timestamps = {
    "like": 0,
    "follow": 0,
    "comment": 0,
    "view_story": 0
}

def can_perform_action(action, limit_per_day, cooldown_seconds=60):
    """Check if a specific action can be performed based on cooldowns and daily limits."""
    global last_action_timestamps

    # Determine the time since the last action
    time_since_last_action = time.time() - last_action_timestamps[action]
    
    if time_since_last_action < cooldown_seconds:
        return False

    # TODO: Implement daily limit checks
    
    return True

def update_last_action_timestamp(action):
    """Update the last performed timestamp for a specific action."""
    global last_action_timestamps
    last_action_timestamps[action] = time.time()
