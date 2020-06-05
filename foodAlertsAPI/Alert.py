from foodAlertsAPI.Problem import Problem
from foodAlertsAPI.ProductDetails import ProductDetails
from foodAlertsAPI.Status import Status
from foodAlertsAPI.BatchDescription import BatchDescription
from foodAlertsAPI.Country import Country
from foodAlertsAPI.Business import Business

class Alert:
    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        # id is written @id in the API
        self.id = dict["@id"]
        
        # assigning different values to some attributes
        if "problem" in list(dict.keys()):
            self.problem = [Problem(p) for p in dict["problem"]]

        if "productDetails" in list(dict.keys()):
            self.productDetails = [ProductDetails(d) for d in dict["productDetails"]]
        
        if "status" in list(dict.keys()):
            self.status = Status(dict["status"])

        if "country" in list(dict.keys()):
            self.country = [Country(c) for c in dict["country"]]

        if "reportingBusiness" in list(dict.keys()):#
            self.reportingBusiness = Business(dict["reportingBusiness"])

        # otherBusiness can be a single object or a list of objects
        if "otherBusiness" in list(dict.keys()):
            try:
                self.otherBusiness = Business(dict["otherBusiness"])
            except AttributeError: 
                self.otherBusiness = [Business(b) for b in dict["otherBusiness"]]


        # add optional attributes as None if not specified
        optionals = [
            "actionTaken", 
            "consumerAdvice",
            "country",
            "SMStext",
            "twitterText",
            "alertURL",
            "shortURL",
            "shortTitle",
            "relatedMedia",
            "problem",
            "productDetails",
            "reportingBusiness",
            "otherBusiness",
            "previousAlert"]

        for entry in optionals:
            if (entry not in list(dict.keys())):
                setattr(self, entry, None)


        # set strings appropriately if not specified
        strings = [
            "SMStext",
            "twitterText",
            "shortTitle"
        ]

        for entry in strings:
            if (entry not in list(dict.keys())):
                setattr(self, entry, "No text specified")