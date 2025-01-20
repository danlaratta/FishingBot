import schedule
import time
from FishingBot.services.notification_service import NotificationService


class AutomateTask:
    def __init__(self, notification: NotificationService):
        self.notification = notification


    # Creates task which is to send the notification
    def task(self):
        message = self.notification.get_message(75)
        self.notification.send_notification(message)


    # Schedule the task
    def schedule_task(self):
        # Schedule to run 9am every day
        schedule.every(10).seconds.do(self.task)


    # Run the task
    @staticmethod
    def run_task():
        print('Task automation started...')
        while True:
            schedule.run_pending()
            time.sleep(1)  # Prevent CPU overuse with a small delay
