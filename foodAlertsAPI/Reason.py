class Reason:
    """Classifies the reason for the problem as being one of a standard set of reasons. 
    This information is useful for analysis and retrieval but does not directly affect the default textual presentation of the alert. 
    Support for this field is under discussion.
    
    Attributes:

        label (string): name for the reason
        notation (string): unique identifier for the reason
    """

    def __init__(self):
        for k, v in dict.items():
            setattr(self, k, v)