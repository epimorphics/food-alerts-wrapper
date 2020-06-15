from foodAlertsAPI.BatchDescription import BatchDescription
from foodAlertsAPI.Allergen import Allergen

class ProductDetails:
    """
    Attributes:

        productName (string): name of the affected product
        productCode (string, optional): identifying code for the affected product
        packSizeDescription (string, optional): description of the package size affected - may be weight, volume or other description
        allergen (object[]): array of allergens drawn from the controlled list of allergens
        batchDescription (object[]): an array of `foodAlertsAPI.BatchDescription` objects
        productCategory (object, optional): a `foodAlertsAPI.ProductCategory` object. Identifies the category of the affected product. 
                                  This information is used to support search and analysis and does not need to be separately included in the alert presentation.
        
    """
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

        if "allergen" in list(dict.keys()):
            allergen = [Allergen(a) for a in dict["allergen"]]
            self.allergen = allergen

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

    def __getattr__(self, attribute):
        return None