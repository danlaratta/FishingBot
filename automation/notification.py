from plyer import notification


class Notification:

    @staticmethod
    def send_notification(message, date):
        notification.notify(
            title= f'Fishing Conditions Update {date}',
            message= message,
            timeout= 300 # notication will last 5 mins (300 seconds)
        )

