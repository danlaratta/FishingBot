from pync import Notifier
from datetime import datetime
from FishingBot.services.api_service import ApiService
from FishingBot.services.calculation_service import CalculationService



class NotificationService:
    # Sends the notification
    @staticmethod
    def send_notification(message):
        try:
            Notifier.notify(
                message,
                title=f"Fishing Conditions {datetime.now().strftime('%b %-d %Y')}",
                sound=True  # Plays the default notification sound
            )
            print('Notification sent')
        except Exception as e:
            print("Notification error:", e)

    # Creates and returns the message that will be sent in the notification
    @staticmethod
    def get_message(threshold):
        api_service = ApiService()
        calc_service = CalculationService(api_service)

        overall_percent = calc_service.get_overall_day_percent()
        best_hours = calc_service.get_best_fishing_hours(threshold)
        message = f'''\n\nOverall Day:  {overall_percent}%
                       \nBest Hours(if any): \n{best_hours}
                 '''
        return message
