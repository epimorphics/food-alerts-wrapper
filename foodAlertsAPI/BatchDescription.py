class BatchDescription:
    """
    
    Attributes:

        bestBeforeDescription (string, optional): "best before" date range for the batch
        bestBeforeDate (string, optional): "best before" date (or dates) for the batch
        useByDescription (string, optional): "use by" date range for the batch
        useByDate (string, optional): "use by" date (or dates) for the batch
        batchCode (string, optional): batch number or code for the batch
        lotNumber (string, optional): lot number for the batch
        batchTextDescription (string, optional): other textual description for the batch        
    """

    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        # add optional attributes as None

        optionals = [
            "bestBeforeDescription",
            "bestBeforeDate",
            "useByDescription",
            "useByDate",
            "batchCode",
            "lotNumber",
            "batchTextDescription"
        ]

        for entry in optionals:
            if (entry not in list(dict.keys())):
                setattr(self, entry, None)
    
    def __getattr__(self, attribute):
        return None