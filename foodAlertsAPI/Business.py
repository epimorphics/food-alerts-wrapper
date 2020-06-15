class Business:
    """
    Attributes:

        commonName (string): name by which the organisation is commonly known 
        identifier (string, optional): unique identifier for the organisation
        legalName (string, optional): legal (registered) name of the organisation   
    """

    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        # only seems to have attribute:
        #   commonName

        optionals = [
           "identifier",
           "legalName"
        ]

        for entry in optionals:
            if (entry not in list(dict.keys())):
                setattr(self, entry, None)

    def __getattr__(self, attribute):
        return None