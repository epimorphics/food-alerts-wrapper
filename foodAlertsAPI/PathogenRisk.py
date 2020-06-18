class PathogenRisk:
    """Classifies the problem as being due to actual or possible contamination with a pathogen.
    
    Attributes:

        _label (string): name for the pathogen risk
        _notation (string): unique identifier for the pathogen risk
        _pathogen (object): indicates the actual pathogen involved. The PathogenRisk may represent actual or possible contamination with this pathogen.
        _riskStatement (string): text describing the risk from this pathogen, or possible pathogen
    """

    def __init__(self):
        for k, v in dict.items():
            setattr(self, "_"+k, v)

        # id is written @id in the APi
        self._id = dict["@id"]

    def __getattr__(self, attribute):
        return None
    
    def label(self):
        """
        Returns:
            label (string): name for the pathogen risk
        """
        
        try:
            value = self._label
        except AttributeError:
            value = None

        return value
        
    def notation(self):
        """
        Returns:
            notation (string): unique identifier for the pathogen risk
        """
        
        try:
            value = self._notation
        except AttributeError:
            value = None

        return value
        
    def pathogen(self):
        """
        Returns:
            pathogen (object): indicates the actual pathogen involved. The PathogenRisk may represent actual or possible contamination with this pathogen
        """
        
        try:
            value = self._pathogen
        except AttributeError:
            value = None

        return value
        
    def riskStatement(self):
        """
        Returns:
            riskStatement (string): text describing the risk from this pathogen, or possible pathogen
        """
        
        try:
            value = self._riskStatement
        except AttributeError:
            value = None

        return value
