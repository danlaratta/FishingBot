
class CalculationService:
    def __init__(self, api_service):
        self.api_service = api_service

    # Calculates percentage for the day
    def get_overall_day_percent(self):
        # Get dataframe containing data and points
        df = self.api_service.get_dataframe()
        if df is None:
            print('No DataFrame exists')
            return

        # Get avergage of percentage column
        avg_percentage = round(df['percentage'].mean(), 2)
        return avg_percentage


    # Return dataframe of hours and percentages where percents are above threshold for best hours to fish for the day
    def get_best_fishing_hours(self, threshold):
        # Get dataframe containing data and points
        df = self.api_service.get_dataframe()
        if df is None:
            print('No DataFrame exists')
            return

        # filter for percentages over threshold
        filtered_hours = df[df['percentage'] >= threshold].copy()

        # if filtered_hours is empty means bad fishing conditions for the day
        if filtered_hours.empty:
            print('Poor fishing conditions, not worth fishing today.')
            return 'Poor fishing conditions, not worth fishing today.'

        # if there's good conditions, format the hours and create df with hour and percentage columns
        filtered_hours['hour'] = filtered_hours['date_time'].dt.strftime('%-I%p')
        hours = filtered_hours[['hour', 'percentage']]
        return hours.to_string(index=False)
