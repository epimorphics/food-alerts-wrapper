class HazardCategory:
    """Classifies the problem as into one of the hazard categories. 
    This information is useful for analysis and retrieval but does not directly affect the default textual presentation of the alert.
    Support for this field is under discussion.


    Attributes:

        label (string): name for the hazard category
        notation (string): unique identifier for the hazard category
    """

    def __init__(self):
        for k, v in dict.items():
            setattr(self, k, v)

    def __getattr__(self, attribute):
        return None