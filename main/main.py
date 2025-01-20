from FishingBot.automation.automate_task import AutomateTask
from FishingBot.services.api_service import ApiService
from FishingBot.services.notification_service import NotificationService


class Main:
    @staticmethod
    def run():
        # Initialize services and dependencies
        api_service = ApiService()
        notification_service = NotificationService()
        automate_task = AutomateTask(notification_service)

        # Example usage of the ApiService (if needed)
        try:
            df = api_service.get_dataframe()
            if df is not None:
                print("Weather data successfully processed.")
        except Exception as e:
            print(f"Error while fetching weather data: {e}")

        # Start the automation task
        automate_task.schedule_task()
        automate_task.run_task()


# Entry point that runs the project
if __name__ == "__main__":
    print("Starting the project...")
    Main.run()