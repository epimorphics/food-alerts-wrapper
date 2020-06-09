from foodAlertsAPI.Problem import Problem
from foodAlertsAPI.ProductDetails import ProductDetails
from foodAlertsAPI.Status import Status
from foodAlertsAPI.BatchDescription import BatchDescription
from foodAlertsAPI.Country import Country
from foodAlertsAPI.Business import Business
from foodAlertsAPI.RelatedMedia import RelatedMedia

class Alert:
    """Alert is the base class representing the details of an FSA Food Alert.

    Attributes:
        
        id (string): url to alert in the FSA page, same as the alertURL attribute
        title (string):   
        shortTitle (string): "None" if the API does not provide this value
        description (string):    
        created (string): represents date in ISO format
        modified (string): represents datetime in ISO format
        notation (string): unique identifier for alert used in the `foodAlertsAPI.foodAlertsAPI` getAlert() function
        country (object):  a `foodAlertsAPI.Country` object. None if unspecified by the API indicating that the alert may apply to any country in the UK
        status (object): a `foodAlertsAPI.Status` object
        type (string[]): an array of strings (URLs, one corresponding to the Alert object in the API, 
                         and another to the type of alert corresponding to the Alert object (one of "AA" - allergen, "FAFA" - food action, or "PRIN" - product recall))
        actionTaken (string):  description of the action taken, or in the case of FAFAs actions to be taken by enforcement authority
        consumerAdvice (string): text giving the advice to consumers
        SMSText (string):  	short description to be used in SMS notifications
        twitterText (string):  short description to be used in Twitter notifications
        alertURL (string):  URL for the alert on the FSA web site
        shortURL (string):    
        relatedMedia (object[]):  array of `foodAlertsAPI.RelatedMedia` objects
        problem (object[]):  array of `foodAlertsAPI.Problem` objects
        productDetails (object[]):  array of `foodAlertsAPI.ProductDetails` objects
        reportingBusiness (object[]):  a `foodAlertsAPI.Business` object
        otherBusiness (object[]):  an array of `foodAlertsAPI.Business` objects
        previousAlert (object):  an `foodAlertsAPI.Alert` object
    """


    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        keys = list(dict.keys())

        # id is written @id in the API
        self.id = dict["@id"]
        
        # assigning different values to some attributes
        if "problem" in keys:
            self.problem = [Problem(p) for p in dict["problem"]]

        if "productDetails" in keys:
            self.productDetails = [ProductDetails(d) for d in dict["productDetails"]]
        
        if "status" in keys:
            self.status = Status(dict["status"])

        if "country" in keys:
            self.country = [Country(c) for c in dict["country"]]

        if "reportingBusiness" in keys:#
            self.reportingBusiness = Business(dict["reportingBusiness"])

        if "otherBusiness" in keys:
            try:
                self.otherBusiness = [Business(dict["otherBusiness"])]
            except AttributeError: 
                self.otherBusiness = [Business(b) for b in dict["otherBusiness"]]

        if "relatedMedia" in keys:
            try:
                self.relatedMedia = [RelatedMedia(dict["relatedMedia"])]
            except AttributeError: 
                self.relatedMedia = [RelatedMedia(m) for m in dict["relatedMedia"]]

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