class EarthquakePredictionModel:
    def __init__(self, data):
        self.data = data
        
    def classify_magnitude(self):
        """
        Classify earthquakes into magnitude ranges:
        - Minor: < 3.0
        - Light: 3.0-4.9
        - Moderate: 5.0-5.9
        - Strong: 6.0-6.9
        - Major: 7.0-7.9
        - Great: ≥ 8.0
        """
        magnitude_bins = [0, 3.0, 4.9, 5.9, 6.9, 7.9, np.inf]
        magnitude_labels = ['Minor', 'Light', 'Moderate', 'Strong', 'Major', 'Great']
        return pd.cut(self.data['magnitude'], bins=magnitude_bins, labels=magnitude_labels)
