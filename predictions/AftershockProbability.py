    def predict_aftershocks(self):
        """
        Predict aftershock characteristics:
        - Probability
        - Potential magnitude
        - Time window
        """
        aftershock_features = [
            'primary_magnitude',
            'depth',
            'time_since_main',
            'fault_mechanism',
            'stress_transfer'
        ]
        return self._calculate_aftershock_probability(aftershock_features)
