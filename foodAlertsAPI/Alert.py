from Problem import Problem
from RelatedMedia import RelatedMedia
from Country import Country

class Alert:
    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)
        
        # assigning different values to some attributes
        if "problem" in list(dict.keys()):
            this.problem = Problem(dict["problem"])
        
        if "relatedMedia" in list(dict.keys()):
            relatedMediaID = dict["relatedMedia"]["@id"]
            relatedMediaTitle = dict["relatedMedia"]["title"]

            this.relatedMedia = RelatedMedia(relatedMediaID, relatedMediaTitle)

        if "country" in list(dict.keys()):
            countryID = dict["country"]["@id"]
            countryLabel = dict["country"]["label"]

            this.country = Country(countryID, countryLabel)

        # add optional attributes as None if not specified
        optionals = [
            "actionTaken", 
            "consumerAdvice",
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

    # def __init__(self,
    #             title,
    #             shortTitle,
    #             description,
    #             created,
    #             modified,
    #             notation,
    #             country,
    #             countryLabel,
    #             status,
    #             statusLabel,
    #             AlertType,
    #             actionTaken = None,
    #             consumerAdvice = None,
    #             SMStext = None,
    #             twitterText = None,
    #             alertURL = None,
    #             shortURL = None,
    #             relatedMedia = None,
    #             relatedMediaTitle = None,
    #             problem = None,
    #             productDetails = None,
    #             reportingBusiness = None,
    #             otherBusiness = None,
    #             previousAlert = None
    # ):

    #     self.title = title
    #     self.shortTitle = shortTitle
    #     self.description = description
    #     self.created = created
    #     self.modified = modified
    #     self.notation = notation
    #     self.country = country
    #     self.countryLabel = countryLabel
    #     self.status = status
    #     self.statusLabel = statusLabel
    #     self.AlertType = AlertType
    #     self.actionTaken = actionTaken
    #     self.consumerAdvice = consumerAdvice
    #     self.SMStext = SMStext
    #     self.twitterText = twitterText
    #     self.alertURL = alertURL
    #     self.shortURL = shortURL
    #     self.relatedMedia = relatedMedia
    #     self.relatedMediaTitle = relatedMediaTitle
    #     self.problem = problem
    #     self.productDetails = productDetails
    #     self.reportingBusiness = reportingBusiness
    #     self.otherBusiness = otherBusiness
    #     self.previousAlert = previousAlert