from Problem import Problem
from RelatedMedia import RelatedMedia
from Country import Country

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
        
        if "relatedMedia" in list(dict.keys()):
            relatedMediaID = dict["relatedMedia"]["@id"]
            relatedMediaTitle = dict["relatedMedia"]["title"]

            self.relatedMedia = RelatedMedia(relatedMediaID, relatedMediaTitle)

        if "country" in list(dict.keys()):
            countryID = dict["country"]["@id"]
            countryLabel = dict["country"]["label"]

            self.country = Country(countryID, countryLabel)

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