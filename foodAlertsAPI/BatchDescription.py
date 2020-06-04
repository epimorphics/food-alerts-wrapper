class BatchDescription:
    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        # all attributes optional

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