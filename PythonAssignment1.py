from functools import reduce
from collections import defaultdict

class ClimateDataProcessor:
    def __init__(self):
        self.observations = []

    def insert_observation(self, location, temp, moisture):
        self.observations.append({
            'location': location,
            'temp': temp,
            'moisture': moisture
        })

    def process_data(self):
        location_stats = defaultdict(lambda: {'temps': [], 'moistures': []})
        
        for observation in self.observations:
            place = observation.get('location')
            if place:
                location_stats[place]['temps'].append(observation.get('temp'))
                location_stats[place]['moistures'].append(observation.get('moisture'))
        
        compute_mean = lambda measurements: sum(filter(None, measurements)) / len(list(filter(None, measurements))) if any(measurements) else None
        
        return {place: {
            'mean_temp': compute_mean(stats['temps']),
            'mean_moisture': compute_mean(stats['moistures'])
        } for place, stats in location_stats.items()}

    @staticmethod
    def get_numeric_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def execute_interface(self):
        print("Input climate data (press Enter for location to finish):")
        while True:
            location = input("Input location name: ")
            if not location:
                break
            temp = self.get_numeric_input("Input temperature: ")
            moisture = self.get_numeric_input("Input humidity: ")
            self.insert_observation(location, temp, moisture)
        
        processed_data = self.process_data()
        print("Processed climate data:", processed_data)


if __name__ == "__main__":
    processor = ClimateDataProcessor()
    processor.execute_interface()