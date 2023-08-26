
# Miscellaneous utility functions to support bot operations

import random
import time

def random_sleep(min_seconds=5, max_seconds=15):
    """Sleep for a random duration between min_seconds and max_seconds."""
    time.sleep(random.uniform(min_seconds, max_seconds))
