
from instagrapi import Client
from utils.bot_utils import random_sleep
from utils.logs import log_message
from utils.cooldowns import can_perform_action, update_last_action_timestamp

def view_followers(client: Client, username, num_followers=10):
    """View a specified number of followers of a user."""
    followers = client.user_followers(username, count=num_followers)
    for follower in followers:
        random_sleep(2, 5)

def follow_user(client: Client, user_id):
    """Follow a specific user."""
    if can_perform_action("follow"):
        client.user_follow(user_id)
        update_last_action_timestamp("follow")
        log_message(f"Followed user with ID {user_id}")
        random_sleep(2, 5)

def unfollow_user(client: Client, user_id):
    """Unfollow a specific user."""
    if can_perform_action("unfollow"):
        client.user_unfollow(user_id)
        update_last_action_timestamp("unfollow")
        log_message(f"Unfollowed user with ID {user_id}")
        random_sleep(2, 5)
