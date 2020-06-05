from foodAlertsAPI.Problem import Problem
from foodAlertsAPI.ProductDetails import ProductDetails
from foodAlertsAPI.Status import Status
from foodAlertsAPI.BatchDescription import BatchDescription
from foodAlertsAPI.RelatedMedia import RelatedMedia
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
            problems = [Problem(p) for p in dict["problem"]]
            self.problem = problems

        if "productDetails" in list(dict.keys()):
            productDetails = [ProductDetails(d) for d in dict["productDetails"]]
            self.productDetails = productDetails
        
        if "status" in list(dict.keys()):
            self.status = Status(dict["status"])
        
        if "relatedMedia" in list(dict.keys()):
            self.relatedMedia = [RelatedMedia(r) for r in dict["relatedMedia"]]

        if "country" in list(dict.keys()):
            countries = []

            # instantiate a Country instance for each country returned
            for country in dict["country"]:
                countryID = country["@id"]
                countryLabel = country["label"]
                countries.append(Country(countryID, countryLabel))

            self.country = countries

        if "reportingBusiness" in list(dict.keys()):
            self.reportingBusiness = Business(dict["reportingBusiness"])

        if "otherBusiness" in list(dict.keys()):
            self.otherBusiness = Business(dict["otherBusiness"])


        # add optional attributes as None if not specified
        optionals = [
            "actionTaken", 
            "consumerAdvice",
            "country",
            "SMStext",
            "twitterText",
            "alertURL",
            "shortURL",
            "relatedMedia",
            "problem",
            "productDetails",
            "reportingBusiness",
            "otherBusiness",
            "previousAlert"]


        for entry in optionals:
            if (entry not in list(dict.keys())):
                setattr(self, entry, None)