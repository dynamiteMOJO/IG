
from instagrapi import Client
from utils.bot_utils import random_sleep
from utils.logs import log_message
from utils.cooldowns import can_perform_action, update_last_action_timestamp

def view_feed_posts(client: Client, num_posts=10):
    """View a specified number of posts from the feed."""
    feed = client.feed_timeline(count=num_posts)
    for post in feed:
        # Simulate viewing the post for a random duration
        random_sleep(5, 15)

def like_feed_posts(client: Client, num_posts=5):
    """Like a specified number of posts from the feed."""
    feed = client.feed_timeline(count=num_posts)
    for post in feed:
        if can_perform_action("like"):
            client.media_like(post.id)
            update_last_action_timestamp("like")
            log_message(f"Liked post with ID {post.id}")
            random_sleep(2, 5)

def comment_on_feed_post(client: Client, post_id, comment_text):
    """Comment on a specific post from the feed."""
    if can_perform_action("comment"):
        client.media_comment(post_id, comment_text)
        update_last_action_timestamp("comment")
        log_message(f"Commented on post with ID {post_id}")
