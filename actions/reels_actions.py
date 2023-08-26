
from instagrapi import Client
from utils.bot_utils import random_sleep
from utils.logs import log_message
from utils.cooldowns import can_perform_action, update_last_action_timestamp

def watch_reels(client: Client, num_reels=10):
    """Watch a specified number of reels."""
    # Note: The exact method to fetch reels is not explicitly mentioned in the instagrapi guide,
    # but this is a placeholder to indicate the logic.
    reels = []  # Placeholder for fetching reels
    for reel in reels:
        # Simulate watching the reel for a random duration
        random_sleep(5, 15)

def like_reel(client: Client, reel_id):
    """Like a specific reel."""
    if can_perform_action("like"):
        client.media_like(reel_id)
        update_last_action_timestamp("like")
        log_message(f"Liked reel with ID {reel_id}")
        random_sleep(2, 5)
