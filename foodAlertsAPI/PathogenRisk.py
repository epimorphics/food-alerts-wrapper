class PathogenRisk:
    """Classifies the problem as being due to actual or possible contamination with a pathogen.
    
    Attributes:

        label (string): name for the pathogen risk
        notation (string): unique identifier for the pathogen risk
        pathogen (object): indicates the actual pathogen involved. The PathogenRisk may represent actual or possible contamination with this pathogen.
        riskStatement (string): text describing the risk from this pathogen, or possible pathogen
    """

    def __init__(self):
        for k, v in dict.items():
            setattr(self, k, v)

        # id is written @id in the APi
        self.id = dict["@id"]
