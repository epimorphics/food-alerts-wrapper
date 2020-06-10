class Allergen:
    """ Array of allergens drawn from the controlled list of allergens. 
    For an Allergen Alert there will also be at least one allergen present on the problem statement.

    Attributes:

        label (string): name for the allergen
        notation (string): a unique identifier for the allergen
        riskStatement (string): text describing the risk from the allergen
    """


    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        # id is written @id in the API
        self.id = dict["@id"]

