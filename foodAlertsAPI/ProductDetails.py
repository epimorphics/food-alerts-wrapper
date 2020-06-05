from foodAlertsAPI.BatchDescription import BatchDescription

class ProductDetails:
    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        # only seems to have attributes:
        #   id
        #   productName

        # id is written @id in the API
        self.id = dict["@id"]

        if "batchDescription" in list(dict.keys()):
            batchDescriptions = [BatchDescription(b) for b in dict["batchDescription"]]
            self.batchDescription = batchDescriptions

        # add optional attributes as None

        optionals = [
            "productCode",
            "packSizeDescription",
            "allergen",
            "batchDescription",
            "productCategory"
        ]

        for entry in optionals:
            if (entry not in list(dict.keys())):
                setattr(self, entry, None)