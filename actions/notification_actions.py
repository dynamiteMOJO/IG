
from instagrapi import Client
from utils.bot_utils import random_sleep
from utils.logs import log_message
from utils.cooldowns import can_perform_action, update_last_action_timestamp

def fetch_notifications(client: Client, num_notifications=10):
    """Fetch a specified number of notifications."""
    # Fetch notifications
    notifications = client.notifications(count=num_notifications)
    for notification in notifications:
        # Simulate viewing the notification for a random duration
        random_sleep(1, 3)

def mark_notifications_as_seen(client: Client):
    """Mark all notifications as seen."""
    client.notifications_seen()
    log_message("Marked all notifications as seen")
    random_sleep(1, 2)
