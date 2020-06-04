class Problem:
    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        
        # only seems to have attributes:
        #   id
        #   allergen (some don't)
        #   riskStatement

        # id is written @id in the API
        self.id = dict["@id"]

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