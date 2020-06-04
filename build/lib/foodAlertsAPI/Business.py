class Business:
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