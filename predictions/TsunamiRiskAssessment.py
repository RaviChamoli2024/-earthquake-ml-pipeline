    def assess_tsunami_risk(self):
        """
        Evaluate tsunami potential:
        - Wave generation likelihood
        - Coastal exposure
        - Warning time
        """
        tsunami_features = [
            'magnitude',
            'depth',
            'distance_to_coast',
            'ocean_depth',
            'fault_type'
        ]
        return self._calculate_tsunami_risk(tsunami_features)