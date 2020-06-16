from foodAlertsAPI.Allergen import Allergen

class Problem:
    """
    Attributes:

        riskStatement (string): text describing the problem in terms of the risk to consumers
        allergen (object[]): a list of `foodAlertsAPI.Allergen` objects
        hazardCategory (object, optional): a `foodAlertsAPI.HazardCategory` object. Classifies the problem as into one of the hazard categories. 
                                   Support for this field is under discussion.
        pathogenRisk (object, optional): classifies the problem as being due to actual or possible contamination with a pathogen.
        reason (object, optional): a `foodAlertsAPI.Reason` object
    """

    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        # id is written @id in the API
        self.id = dict["@id"]

        if "allergen" in list(dict.keys()):
            allergen = [Allergen(a) for a in dict["allergen"]]
            self.allergen = allergen

        # add optional attributes as None

        optionals = [
            "hazardCategory",
            "pathogenRisk",
            "reason",
            "allergen"
        ]

        for entry in optionals:
            if (entry not in list(dict.keys())):
                setattr(self, entry, None)

    def __getattr__(self, attribute):
        return None